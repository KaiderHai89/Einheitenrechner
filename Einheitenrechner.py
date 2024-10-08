# Programm zum Umrechnen von Einheiten
# Ersteller: Kai Meiners / Josie Wöste
# Datum 20.08.24
# Letzte Änderung: 01.09.24 
######################################################################
# Variablen definieren


# Menü denfinieren
def auswahlmenue():
    print(" ")
    print("############################")
    print("Willkommen im Auswahlmenü")
    print("Was willst du umrechen?")
    print("1. Skrupel -> Gramm")
    print("2. Knoten -> Km/h")
    print("3. Lachter -> Meter")
    print("4. Gert -> Meter")
    print("5. Koenigselle -> Meter")
    print("6. Beenden")

# Ausgabe Einheiten, hier werden die Einheiten nach Auswahl mit ihrem Umrechnungsfaktor umgerechnet.

def umrechnung_skrupel_in_gramm():
    print("Du hast Skrupel ausgewählt.")
    skrupel = float(input("Wie viel Skupel hast du?: "))
    # float da wir so Gleitkommazahlen benutzen können.
    umrskrupel = skrupel * 1.25
    # die umgerechneten Werte werden in die "umr" variablen gechrieben, zb. umrskr.
    print(skrupel, "Skrupel sind", umrskrupel, "Gramm") 

def umrechnung_knoten_in_kmph():
    print("Du hast Knoten ausgewählt.")
    knoten = float(input("Wie viel Knoten hast du?: "))
    umrknoten = knoten * 1.852
    print(knoten, "Konten sind", umrknoten, "Kilometer pro Stunde")

def umrechnung_lachter_in_meter():
    print("Du hast Lachter ausgewählt.")
    lachter = float(input("Wie viele Lachter hast du? "))
    umrlachter = lachter * 1.938
    print(lachter, "Lachter sind", umrlachter, "Meter")
    
def umrechnung_gert_in_meter():
    print("Du hast Gert ausgewählt.")
    gert = float(input("Wie viele Gerts hats du?: "))
    umrgert = gert * 3.6
    print(gert, "Gert sind", umrgert, "Meter")
    
def umrechnung_koenigselle_in_meter():
    print("Du hast Koenigselle ausgewählt.")
    koenigselle = float(input("Wie viele Koenigsellen hast du?: "))
    umrkoenigselle = koenigselle * 0.524
    print(koenigselle, "Koenigsellen sind", umrkoenigselle, "Meter")
    
# Logik hinterm Auswahlmenü
while True:
    auswahlmenue()
    wahl = input("Bitte wähle eine Option (1-6): ")

    if wahl == "1":
        umrechnung_skrupel_in_gramm()
    elif wahl == "2":
        umrechnung_knoten_in_kmph()
    elif wahl == "3":
        umrechnung_lachter_in_meter()
    elif wahl == "4":
        umrechnung_gert_in_meter()
    elif wahl == "5":
        umrechnung_koenigselle_in_meter()
    elif wahl == "6":
        print(" ")
        print("########################")
        print("Programm wid beendet...")
        print("########################")
        break
    # wir benutzen break zum beenden der Schleife.
    else:
        print(" ")
        print("#################################################")
        print("Ungültige Eingabe, bitte Zahl ohne Punkt angeben.")
        print("#################################################")
