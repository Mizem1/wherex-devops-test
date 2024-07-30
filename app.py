from flask import Flask, jsonify
from utils import system_metrics, format

app = Flask(__name__)

@app.route("/metrics", methods=["GET"])
def get_metrics():
    """
    Ruta que devuelve las métricas del sistema en formato JSON.
    """
    try:
        cpu_usage = system_metrics.get_cpu_usage()
        ram_info = system_metrics.get_ram_info()

        metrics = {
            "status": "success",
            "data": {
                "cpu_usage_percent": format.format_cpu_usage(cpu_usage),
                "memory": format.format_ram_info(ram_info),
            },
        }
        return jsonify(metrics)

    except Exception as error:
        error_message = {
            "error": "An error occurred while retrieving metrics.",
            "details": str(error)
        }
        return jsonify(error_message), 500