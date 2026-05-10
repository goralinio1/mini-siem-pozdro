import socket

def collect_metrics():
    return {"host": socket.gethostname()}

print(collect_metrics())
