
#Deklarationen

weiter = True
bestell = 0
frei = 100
ticketpreis = 0
gesammt = 0
import os

while weiter: 
# EINGABEN
    os.system('cls')    
    print("\n"*5,"*"*10," KINO-KASSENAUTOMAT ","*"*10,"\n"*3)    
    name = input("Hallo! gib mir dein Name: ")
    print("\n *** Willkommen ",name,"! ***\n")

#Altereingabe
    while True:
        try: 
            alter = int(input("\nWie alt bist du? "))
            if alter > 120 or alter < 0: 
                raise ValueError("\n !!! Unrealistische Alter !!! \n")
            elif alter < 6:
                weiter = False
                raise ValueError("\n !!! Bestellung abgeleht, du bist noch zu jung !!! \n")
            elif alter >= 65: 
                bestell += 1
                print("\n !!! Glückwunsch! Du bekommst 10% Senior-Rabatt auf Tickets !!! \n")
                break
            else:
                bestell +=1
                break
        except ValueError as e:
            print(e)
    print("\n------------------------------------\n")

#Filmtyp
    while True:
 #       try: 
            filmtyp = input("\nWelches Filmtyp möchtest du anschauen (2 = 2D oder 3 = 3D) ")
            if filmtyp in ["2" or "2D" or "2d"]:
                ticketpreis = 9.5
                break
            elif filmtyp in ["3" or "3D" or "3d"]:
                ticketpreis = 12    
                break
            else:
                print("\n !!! Falsche Eingabe! Bitte nur 2 oder 3 eingeben !!! \n")
  
    print("\n------------------------------------\n")

#TicketsAnzahl
    while True:
        try: 
            stück = int(input("\nWie viele Tickets brauchst du? "))
            if stück < 0:
               raise ValueError("\n !!! Bitte nur positive Zahlen eingeben! !!! \n")  
            elif stück > frei:
                print("\n !!! Wir haben leider nur ",frei," Plätze frei !!! \n")
            elif stück > 5:
                frei -= stück
                if stück > 10:
                    rabatt = 0.9
                    print("\n !!! Du bekommst 10% Mengenrabatt !!! \n")
                    break
                else:
                    rabatt = 0.95
                    print("\n !!! Du bekommst 5% Mengenrabatt !!! \n")  
                    break 
            else:
                frei -= stück
                rabatt = 1
                break
        except ValueError as e:
            print("\n",e)
     
    print("\n------------------------------------\n")

#Snack
    while True:
        antwort = (input("\nMöchtest du auch Snack dazu (J/N)? ")).strip().lower()
        if antwort in ["j","n"]:
            snack = (antwort == "j")
            break
        else:
            print("\n !!! Falsche Eingabe! Bitte nur j oder n eingeben !!! \n")

    print("\n------------------------------------\n")        

#Zahlungsmetode
    while True:
        antwort = (input("\nWie möchtest du Zahlen?\n     1: Karte (Es wird ein Gebühr von 1,5% draufgerechnet!\n     2: Bar\n")).strip()
        if antwort in ["1","2"]:
            karte = (antwort == "1")
            break
        else:
            print("\n !!! Falsche Eingabe! Bitte nur 1 oder 2 eingeben !!! \n")

#AUSGABE

#Ticket
    print("\n"*5,"*"*30," TICKETS ","*"*30,"\n")
    for i in range(1,stück+1):
        print(i,". Ticket von ",stück," Film: ",filmtyp,"D Sitzplatz: Reiche ",chr(64+bestell),", Sitz ",5+i)
        print("\n","-"*70,"\n")          
  
#Quittung     
    print("*"*70,"\n")
    print("\n"*2," "*20,"☺☺☺  Q U I T T U N G  ☺☺☺\n")
    print("\n"*2,"*"*70,"\n")
    print("\nKunde: ",name, "  / Alter: ",alter,"\n\nFilm:                          ",filmtyp,"D\nBestellungsnummer:               ",bestell,"\n")
    print("\n","-"*70,"\n")
    print("Tickets (%3i x %4.2f ) %13.2f" % (stück, ticketpreis, (stück*ticketpreis)))
    preis = stück*ticketpreis
    if snack:
        print("Snacks  (%3i x 4.20€ ) %12.2f" % (stück,(stück*4.2))) 
        preis += stück*4.2    
    if alter > 65:
        print("Senioren-Rabatt:             ",-round((preis*0.10),2))
        preis = preis * 0.9        
    if rabatt == 0.9:
        preis = preis*rabatt
        print("Mengenrabatt von 10%:        ",-round((preis*0.1),2))        
    if rabatt == 0.95:
        preis = preis*rabatt            
        print("Mengenrabatt von 5%:         ",-round((preis*0.05),2))        
    if karte:
        print("Kartengebühr (1,5%):          ",round((preis*0.015),2))
        preis =  preis*1.015
    print("\n","-"*70,"\n")
    print("Zu zahlen ist:              %7.2f" % (preis))
    gesammt += preis
    while True:
        print("\n","-"*70,"\n")
        again = input("\n\n\nMöchtest du nochmal einkaufen (j/n?").lower()
        if again == "n":
            print("\n\n------------------------------------\n")
            print("Wir freuen uns auf dich nächstes mal wieder!")
            print("\n------------------------------------\n")
            weiter = False
            break
        elif again == "j":
            break
        else:
            print("\nBitte nur j oder n eingeben!")                        
#os.system('cls')    
print("\n"*3,"*"*70,"\n")
print("\n"*2," "*10,"☺☺☺  T A G ES Z U S A M M E N F A S S U N G  ☺☺☺\n")
print("\n"*2,"*"*70,"\n")
print("\nBestellungen heute:     ",bestell,    "\nVerkaufte Tickets:     ",(100-frei),"\nGesammteinkommen:  ",round(gesammt,2))
print("\n"*3,"*"*70,"\n")
print("\n"*2," "*14,"☺☺☺  Schönen Feierabend !!!  ☺☺☺\n")
print("\n"*2,"*"*70,"\n")
