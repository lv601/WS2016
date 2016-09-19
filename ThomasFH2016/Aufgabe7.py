# Variable Menükarte / Unterpunkte können ausgelassen werden
# Es fehlt das RightAlignment nach den Menüeinträgen

# ************************* Menu ******************************
# Vorspeisen:
# Suppe             Tagessuppe von vorvorgestern      2.30 €
# Suppe deluxe      Für die große Geldbörse       1,300.50 €
# *************************************************************


class Menu:

    def __init__(self):
        self.FirstMenu = True
        self.lVorspeisen = []
        self.lHauptspeisen = []
        self.lNachspeisen = []
        self.lCategories = [' Vorspeisen ', ' Hauptspeise ', ' Nachspeisen ']
        self.strEmptyLine = u'\u2551' + str(" ") * 73 + u'\u2551'
        self.strMenuSeparator = u'\u255F' + str(u'\u2500') * 73 + u'\u2562'
        self.strVorspeise = self.strEmptyLine + "\n"
        self.strHauptspeise = self.strEmptyLine + "\n"
        self.strNachspeise = self.strEmptyLine + "\n"
        self.strVorspeise += u'\u2551' + str(u'\u2550' + self.lCategories[0] + u'\u2550').center(73) + u'\u2551' + "\n"
        self.strHauptspeise += u'\u2551' + str(u'\u2550' + self.lCategories[1] + u'\u2550').center(73) + u'\u2551' + "\n"
        self.strNachspeise += u'\u2551' + str(u'\u2550' + self.lCategories[2] + u'\u2550').center(73) + u'\u2551' + "\n"
        self.strVorspeise += self.strMenuSeparator + "\n"
        self.strHauptspeise += self.strMenuSeparator + "\n"
        self.strNachspeise += self.strMenuSeparator + "\n"

    def add_vorspeise(self, menu_name, menu_description, price):
        self.lVorspeisen.append([menu_name, menu_description, price])
        return self.lVorspeisen[-1]

    def add_hauptspeise(self, menu_name, menu_description, price):
        self.lHauptspeisen.append([menu_name, menu_description, price])
        return self.lHauptspeisen[-1]

    def add_nachspeise(self, menu_name, menu_description, price):
        self.lNachspeisen.append([menu_name, menu_description, price])
        return self.lNachspeisen[-1]


    def Write_Header(self):
        tmpStr = u'\u2554' + u'\u2550' * 73 + u'\u2557' + "\n"
        tmpStr += u'\u2551' + "Menu".center(73) + u'\u2551' + "\n"
        tmpStr += u'\u2560' + u'\u2550' * 73 + u'\u2563' + "\n"
        return tmpStr

    def Write_Vorspeisen(self):
        if len(self.lVorspeisen) == 0:
            return ""
        else:
            if self.FirstMenu == True:
                sVorspeisen = self.strMenuSeparator + "\n"
                self.FirstMenu == False
        sVorspeisen = self.strVorspeise
        for entry in self.lVorspeisen:
            sVorspeisen += u'\u2551' + ("  \u257A {vorspeisen[0]:<15}{vorspeisen[1]:<30}"
                           "{vorspeisen[2]:>10,.2f} €" + " "*12  + "\u2551\n").format(vorspeisen=entry)
        return sVorspeisen

    def Write_Hauptspeisen(self):
        sHauptspeisen = ""
        if len(self.lHauptspeisen) == 0:
            return ""
        else:
            if self.FirstMenu == True:
                sHauptspeisen += self.strMenuSeparator + "\n"
                self.FirstMenu == False
        sHauptspeisen += self.strHauptspeise
        for entry in self.lHauptspeisen:
            sHauptspeisen += u'\u2551' + ("  \u257A {hauptspeisen[0]:<15}{hauptspeisen[1]:<30}"
                           "{hauptspeisen[2]:>10,.2f} €" + " "*12  + "\u2551\n").format(hauptspeisen=entry)
        return sHauptspeisen

    def Write_Nachspeisen(self):
        sNachspeisen = ""
        if len(self.lNachspeisen) == 0:
            return ""
        else:
            if self.FirstMenu == True:
                sNachspeisen += self.strMenuSeparator + "\n"
                self.FirstMenu == False
        sNachspeisen += self.strNachspeise
        for entry in self.lNachspeisen:
            sNachspeisen += u'\u2551' + ("  \u257A {nachspeisen[0]:<15}{nachspeisen[1]:<30}"
                           "{nachspeisen[2]:>10,.2f} €" + " "*12  + "\u2551\n").format(nachspeisen=entry)
        return sNachspeisen

    def Write_Footer(self):
        return u'\u255A' + u'\u2550' * 73 + u'\u255D' + "\n"

    def Write_Menu(self):
        sMenu = self.Write_Header()
        sMenu += self.Write_Vorspeisen()
        sMenu += self.Write_Hauptspeisen()
        sMenu += self.Write_Nachspeisen()
        sMenu += self.Write_Footer()
        return sMenu


new_menu = Menu()

new_menu.add_vorspeise("Suppe", "Tagessuppe von vorvorgestern", 2.3)
new_menu.add_vorspeise("Suppe deluxe", "Für die große Geldbörse", 1300.5)

new_menu.add_hauptspeise("Ein Salat", "Grün, Knackig, Langweilig", 10.5)

new_menu.add_nachspeise("Erdbeereis", "Süß und gut", 22.50)
new_menu.add_nachspeise("Schoko", "Braucht keine Beschreibung", 8.80)

print(new_menu.Write_Menu())