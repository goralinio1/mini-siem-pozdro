# mini-SIEM

System centralnego monitorowania i analizy zdarzeń rozwijany w ramach projektu inżynierskiego.

## Przepływ danych
`agent.py -> HTTP POST /log -> Flask -> SQLite -> reguły alertowe -> Grafana`

Agent zbiera CPU, RAM i zajętość dysku. Backend dodaje centralny znacznik czasu, zapisuje telemetrię w SQLite, sprawdza progi CPU/RAM/dysk oraz ogranicza powtarzające się alerty cooldownem 60 s. `/status` klasyfikuje host jako ACTIVE/INACTIVE przy progu 30 s.

## Katalogi
- `agent/` – agent Linux
- `server/` – Flask, SQLite i reguły alertowe
- `grafana/` – zapytania dashboardu
- `systemd/` – automatyczny start usług
- `tests/` – scenariusze i testy
- `docs/` – dokumentacja techniczna i ewidencja prac

## Historia
Historia Git pokazuje kolejne etapy implementacji i jest powiązana z identyfikatorami SIEM-xx oraz wpisami `Time spent`.
