-- Latest CPU
SELECT cpu FROM logs WHERE host='mini-siem-client1' ORDER BY id DESC LIMIT 1;
-- Latest RAM
SELECT ram FROM logs WHERE host='mini-siem-client1' ORDER BY id DESC LIMIT 1;
-- Latest disk
SELECT disk FROM logs WHERE host='mini-siem-client1' ORDER BY id DESC LIMIT 1;
-- Metrics history
SELECT strftime('%s', received_at) AS time, cpu, ram, disk FROM logs WHERE host='mini-siem-client1' ORDER BY received_at;
-- Recent alerts
SELECT created_at,host,type,value,threshold FROM alerts ORDER BY id DESC LIMIT 20;
-- Total alerts
SELECT COUNT(*) AS total_alerts FROM alerts;
-- Last seen per host
SELECT host, MAX(received_at) AS last_seen FROM logs GROUP BY host ORDER BY host;
