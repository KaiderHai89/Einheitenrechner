# Programm zum Umrechnen von Einheiten
# Ersteller: Kai Meiners / Josie Wöste
# Datum 20.08.24
# Letzte Änderung: 01.09.24 
######################################################################
# Menü denfinieren
def auswahlmenue():
    print("Willkommen im Auswahlmenü")
    print("Was willst du umrechen?")
    print("1. Skrupel")
    print("2. Knoten")
    print("3. Lachter")
    print("4. Gert")
    print("5. Koenigselle")
    print("6. Beenden")

# Ausgabe Einheiten
def option_1():
    print("Du hast Skrupel ausgewählt.")
    skrupel = float(input("Wie viel Skupel hast du?: "))
    # float ist der Datentyp und steht für Gleitkommazahlen, zb 5.55.
    # int zb ist der Datentyp für Ganzzahlen ohne Punkt.
    # input ist eine Funktion für die Eingabe von Daten über Tastatur.
    
    umrskr = skrupel * 1.25
    # Hier findet die eigentliche Umrechnung statt, wir schreiben das Produkt aus
    # eingegebenem Wert und Umrechnungsfaktor in eine Variable, die wir ausgeben können.
    
    print(skrupel, "Skrupel sind", umrskr, "Gramm")
    # print sorgt für Textausgabe.

def option_2():
    print("Du hast Knoten ausgewählt.")
    knoten = float(input("Wie viel Knoten hast du?: "))
    umrkno = knoten * 1.852
    print(knoten, "Konten sind", umrkno, "Kilometer pro Stunde")

def option_3():
    print("Du hast Lachter ausgewählt.")
    lachter = float(input("Wie viele Lachter hast du? "))
    umrlac = lachter * 1.938
    print(lachter, "Lachter sind", umrlac, "Meter")
    
def option_4():
    print("Du hast Gert ausgewählt.")
    gert = float(input("Wie viele Gerts hats du?: "))
    umrgert = gert * 3.6
    print(gert, "Gert sind", umrgert, "Meter")
    
def option_5():
    print("Du hast Koenigselle ausgewählt.")
    koenigselle = float(input("Wie viele Koenigsellen hast du?: "))
    umrkoe = koenigselle * 0.524
    print(koenigselle, "Koenigsellen sind", umrkoe, "Meter")
    
#Logik hinterm Auswahlmenü
def main():
    while True:
        auswahlmenue()
        wahl = input("Bitte wähle eine Option (1-6): ")

        if wahl == "1":
            option_1()
        # Hier wird die Eingabe mit unseren optionen fürs Menü verglichen.

        elif wahl == "2":
            option_2()
        elif wahl == "3":
            option_3()
        elif wahl == "4":
            option_4()
        elif wahl == "5":
            option_5()
        elif wahl == "6":
            print("Programm wird beendet...")
            break
        # break beendet eine Schleife und somit unser Auswahlmenü.
        
        else:
            print("Ungültige Eingabe, bitte versuche es erneut."
                  "Bitte Zahl ohne Punkt angeben")
        # Wenn die eingegebene option nicht vorhanden ist, erscheint diese Fehlermeldung.    

#Schleife damit das Menü direkt wieder erscheint
if True == True:
    main()
    