# mini-SIEM

System centralnego monitorowania metryk hostów Linux. Repozytorium zawiera backend Flask, agenta, warstwę SQLite, konfigurację Grafany, usługi systemd i testy.

## Przepływ
`agent -> HTTP/JSON -> Flask -> storage/detection -> Grafana`
