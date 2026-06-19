#  Kino-Kassenautomat

> Interaktives Konsolenprogramm zur Ticketverwaltung  entwickelt im Rahmen der Berufsschulausbildung zur Fachinformatikerin Anwendungsentwicklung.

##  Projektbeschreibung

Dieses Projekt simuliert einen vollstndigen Kino-Kassenautomaten. Der Nutzer kann interaktiv Tickets kaufen, Snacks hinzufgen und zwischen Bar- oder Kartenzahlung whlen. Das Programm berechnet automatisch alle anfallenden Rabatte und Gebhren und gibt eine formatierte Quittung aus. Am Ende des Tages erscheint eine Tageszusammenfassung mit Gesamteinnahmen.

##  Funktionsumfang

### Eingaben
- Name und Alter (mit vollstndiger Validierung)
- Filmtyp: 2D (9,50 ) oder 3D (12,00 )
- Ticketanzahl (begrenzt auf verfgbare Pltze)
- Snack-Option  4,20  pro Ticket
- Zahlungsart: Bar oder Karte (+1,5% Gebhr)

### Preisregeln
| Regel | Bedingung | Auswirkung |
|---|---|---|
| Alterscheck | Alter < 6 | Bestellung abgelehnt |
| Seniorenrabatt | Alter  65 | 10% auf Gesamtpreis |
| Mengenrabatt | > 5 Tickets | 5% auf Tickets |
| Mengenrabatt | > 10 Tickets | 10% auf Tickets |
| Kartengebhr | Zahlung per Karte | +1,5% auf Gesamtpreis |
| 3D-Hinweis | Alter < 12 + 3D | Hinweis: nur mit Begleitung |

### Ausgabe
- Einzelne Tickets mit Sitzplatzzuweisung (Reihe + Sitznummer)
- Formatierte Quittung mit allen Positionen und Abzgen
- Tageszusammenfassung: Bestellanzahl, verkaufte Tickets, Gesamteinnahmen

##  Verwendete Python-Konzepte

| Konzept | Anwendung im Projekt |
|---|---|
| `while`-Schleife | Hauptschleife + alle Eingabevalidierungen |
| `for`-Schleife | Ticket-Ausgabe mit Nummerierung |
| `try` / `except` | Fehlerbehandlung bei allen Nutzereingaben |
| `raise ValueError` | Eigene Fehlermeldungen (z.B. unrealistisches Alter) |
| Geschachtelte Verzweigung | Mehrfache `if/elif/else`-Blcke fr Preisregeln |
| Logische Operatoren | `and`, `or` fr kombinierte Bedingungen |
| f-Strings | Formatierte, ausgerichtete Konsolenausgabe |
| `chr()` | Sitzreihen-Buchstaben automatisch generieren |

##  Ausfhren

```bash
python Kino.py
```

> **Voraussetzungen:** Python 3.x  Keine externen Bibliotheken ntig

##  ber die Entwicklerin

Dieses Projekt entstand als bungsaufgabe in der Berufsschule. Es zeigt meine Fhigkeit, komplexe Programmlogik mit mehreren verschachtelten Bedingungen, Schleifen und Fehlerbehandlung umzusetzen.
