# ACTIVE -> INACTIVE -> ACTIVE
1. Sprawdź `/status` przy działającym agencie.
2. Zatrzymaj `mini-siem-agent`.
3. Odczekaj ponad 30 sekund.
4. Potwierdź `INACTIVE`.
5. Uruchom usługę ponownie.
6. Potwierdź powrót do `ACTIVE` po kolejnej próbce.
