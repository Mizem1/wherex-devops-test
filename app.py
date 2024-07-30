from flask import Flask, jsonify
import psutil

app = Flask(__name__)

@app.route("/metrics", methods=["GET"])
def get_metrics():
    """
    Ruta que devuelve las métricas del sistema en formato JSON.
    """
    try:
        cpu_usage = psutil.cpu_percent(interval=1) 

        ram_info = psutil.virtual_memory()
        ram_total_mb = ram_info.total / (1024 ** 2)
        ram_used_mb = ram_info.used / (1024 ** 2)    
        ram_available_mb = ram_info.available / (1024 ** 2)  


        metrics = {
            "status": "success",
            "data": {
                "cpu_usage_percent": round(cpu_usage, 2),
                "memory": {
                    "total_mb": round(ram_total_mb, 2),
                    "used_mb": round(ram_used_mb, 2),
                    "available_mb": round(ram_available_mb, 2)
                }
            },
        }
        return jsonify(metrics)

    except Exception as error:
        error_message = {
            "error": "An error occurred while retrieving metrics.",
            "details": str(error)
        }
        return jsonify(error_message), 500