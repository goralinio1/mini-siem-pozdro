import sqlite3
from datetime import datetime
from flask import Flask, jsonify, request
from config import (DB_PATH, HOST_TIMEOUT_SECONDS, ALERT_COOLDOWN_SECONDS, CPU_THRESHOLD, RAM_THRESHOLD, DISK_THRESHOLD)

app = Flask(__name__)
_last_alert = {}
REQUIRED_FIELDS = ("host", "cpu", "ram", "disk")

def db():
    conn = sqlite3.connect(DB_PATH); conn.row_factory = sqlite3.Row; return conn

def validate_payload(data):
    missing=[field for field in REQUIRED_FIELDS if field not in data]
    if missing: return False, f"Missing fields: {', '.join(missing)}"
    if not isinstance(data["host"], str) or not data["host"].strip(): return False, "Invalid host"
    for field in ("cpu","ram","disk"):
        if not isinstance(data[field], (int,float)) or not 0 <= float(data[field]) <= 100: return False, f"Invalid {field}"
    return True, None

def save_log(data):
    with db() as conn: conn.execute("INSERT INTO logs(host,cpu,ram,disk,received_at) VALUES(?,?,?,?,?)", (data["host"],data["cpu"],data["ram"],data["disk"],data["received_at"]))

def save_alert(alert):
    with db() as conn: conn.execute("INSERT INTO alerts(host,type,message,value,threshold,created_at) VALUES(?,?,?,?,?,?)", (alert["host"],alert["type"],alert["message"],alert["value"],alert["threshold"],alert["created_at"]))

def rows(sql, params=()):
    with db() as conn: return [dict(r) for r in conn.execute(sql, params).fetchall()]

@app.post("/log")
def receive_log():
    data=request.get_json(silent=True) or {}
    valid,error=validate_payload(data)
    if not valid: return jsonify({"status":"error","message":error}),400
    data["received_at"]=datetime.now().isoformat(); save_log(data)
    alerts = check_alerts(data)
    for alert in alerts: save_alert(alert)
    return jsonify({"status":"ok", "alerts_generated":len(alerts)})

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
    s=latest_status(); return jsonify({"total_logs":len(rows("SELECT * FROM logs")),"total_alerts":len(rows("SELECT * FROM alerts")),"total_hosts":len(s),"active_hosts":sum(1 for x in s.values() if x["state"]=="ACTIVE"),"inactive_hosts":sum(1 for x in s.values() if x["state"]=="INACTIVE"),"unknown_hosts":0})
if __name__ == "__main__": app.run(host="0.0.0.0",port=5000)

# Alert rules are evaluated centrally after a valid telemetry sample is stored.
def build_alert(host, alert_type, value, threshold):
    return {"host":host,"type":alert_type,"message":f"{alert_type}: {value}% > {threshold}%","value":float(value),"threshold":float(threshold),"created_at":datetime.now().isoformat()}

def check_alerts(data):
    rules=(("HIGH_CPU","cpu",CPU_THRESHOLD),("HIGH_RAM","ram",RAM_THRESHOLD),("HIGH_DISK","disk",DISK_THRESHOLD))
    return [build_alert(data["host"],kind,data[field],threshold) for kind,field,threshold in rules if float(data[field]) > threshold]
