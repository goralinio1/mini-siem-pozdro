# Deployment
1. Utwórz `/var/lib/mini-siem` i nadaj właściwe uprawnienia.
2. Utwórz środowiska venv dla serwera i agenta.
3. Zainstaluj zależności z `requirements.txt`.
4. Uruchom `server/init_db.py`.
5. Skopiuj jednostki systemd i wykonaj `daemon-reload`.
6. Włącz `mini-siem-server`, `mini-siem-agent` oraz `grafana-server`.
7. Zweryfikuj `/summary`, `/status` i dashboard.
