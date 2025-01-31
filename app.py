"""
This module contains the Flask application and routes for retrieving
system metrics such as CPU usage and RAM information.
"""
from flask import Flask, jsonify
from utils import system_metrics, format as format_utils

app = Flask(__name__)

@app.route("/metrics", methods=["GET"])
def get_metrics():
    """
    Route that returns system metrics in JSON format.
    """
    try:
        cpu_usage = system_metrics.get_cpu_usage()
        ram_info = system_metrics.get_ram_info()

        metrics = {
            "status": "success",
            "data": {
                "cpu_usage_percent": format_utils.format_cpu_usage(cpu_usage),
                "memory": format_utils.format_ram_info(ram_info),
            },
        }
        return jsonify(metrics)

    except Exception as error:
        error_message = {
            "error": "An error occurred while retrieving metrics.",
            "details": str(error)
        }
        return jsonify(error_message), 500
