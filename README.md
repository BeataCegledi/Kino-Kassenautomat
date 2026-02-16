# Projektaufgabe: „Kassenautomat im Kino“

Du programmierst einen kleinen Kassenautomaten, der Tickets verkauft. Der Nutzer
kann mehrere Bestellungen hintereinander machen, bis er beendet. Es gibt Rabatte,
Altersregeln, Fehlerbehandlung und eine formatierte Rechnung.

---

## 1) Eingaben (Input)

Der Automat fragt den Nutzer in einer Schleife nach:

- Name (String)
- Alter (Ganzzahl)
- Filmtyp (2D oder 3D)
- Anzahl Tickets (Ganzzahl)
- Snack (ja/nein)
- Zahlungsmethode (karte oder bar)

Am Ende jeder Bestellung: **weitere Bestellung? (ja/nein)**

---

## 2) Regeln & Rechnen

### Ticketpreise
- **2D:** 9.50 €
- **3D:** 12.00 €

### Altersregel
- Alter < 0 oder > 120 → `ValueError("Unrealistisches Alter!")`
- Alter < 6 → Bestellung ablehnen („Zu jung“)
- Alter ≥ 65 → **Senior-Rabatt 10%**

### Mengenrabatt
- Tickets ≥ 5 → **5% Rabatt**
- Tickets ≥ 10 → **10% Rabatt**
- *(Nur ein Rabatt darf gelten!)*

### Snackpreis
- Snack „ja“ → **4.20 € pro Ticket**
- Snack „nein“ → 0 €

### Kartengebühr
- Zahlung „karte“ → **+1.5% Gebühr**
- Zahlung „bar“ → keine Gebühr

---

## 3) Vorgaben zu Kontrollstrukturen

### A) while-Schleife
Der Automat läuft, bis der Nutzer „nein“ bei „weitere Bestellung?“ eingibt.

### B) Fehler abfangen
Numerische Eingaben müssen geschützt werden:
- Bei Eingabe wie „abc“ → Fehlermeldung → erneut fragen.

### C) Fehler erzeugen
- Alter < 0 oder > 120 → `raise ValueError("Unrealistisches Alter!")`
- Ticketanzahl ≤ 0 → `raise ValueError("Ticketanzahl muss > 0 sein!")`

### D) for-Schleife
Nach jeder Bestellung:
Ticket 1/3: 3D - Reihe A (Reihe kann statisch oder dynamisch sein. Bei mir jede Bestellung andere Reiche)

### E) Geschachtelte Verzweigung
Beispiel:
- Wenn Filmtyp 3D **und** Alter < 12 → „3D nur mit Begleitung empfohlen“
- Wenn zusätzlich Snack „ja“ → „Snack wird vorbereitet“

### F) Logische Operatoren
Mindestens einmal sinnvoll nutzen:
- `and`
- `or`
- `not`

---

## 4) Ausgabe Rechnung

Die Rechnung enthält:

- Name, Alter, Filmtyp
- Tickets, Einzelpreis, Zwischensumme
- Rabatte (Senior / Menge)
- Snack-Kosten
- Kartengebühr (falls Karte)
- Endsumme

**Formatierung:**
- Geldwerte mit **2 Nachkommastellen**
- Ausrichtung per f-Strings

### Beispiel:
Kino-Kasse - Rechnung
Kunde: Mia (Alter: 17)
Film: 3D
Position                     Betrag Tickets (3 x 12.00€)         36.00€ Snack (3 x 4.20€)            12.60€ Kartengebühr (1.5%)           0.73€
Zu zahlen:                   49.33€

---

## 5) Tageszusammenfassung

Am Ende des Programms:

- Anzahl aller Bestellungen
- Summe aller verkauften Tickets
- Gesamteinnahmen (formatiert)

---

## Muss-Checkliste

☒ Eingabe / Ausgabe  
☒ Rechnen  
☒ String-Verkettung  
☒ Vergleichsoperatoren  
☒ Einfache + mehrfache + geschachtelte Verzweigung  
☒ Logische Operatoren  
☒ for-Schleife  
☒ while-Schleife  
☒ Formatierte Ausgaben (f-Strings)  
☒ Fehler abfangen (try/except)  
☒ Fehler erzeugen (raise)
