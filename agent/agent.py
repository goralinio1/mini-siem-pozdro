import socket
import time
import psutil
import requests

SERVER_URL = "http://192.168.26.130:5000/log"

def collect_metrics():
    return {"host": socket.gethostname(), "cpu": psutil.cpu_percent(interval=1), "ram": psutil.virtual_memory().percent, "disk": psutil.disk_usage("/").percent}

while True:
    data = collect_metrics()
    try:
        response = requests.post(SERVER_URL, json=data, timeout=5)
        print("Wyslano dane:", data, "Status:", response.status_code)
    except Exception as exc:
        print("Blad wysylania:", exc)
    time.sleep(5)
