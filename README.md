# mini-SIEM

System centralnego monitorowania metryk hostów Linux. Repozytorium zawiera backend Flask, agenta, warstwę SQLite, konfigurację Grafany, usługi systemd i testy.

## Przepływ
`agent -> HTTP/JSON -> Flask -> storage/detection -> Grafana`

## Historia zmian i taski
Każdy commit zawiera identyfikator `SIEM-xx`, autora oraz `Time spent`. Szczegółowe zestawienie znajduje się w `docs/time-report.md` i `docs/tasks.csv`.

Przydatne polecenia:
```bash
git log --date=short --pretty=format:"%h | %ad | %an | %s"
git show <hash>
git diff <starszy_commit>..<nowszy_commit>
```
