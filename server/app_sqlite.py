import sqlite3
from datetime import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)
DB_PATH = "mini_siem.db"
HOST_TIMEOUT_SECONDS = 30

def db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def save_log(data):
    conn=db(); conn.execute("INSERT INTO logs(host,cpu,ram,disk,received_at) VALUES(?,?,?,?,?)", (data.get("host","unknown"),data.get("cpu"),data.get("ram"),data.get("disk"),data["received_at"])); conn.commit(); conn.close()

@app.post("/log")
def receive_log():
    data=request.get_json(silent=True) or {}
    data["received_at"]=datetime.now().isoformat()
    save_log(data)
    return jsonify({"status":"ok"})

def save_alert(alert):
    conn=db(); conn.execute("INSERT INTO alerts(host,type,message,value,threshold,created_at) VALUES(?,?,?,?,?,?)", (alert["host"],alert["type"],alert.get("message"),alert.get("value"),alert.get("threshold"),datetime.now().isoformat())); conn.commit(); conn.close()
