"""
This module contains utility functions for formatting system metrics.
"""
def format_cpu_usage(cpu_usage):
    """Formats the CPU usage."""
    return round(cpu_usage, 2)

def format_ram_info(ram_info):
    """Formats the RAM information."""
    return {
        "total_gb": round(ram_info['total_gb'], 2),
        "used_gb": round(ram_info['used_gb'], 2),
    }
