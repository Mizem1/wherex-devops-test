import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_metrics(client):
    """Prueba la ruta /metrics."""
    response = client.get('/metrics')
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "success"
    assert "cpu_usage_percent" in data["data"]
    assert "memory" in data["data"]
    assert "total_gb" in data["data"]["memory"]
    assert "used_gb" in data["data"]["memory"]

def test_get_metrics_error_handling(mocker, client):
    """Prueba el manejo de errores de la ruta /metrics."""
    mocker.patch('psutil.cpu_percent', side_effect=Exception("Test Exception"))
    response = client.get('/metrics')
    assert response.status_code == 500
    data = response.get_json()
    assert "error" in data
    assert data["error"] == "An error occurred while retrieving metrics."