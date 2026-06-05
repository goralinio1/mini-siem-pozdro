from flask import Flask, jsonify, request

app = Flask(__name__)
LOG_FILE = "logs.jsonl"

def append_jsonl(path, data):
    import json
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(data) + "\n")

def read_jsonl(path):
    import json, os
    if not os.path.exists(path): return []
    with open(path, encoding="utf-8") as f: return [json.loads(line) for line in f if line.strip()]

@app.get("/")
def health():
    return jsonify({"service": "mini-siem", "status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.post("/log")
def receive_log():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "invalid payload"}), 400
    from datetime import datetime
    data["received_at"] = datetime.now().isoformat()
    append_jsonl(LOG_FILE, data)
    return jsonify({"status": "ok"}), 200

@app.get("/logs")
def get_logs():
    return jsonify(read_jsonl(LOG_FILE))

ALERT_FILE = "alerts.jsonl"

def check_alerts(data):
    alerts = []
    if (data.get("cpu") or 0) > 80:
        alerts.append({"host": data.get("host", "unknown"), "type": "HIGH_CPU", "value": data.get("cpu"), "threshold": 80})
    if (data.get("ram") or 0) > 80:
        alerts.append({"host": data.get("host", "unknown"), "type": "HIGH_RAM", "value": data.get("ram"), "threshold": 80})
    if (data.get("disk") or 0) > 90:
        alerts.append({"host": data.get("host", "unknown"), "type": "HIGH_DISK", "value": data.get("disk"), "threshold": 90})
    return alerts

@app.get("/alerts")
def get_alerts_endpoint():
    return jsonify(read_jsonl(ALERT_FILE))

HOST_TIMEOUT_SECONDS = 30

def get_latest_status():
    from datetime import datetime
    latest = {}
    for log in read_jsonl(LOG_FILE):
        latest[log.get("host", "unknown")] = log
    now = datetime.now()
    for host, data in latest.items():
        ts = data.get("received_at")
        if not ts:
            data["state"] = "UNKNOWN"
            continue
        seconds = (now - datetime.fromisoformat(ts)).total_seconds()
        data["seconds_since_last_seen"] = round(seconds, 2)
        data["state"] = "ACTIVE" if seconds <= HOST_TIMEOUT_SECONDS else "INACTIVE"
    return latest

@app.get("/status")
def status_endpoint():
    return jsonify(get_latest_status())
