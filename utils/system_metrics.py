import psutil

def get_cpu_usage():
    """Obtiene el uso de la CPU."""
    return psutil.cpu_percent(interval=1)

def get_ram_info():
    """Obtiene la información de la memoria RAM."""
    ram_info = psutil.virtual_memory()
    return {
        "total_gb": ram_info.total / (1024 ** 3),
        "used_gb": ram_info.used / (1024 ** 3),
    }
