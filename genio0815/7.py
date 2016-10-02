menu = [("Suppe", "Tagessuppe von vorvorgestern", 2.3),
("Suppe deluxe", "Für die große Geldbörse", 1300.5)]

# Menu header
string = 27 * "*" + " Menu " + 27 * "*" + "\nVorspeisen:\n"
# First entry
string += ("  {speisen[0][0]:<15}{speisen[0][1]:<30}"
   "{speisen[0][2]:>10,.2f} €\n").format(speisen=menu)
# Second entry
string += ("  {speisen[1][0]:<15}{speisen[1][1]:<30}"
  "{speisen[1][2]:>10,.2f} €\n").format(speisen=menu)
# Menu footer
string += "\n" + 60 * "*" + "\n"

print(string)