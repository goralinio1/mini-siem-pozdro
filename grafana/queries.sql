-- CPU
SELECT received_at, cpu FROM logs WHERE host='mini-siem-client1' ORDER BY id DESC LIMIT 100;
-- RAM
SELECT received_at, ram FROM logs WHERE host='mini-siem-client1' ORDER BY id DESC LIMIT 100;
-- DISK
SELECT received_at, disk FROM logs WHERE host='mini-siem-client1' ORDER BY id DESC LIMIT 100;

-- Recent alerts
SELECT * FROM alerts ORDER BY id DESC LIMIT 20;
-- Total alerts
SELECT COUNT(*) AS total_alerts FROM alerts;

-- Host status helper
SELECT host, MAX(received_at) AS last_seen FROM logs GROUP BY host;
