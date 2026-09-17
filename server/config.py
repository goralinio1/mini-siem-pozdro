import os

DB_PATH = os.getenv("MINI_SIEM_DB_PATH", "/var/lib/mini-siem/mini_siem.db")
HOST_TIMEOUT_SECONDS = int(os.getenv("MINI_SIEM_HOST_TIMEOUT", "30"))
ALERT_COOLDOWN_SECONDS = int(os.getenv("MINI_SIEM_ALERT_COOLDOWN", "60"))
CPU_THRESHOLD = float(os.getenv("MINI_SIEM_CPU_THRESHOLD", "80"))
RAM_THRESHOLD = float(os.getenv("MINI_SIEM_RAM_THRESHOLD", "80"))
DISK_THRESHOLD = float(os.getenv("MINI_SIEM_DISK_THRESHOLD", "90"))
