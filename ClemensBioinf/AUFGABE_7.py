menu = [["Suppe", "Suppe von vorgestern", 2.30],["Suppe deluxe", "für die große Geldbörse", 1300.5]]
print("*" * 24 + " Menu " + "*" * 24 + "\n\n" + "Vorspeisen:\n{menu[0][0]}\t"\
      "\t\t{menu[0][1]}\t\t{menu[0][2]:.2f} Eur\n{menu[1][0]}\t{menu[1][1]}\t\t"\
    "{menu[1][2]:.2f} Eur\n".format(menu=menu))
print("*" * 54)


