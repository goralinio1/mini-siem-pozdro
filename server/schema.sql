CREATE TABLE IF NOT EXISTS logs (
 id INTEGER PRIMARY KEY AUTOINCREMENT, host TEXT NOT NULL, cpu REAL, ram REAL, disk REAL, received_at TEXT NOT NULL
);
CREATE TABLE IF NOT EXISTS alerts (
 id INTEGER PRIMARY KEY AUTOINCREMENT, host TEXT NOT NULL, type TEXT NOT NULL, message TEXT, value REAL, threshold REAL, created_at TEXT NOT NULL
);
CREATE INDEX IF NOT EXISTS idx_logs_host_time ON logs(host, received_at);
CREATE INDEX IF NOT EXISTS idx_alerts_host_time ON alerts(host, created_at);
