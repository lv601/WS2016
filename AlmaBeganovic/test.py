menu = [("Suppe", "Tagessuppe von vorgestern", 2.3), "Suppe delux", "Fuer die grosse Geldboerse", 1300.5]

string = 30 * "*" + " Menu " + 30 * "*" + "\nVorspeisen:\n"

string += ("-{speisen[0][0]:<30}\n").format(speisen=menu)
string += ("-{speisen[0][1]:<30}").format(speisen=menu)
string += ("{speisen[0][2]:>30}\n").format(speisen=menu)
#string += ("-{speisen[0][4]:<30}\n").format(speisen=menu)
#string += ("-{speisen[0][5]:<30}\n").format(speisen=menu)


string += "\n" + 66 * "*" + "\n"


print (string)




