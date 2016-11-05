### Aufgabe 7 - Alexander Tolios - last modified am 29.10.2016 ###

# Speisekarte erstellen nach folgender Formatvorlage: 

# *************************** Menu ***************************
# Vorspeisen:
# Suppe          Tagessuppe von vorvorgestern        2.30 €
# Suppe deluxe   Für die große Geldbörse         1,300.50 €
# ************************************************************



menu = [("Suppe", "Tagessuppe von anno dazuma(h)l", 2.3),
("Suppe deluxe", "Für die sehr große Geldbörse", 1300.5)]

# Menu header
string = 23 * "*" + " Suppenbuffet " + 23 * "*" + "\n" +  4 * " " + "Vorspeisen:\n"
# First entry
string += (2 * " " + "{speisen[0][0]:<15}{speisen[0][1]:<30}"
   "{speisen[0][2]:>10,.2f} €\n").format(speisen=menu)
# Second entry
string += (2 * " " + "{speisen[1][0]:<15}{speisen[1][1]:<30}"
  "{speisen[1][2]:>10,.2f} €\n").format(speisen=menu)
# Menu footer
string += "\n" + 60 * "*" + "\n"

print(string)
