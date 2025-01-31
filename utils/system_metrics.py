"""
This module contains functions to retrieve system metrics such as CPU usage
and RAM information using the psutil library.
"""
import psutil

def get_cpu_usage():
    """Gets the CPU usage."""
    return psutil.cpu_percent(interval=1)

def get_ram_info():
    """Gets the RAM information."""
    ram_info = psutil.virtual_memory()
    return {
        "total_gb": ram_info.total / (1024 ** 3),
        "used_gb": ram_info.used / (1024 ** 3),
    }
