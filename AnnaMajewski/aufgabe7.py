## Date: 24.09.2016
## Author: Anna Majewski
## Description: Menükarte mithilfe des Formatstrings

## Habe zuerst das Menü in eine Liste geschrieben.
## Die Elemente der Liste sind ein Dictionary.
menu = [{"billig":
             {"name": "Suppe", "desc": "Tagessuppe von vorvorgestern", "preis": 2.30}
         },
        {"teuer":
             {"name": "Suppe deluxe", "desc": "Für die große Geldbörse", "preis": 1300.50}
         }]

## Die anderen Worte wurden in einer zweiten Liste gespeichert.
speisekarte = ["Menu", "Vorspeisen"]

## Der String wird jedes Mal verlängert.
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
          "{:>28} €".format(menu[0]["billig"]["preis"])
string += "\n"
string += "{:<30}".format(menu[1]["teuer"]["name"])+\
          "{:<30}".format(menu[1]["teuer"]["desc"])+\
          "{:>28} €".format(menu[1]["teuer"]["preis"])
string += "\n\n"
string += "{:*^90}".format("")

print(string)
