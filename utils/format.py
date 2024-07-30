def format_cpu_usage(cpu_usage):
    """Formatea el uso de la CPU."""
    return round(cpu_usage, 2)

def format_ram_info(ram_info):
    """Formatea la información de la memoria RAM."""
    return {
        "total_gb": round(ram_info['total_gb'], 2),
        "used_gb": round(ram_info['used_gb'], 2),
    }