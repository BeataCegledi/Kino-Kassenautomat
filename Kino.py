# =============================================================================
# Kino-Kassenautomat
# Autor: Beata Cegledi
# Beschreibung: Konsolenprogramm zur Ticketverwaltung in einem Kino.
#               Tickets kaufen, Rabatte berechnen, Tageszusammenfassung.
#
# Konzepte: while, for, try/except, raise ValueError,
#           geschachtelte Verzweigung, logische Operatoren, f-Strings
# =============================================================================

import os

# --- Globale Variablen ---
weiter = True        # Steuert die Hauptschleife
bestell = 0          # Zaehlt Bestellungen (auch fuer Sitzreihe)
frei = 100           # Freie Sitzplaetze
ticketpreis = 0      # Preis pro Ticket (abhaengig vom Filmtyp)
gesammt = 0          # Gesamteinnahmen des Tages

# =============================================================================
# HAUPTSCHLEIFE
# =============================================================================
while weiter:
    os.system('cls')
    print("\n"*5,"*"*10," KINO-KASSENAUTOMAT ","*"*10,"\n"*3)

    # --- Namenseingabe ---
    name = input("Hallo! Gib mir deinen Namen: ")
    print(f"\n *** Willkommen, {name}! ***\n")

    # --- Altereingabe mit Fehlerbehandlung ---
    # Gueltiger Bereich: 6-120 Jahre. Unter 6: Bestellung abgelehnt. Ab 65: Seniorenrabatt.
    while True:
        try:
            alter = int(input("\nWie alt bist du? "))
            if alter > 120 or alter < 0:
                raise ValueError("\n !!! Unrealistisches Alter !!! \n")
            elif alter < 6:
                weiter = False
                raise ValueError("\n !!! Bestellung abgelehnt - du bist noch zu jung !!! \n")
            elif alter >= 65:
                bestell += 1
                print("\n !!! Glueckwunsch! Du bekommst 10% Senior-Rabatt !!! \n")
                break
            else:
                bestell += 1
                break
        except ValueError as e:
            print(e)

    print("\n------------------------------------\n")

    # --- Filmtyp-Auswahl ---
    # 2D: 9.50 EUR, 3D: 12.00 EUR
    # Hinweis fuer Kinder unter 12 bei 3D (geschachtelte Verzweigung)
    while True:
        filmtyp = input("\nFilmtyp (2 = 2D oder 3 = 3D): ")
        if filmtyp in ["2","2D","2d"]:
            ticketpreis = 9.50
            filmtyp = "2"
            break
        elif filmtyp in ["3","3D","3d"]:
            ticketpreis = 12.00
            filmtyp = "3"
            if alter < 12:
                print("\n !!! Hinweis: 3D nur mit Begleitung fuer Kinder unter 12 !!! \n")
            break
        else:
            print("\n !!! Bitte nur 2 oder 3 eingeben !!! \n")

    print("\n------------------------------------\n")

    # --- Ticketanzahl mit Mengenrabatt ---
    # >5 Tickets: 5% Rabatt | >10 Tickets: 10% Rabatt
    while True:
        try:
            stueck = int(input("\nWie viele Tickets? "))
            if stueck < 0:
                raise ValueError("\n !!! Nur positive Zahlen! !!! \n")
            elif stueck > frei:
                print(f"\n !!! Nur noch {frei} Plaetze frei !!! \n")
            elif stueck > 10:
                frei -= stueck
                rabatt = 0.90
                print("\n !!! 10% Mengenrabatt !!! \n")
                break
            elif stueck > 5:
                frei -= stueck
                rabatt = 0.95
                print("\n !!! 5% Mengenrabatt !!! \n")
                break
            else:
                frei -= stueck
                rabatt = 1
                break
        except ValueError as e:
            print("\n", e)

    print("\n------------------------------------\n")

    # --- Snack-Auswahl ---
    # Snack: 4.20 EUR pro Ticket
    while True:
        antwort = input("\nMoechtest du Snacks dazu? (j/n): ").strip().lower()
        if antwort in ["j","n"]:
            snack = (antwort == "j")
            if snack and filmtyp == "3" and alter < 12:
                print("\n !!! Snack wird vorbereitet !!! \n")
            break
        else:
            print("\n !!! Nur j oder n eingeben !!! \n")

    print("\n------------------------------------\n")

    # --- Zahlungsart ---
    # Kartenzahlung: +1,5% Gebuehr
    while True:
        antwort = input(
            "\nZahlung:\n"
            "     1: Karte (+1,5% Gebuehr)\n"
            "     2: Bar\n"
        ).strip()
        if antwort in ["1","2"]:
            karte = (antwort == "1")
            break
        else:
            print("\n !!! Nur 1 oder 2 eingeben !!! \n")

    # --- Tickets ausgeben (for-Schleife) ---
    print("\n"*5,"*"*30," TICKETS ","*"*30,"\n")
    for i in range(1, stueck+1):
        print(f"{i}. Ticket von {stueck} | Film: {filmtyp}D | Reihe {chr(64+bestell)}, Sitz {5+i}")
        print("\n","-"*70,"\n")

    # --- Quittung ---
    print("*"*70,"\n")
    print("\n"*2," "*20,"  Q U I T T U N G  \n")
    print("\n"*2,"*"*70,"\n")
    print(f"\nKunde: {name}  / Alter: {alter}\nFilm: {filmtyp}D\nBestellungsnummer: {bestell}\n")
    print("\n","-"*70,"\n")

    # Basispreis
    preis = stueck * ticketpreis
    print(f"Tickets ({stueck:3} x {ticketpreis:4.2f} EUR) {preis:10.2f} EUR")

    # Snack: 4.20 EUR pro Ticket
    if snack:
        snackpreis = stueck * 4.20
        print(f"Snacks  ({stueck:3} x 4.20 EUR) {snackpreis:9.2f} EUR")
        preis += snackpreis

    # Senior-Rabatt 10%
    if alter >= 65:
        abzug = round(preis * 0.10, 2)
        print(f"Senioren-Rabatt (10%):        -{abzug:.2f} EUR")
        preis *= 0.90

    # Mengenrabatt
    if rabatt == 0.90:
        abzug = round(preis * 0.10, 2)
        print(f"Mengenrabatt (10%):           -{abzug:.2f} EUR")
        preis *= rabatt
    elif rabatt == 0.95:
        abzug = round(preis * 0.05, 2)
        print(f"Mengenrabatt (5%):            -{abzug:.2f} EUR")
        preis *= rabatt

    # Kartengebuehr 1,5%
    if karte:
        gebuehr = round(preis * 0.015, 2)
        print(f"Kartengebuehr (1,5%):         +{gebuehr:.2f} EUR")
        preis *= 1.015

    print("\n","-"*70,"\n")
    print(f"Zu zahlen:                  {preis:7.2f} EUR")
    gesammt += preis

    # --- Nochmal einkaufen? ---
    while True:
        again = input("\n\nNochmal einkaufen? (j/n): ").lower()
        if again == "n":
            print("\nWir freuen uns auf deinen naechsten Besuch!")
            weiter = False
            break
        elif again == "j":
            break
        else:
            print("\nBitte nur j oder n eingeben!")

# =============================================================================
# TAGESZUSAMMENFASSUNG
# =============================================================================
print("\n"*3,"*"*70,"\n")
print(" "*10,"  T A G E S Z U S A M M E N F A S S U N G  \n")
print("*"*70,"\n")
print(f"\nBestellungen heute:    {bestell}")
print(f"Verkaufte Tickets:     {100 - frei}")
print(f"Gesamteinnahmen:       {round(gesammt, 2):.2f} EUR")
print("\n"*2,"*"*70,"\n")
print(" "*14,"  Schoenen Feierabend !!!  \n")
print("*"*70,"\n")
