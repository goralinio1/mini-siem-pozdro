import socket
import psutil

def collect_metrics():
    return {
        "host": socket.gethostname(),
        "cpu": psutil.cpu_percent(interval=1),
        "ram": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent,
    }

print(collect_metrics())
