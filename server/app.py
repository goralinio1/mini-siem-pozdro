from flask import Flask, jsonify, request

app = Flask(__name__)
logs = []

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
    logs.append(data)
    return jsonify({"status": "ok"}), 200

@app.get("/logs")
def get_logs():
    return jsonify(logs)
