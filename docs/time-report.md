# Ewidencja czasu pracy

> Czasy są roboczym oszacowaniem przygotowanym na podstawie zakresu zmian i wymagają weryfikacji przez członków zespołu.

| Task | Data | Osoba | Czas | Zakres |
|---|---|---|---:|---|
| SIEM-1 | 2026-05-09 | Damian Szczepiński | 2 h | Przygotowanie struktury projektu i środowiska |
| SIEM-2 | 2026-05-09 | Damian Szczepiński | 2.5 h | Konfiguracja serwera Ubuntu i sieci |
| SIEM-3 | 2026-05-09 | Julia Wasilewska | 3 h | Podstawowy backend Flask |
| SIEM-4 | 2026-05-09 | Julia Wasilewska | 2.5 h | Endpoint POST /log |
| SIEM-5 | 2026-05-09 | Jakub Góral | 2 h | Test POST /log i GET /logs |
| SIEM-6 | 2026-05-10 | Damian Szczepiński | 3.5 h | Utworzenie agenta Linux |
| SIEM-7 | 2026-05-10 | Damian Szczepiński | 2.5 h | Zbieranie CPU przez psutil |
| SIEM-8 | 2026-05-10 | Damian Szczepiński | 2.5 h | Dodanie RAM i dysku |
| SIEM-9 | 2026-05-10 | Damian Szczepiński | 3 h | Wysyłanie telemetrii HTTP JSON |
| SIEM-10 | 2026-05-11 | Jakub Góral | 2.5 h | Test komunikacji agent-serwer |
| SIEM-11 | 2026-05-16 | Julia Wasilewska | 3.5 h | Trwały zapis logs.jsonl |
| SIEM-12 | 2026-05-16 | Julia Wasilewska | 3 h | Zapis alerts.jsonl |
| SIEM-13 | 2026-05-17 | Julia Wasilewska | 3 h | Reguła HIGH_CPU |
| SIEM-14 | 2026-05-17 | Julia Wasilewska | 2.5 h | Reguły HIGH_RAM i HIGH_DISK |
| SIEM-15 | 2026-05-17 | Jakub Góral | 2.5 h | Test progów alertowych |
| SIEM-16 | 2026-05-18 | Julia Wasilewska | 2 h | Endpoint GET /alerts |
| SIEM-17 | 2026-06-05 | Damian Szczepiński | 4 h | Mechanizm ACTIVE/INACTIVE |
| SIEM-18 | 2026-06-05 | Damian Szczepiński | 2.5 h | HOST_TIMEOUT_SECONDS = 30 |
| SIEM-19 | 2026-06-05 | Damian Szczepiński | 3 h | Endpoint GET /status |
| SIEM-20 | 2026-06-05 | Jakub Góral | 2.5 h | Test ACTIVE -> INACTIVE -> ACTIVE |
| SIEM-21 | 2026-06-06 | Damian Szczepiński | 3.5 h | Endpoint GET /summary |
| SIEM-22 | 2026-06-06 | Jakub Góral | 2 h | Walidacja /summary i liczników |
| SIEM-23 | 2026-07-04 | Damian Szczepiński | 3 h | Projekt schematu SQLite |
| SIEM-24 | 2026-07-04 | Damian Szczepiński | 4.5 h | Migracja logów do SQLite |
| SIEM-25 | 2026-07-05 | Damian Szczepiński | 4 h | Migracja alertów do SQLite |
| SIEM-26 | 2026-07-05 | Damian Szczepiński | 3 h | Odczyt logs i alerts z SQLite |
| SIEM-27 | 2026-07-06 | Jakub Góral | 3 h | Test API po migracji SQLite |
| SIEM-28 | 2026-07-06 | Damian Szczepiński | 3.5 h | Status i summary na SQLite |
| SIEM-29 | 2026-09-12 | Julia Wasilewska | 3.5 h | Instalacja i konfiguracja Grafany |
| SIEM-30 | 2026-09-12 | Julia Wasilewska | 4 h | Integracja SQLite z Grafaną |
| SIEM-31 | 2026-09-13 | Julia Wasilewska | 3.5 h | Przeniesienie bazy do /var/lib/mini-siem |
| SIEM-32 | 2026-09-13 | Julia Wasilewska | 5 h | Dashboard CPU RAM Disk |
| SIEM-33 | 2026-09-14 | Julia Wasilewska | 4 h | Panele alertów i statusu hosta |
| SIEM-34 | 2026-09-14 | Damian Szczepiński | 3.5 h | Usługa systemd backendu |
| SIEM-35 | 2026-09-14 | Damian Szczepiński | 3 h | Usługa systemd agenta |
| SIEM-36 | 2026-09-15 | Jakub Góral | 2.5 h | Test autostartu usług |
| SIEM-37 | 2026-09-15 | Damian Szczepiński | 4 h | Cooldown alertów 60 s |
| SIEM-38 | 2026-09-15 | Jakub Góral | 3 h | Test stress-ng i deduplikacji |
| SIEM-39 | 2026-09-16 | Julia Wasilewska | 3 h | Zapytania SQL dla dashboardu |
| SIEM-40 | 2026-09-16 | Jakub Góral | 3 h | Test restartu obu VM |
| SIEM-41 | 2026-09-16 | Damian Szczepiński | 3.5 h | Backup i procedura odtworzenia |
| SIEM-42 | 2026-09-17 | Jakub Góral | 4 h | Końcowa walidacja MVP i dokumentacja testów |

## Suma

- **Damian Szczepiński: 61 h**
- **Julia Wasilewska: 42.5 h**
- **Jakub Góral: 27 h**
- **Łącznie: 130.5 h**
