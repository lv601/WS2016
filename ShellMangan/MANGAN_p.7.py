#Aufgabe 7
menu=[("Suppe","Tagessuppe von vorvorgestern", "2.30"), ("Suppe deluxe", "Für die große Geldbörse", "1300.50")]
#header
string=27*"*"+"Menu"+29*"*"+"\nVorspeisen:\n"
#first
string+=("{speisen[0][0]:<15}{speisen[0][1]:^30}{speisen[0][2]:>10} €\n").format(speisen=menu)
#second
string+=("{speisen[1][0]:<15}{speisen[1][1]:^30}{speisen[1][2]:>10} €\n").format(speisen=menu)
#footer
string+= "\n"+60*"*"+"\n"

print(string)

