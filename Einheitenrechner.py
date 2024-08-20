# Programm zum Umrechnen von Einheiten
# Ersteller: Kai Meiners
# Datum 20.08.24
# Letzte Änderung: 20.08.24 
######################################################################
# Einheiten definieren
skrupel = float(input("Wie viele Skrupel hast du? "))
knoten = float(input("Mit wie viel Knoten fährst du? "))
lachter = float(input("Wie viele Lachter hast du? "))
gert = float(input("Wie viele Gerts hast du? "))
koenigselle = float(input("Wie viele Königsellen hast du? "))
# Umrechnungen definieren
umrskr = skrupel * 1.25
umrkno = knoten * 1.852
umrlac = lachter * 1.938
umrger = gert * 3.6
umrkoe = koenigselle * 0.524
# Ergebnisse ausgeben
print(skrupel, "Skrupel sind", umrskr, "Gramm")
print(knoten, "Knoten sind", umrkno, "Kilometer pro Stunde")
print(lachter, "Lachter sind", umrlac, "Meter")
print(gert, "Gert sind", umrger, "Meter")
print(koenigselle, "Königsellen sind", umrkoe, "Meter")
