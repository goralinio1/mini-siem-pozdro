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
