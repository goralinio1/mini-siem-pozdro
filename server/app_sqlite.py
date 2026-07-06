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

def rows(sql):
    conn=db(); result=[dict(r) for r in conn.execute(sql).fetchall()]; conn.close(); return result

@app.get("/logs")
def logs_endpoint(): return jsonify(rows("SELECT * FROM logs ORDER BY id ASC"))
@app.get("/alerts")
def alerts_endpoint(): return jsonify(rows("SELECT * FROM alerts ORDER BY id ASC"))

def latest_status():
    result={}
    for row in rows("SELECT * FROM logs ORDER BY id ASC"): result[row["host"]]=row
    now=datetime.now()
    for data in result.values():
        sec=(now-datetime.fromisoformat(data["received_at"])).total_seconds(); data["seconds_since_last_seen"]=round(sec,2); data["state"]="ACTIVE" if sec<=HOST_TIMEOUT_SECONDS else "INACTIVE"
    return result
@app.get("/status")
def status_endpoint(): return jsonify(latest_status())
@app.get("/summary")
def summary_endpoint():
    s=latest_status(); return jsonify({"total_logs":len(rows("SELECT * FROM logs")),"total_alerts":len(rows("SELECT * FROM alerts")),"total_hosts":len(s),"active_hosts":sum(1 for x in s.values() if x["state"]=="ACTIVE"),"inactive_hosts":sum(1 for x in s.values() if x["state"]=="INACTIVE")})

if __name__ == "__main__": app.run(host="0.0.0.0", port=5000)
