menu = [{"billig":
             {"name": "Suppe", "desc": "Tagessuppe von vorvorgestern", "preis": 2.30}
         },
        {"teuer":
             {"name": "Suppe deluxe", "desc": "Für die gestopfte Börse", "preis": 1300.50}
         }]

speisekarte = ["Menu", "Vorspeisen"]

string = speisekarte[0].center(90, "*")
string += "\n"
string += speisekarte[1]
string += "\n"
string += "{:<30}".format(menu[0]["billig"]["name"])+\
          "{:<30}".format(menu[0]["billig"]["desc"])+\
          "{:>30}".format(menu[0]["billig"]["preis"])
string = "{:*^90}".format(speisekarte[0])
string += "\n\n"
string += "{:<90}".format(speisekarte[1])
string += "\n"
string += "{:<30}".format(menu[0]["billig"]["name"])+\
          "{:<30}".format(menu[0]["billig"]["desc"])+\
          "{:>28} �".format(menu[0]["billig"]["preis"])
string += "\n"
string += "{:<30}".format(menu[1]["teuer"]["name"])+\
          "{:<30}".format(menu[1]["teuer"]["desc"])+\
          "{:>28} �".format(menu[1]["teuer"]["preis"])
string += "\n\n"
string += "{:*^90}".format("")

print(string)