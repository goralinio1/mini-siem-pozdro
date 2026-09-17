import socket
import time
import psutil
import requests
from config import SERVER_URL, SEND_INTERVAL, REQUEST_TIMEOUT

def collect_metrics():
    return {"host":socket.gethostname(),"cpu":psutil.cpu_percent(interval=1),"ram":psutil.virtual_memory().percent,"disk":psutil.disk_usage("/").percent}

def send_metrics(data):
    return requests.post(SERVER_URL,json=data,timeout=REQUEST_TIMEOUT)

def run():
    while True:
        data=collect_metrics()
        try:
            response=send_metrics(data)
            print("Wyslano dane:",data,"Status:",response.status_code)
        except requests.RequestException as exc:
            print("Blad wysylania:",exc)
        time.sleep(SEND_INTERVAL)

if __name__ == "__main__":
    run()
