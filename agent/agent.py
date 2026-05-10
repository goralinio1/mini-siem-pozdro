import socket
import psutil

def collect_metrics():
    return {"host": socket.gethostname(), "cpu": psutil.cpu_percent(interval=1)}

print(collect_metrics())
