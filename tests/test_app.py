"""
Unit tests for the /metrics endpoint in the Flask application.
"""
from unittest.mock import patch
import unittest
from app import app

class TestMetrics(unittest.TestCase):
    """
    Test case for testing the /metrics endpoint and its error handling.
    """
    def setUp(self):
        """Create a test client before each test."""
        self.client = app.test_client()

    def test_metrics_success(self):
        """Test successful retrieval of metrics."""
        response = self.client.get('/metrics')
        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertEqual(data["status"], "success")
        self.assertIn("cpu_usage_percent", data["data"])
        self.assertIn("memory", data["data"])
        self.assertIn("total_gb", data["data"]["memory"])
        self.assertIn("used_gb", data["data"]["memory"])

    @patch("psutil.cpu_percent", side_effect=Exception("Test Exception"))
    def test_metrics_failure(self, mock_cpu_percent):
        """Test error handling when retrieving metrics."""
        print("mock_cpu_percent", mock_cpu_percent)
        response = self.client.get('/metrics')
        self.assertEqual(
            response.status_code,
            500,
            "Expected HTTP 500 when metrics retrieval fails"
        )

        data = response.get_json()
        self.assertIn("error", data, "Response should contain an 'error' field")
        self.assertEqual(
            data["error"],
            "An error occurred while retrieving metrics.",
            "Error message mismatch"
        )
