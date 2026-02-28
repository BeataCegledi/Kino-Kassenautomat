# 🎬 Kino-Kassenautomat

Konsolenprogramm zur Ticketverwaltung in einem Kino – entwickelt im Rahmen der Berufsschulausbildung zur Fachinformatikerin.

## Funktionsumfang

Der Nutzer kann interaktiv Tickets kaufen. Das Programm berechnet automatisch Rabatte, Snackkosten und Kartengebühren und gibt eine formatierte Quittung aus. Am Ende erscheint eine Tageszusammenfassung.

### Eingaben
- Name und Alter (mit Validierung)
- Filmtyp: 2D (9,50 €) oder 3D (12,00 €)
- Ticketanzahl (max. verfügbare Plätze)
- Snack (ja/nein) – 4,20 € pro Ticket
- Zahlungsart: Bar oder Karte (+1,5% Gebühr)

### Preisregeln
| Regel | Bedingung | Auswirkung |
|---|---|---|
| Alterscheck | Alter < 6 | Bestellung abgelehnt |
| Seniorenrabatt | Alter ≥ 65 | -10% |
| Mengenrabatt | > 5 Tickets | -5% |
| Mengenrabatt | > 10 Tickets | -10% |
| Kartengebühr | Zahlung per Karte | +1,5% |

## Verwendete Python-Konzepte
- `while`-Schleife (Hauptschleife + Eingabevalidierung)
- `for`-Schleife (Ticket-Ausgabe)
- `try` / `except` (Fehlerbehandlung bei Eingaben)
- `raise ValueError` (Fehler erzeugen)
- Geschachtelte Verzweigung (`if` / `elif` / `else`)
- Logische Operatoren (`and`, `or`, `not`)
- f-Strings (formatierte Ausgabe)

## Ausführen

```bash
python Kino.py
```

> Voraussetzungen: Python 3.x, keine externen Bibliotheken
