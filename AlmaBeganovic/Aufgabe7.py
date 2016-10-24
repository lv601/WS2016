menu = [("Suppe", "Tagessuppe von vorgestern", 2.300), "Suppe delux", "Fuer die grosse Geldboerse", 1300.5]

string = 45 * "*" + " Menu " + 45 * "*" + "\nVorspeisen:\n"

string += ("-{speisen[0][0]:<30}").format(speisen=menu)
string += ("{speisen[0][1]:<30}").format(speisen=menu)
string += ("{speisen[0][2]:>30} Eur\n").format(speisen=menu)
string += ("-{speisen[1]:<30}").format(speisen=menu)
string += ("{speisen[2]:<30}").format(speisen=menu)
string += ("{speisen[3]:>30} Eur").format(speisen=menu)

string += "\n" + 96 * "*" + "\n"

print (string)
