SELECT l.*
FROM logs l
JOIN (SELECT host, MAX(id) AS max_id FROM logs GROUP BY host) latest
  ON latest.max_id = l.id
ORDER BY l.host;
