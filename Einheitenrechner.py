def auswahlmenue():
    print("Willkommen im Auswahlmenü")
    print("Was willst du umrechen?")
    print("1. Skrupel")
    print("2. Knoten")
    print("3. Lachter")
    print("4. Gert")
    print("5. Koenigselle")
    print("6. Beenden")

def option_1():
    print("Du hast Skrupel ausgewählt.")
    skrupel = float(input("Wie viel Skupel hast du?: "))
    umrskr = skrupel * 1.25
    print(skrupel, "Skrupel sind", umrskr, "Gramm")

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
    
def main():
    while True:
        auswahlmenue()
        wahl = input("Bitte wähle eine Option (1-6): ")

        if wahl == "1":
            option_1()
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
        else:
            print("Ungültige Eingabe, bitte versuche es erneut."
                  "Bitte Zahl ohne Punkt angeben")

if True == True:
    main()
    