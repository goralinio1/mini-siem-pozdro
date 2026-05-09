from flask import Flask, jsonify, request

app = Flask(__name__)
logs = []

@app.get("/")
def health():
    return jsonify({"service": "mini-siem", "status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
