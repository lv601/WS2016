menu = [["Suppe", "Suppe von vorgestern", 2.30],["Suppe deluxe", "für die große Geldbörse", 1300.5]]
<<<<<<< HEAD
print(" Menu ".center(56, "*") + "\nVorspeisen:\n{menu[0][0]}\t"\
      "\t\t{menu[0][1]}\t\t{menu[0][2]:.2f} Eur\n{menu[1][0]}\t{menu[1][1]}\t\t"\
    "{menu[1][2]:.2f} Eur\n".format(menu=menu) + "\n" + "*" * 56)
=======
# TIPP: Sie haben das Menu bereits in einer Liste. Durchlaufen Sie sie
# sequenziell und erstellen die Menueinträge mit immer dem selben Template
# Sonst müssen Sie bei hundert Einträgen jeden Eintrag extra tippen.
print("*" * 24 + " Menu " + "*" * 24 + "\n\n" + "Vorspeisen:\n{menu[0][0]}\t"\
    # TIPP: Für die Menueingabe können Sie eine for Schleife pro Zeile benutzen. Stellen
    # Sie sich vor sie haben 100te Produkte und müssten alle im Template unterbringen
      "\t\t{menu[0][1]}\t\t{menu[0][2]:.2f} Eur\n{menu[1][0]}\t{menu[1][1]}\t\t"\
    # TIPP: Alignen Sie den Preis rechts. Das sieht besser aus. Sie brauchen auch eine
    # Bindestbreite für den Preis {:>7.2f}
    "{menu[1][2]:.2f} Eur\n".format(menu=menu))
print("*" * 54)
>>>>>>> 49458c719cac72a5544bef3754475d19383cbc38
