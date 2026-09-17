# End-to-end acceptance
- backend odpowiada na `/summary`
- agent cyklicznie zwiększa `total_logs`
- CPU/RAM/disk są widoczne w SQLite
- Grafana odczytuje tę samą bazę
- `stress-ng` powoduje `HIGH_CPU`
- cooldown ogranicza duplikaty w 60 s
- zatrzymanie agenta daje `INACTIVE` po >30 s
- restart usług przywraca przepływ danych
- backup obejmuje kod, bazę i konfigurację
