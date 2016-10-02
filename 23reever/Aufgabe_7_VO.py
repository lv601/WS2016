# Erstellen Sie ien Menukarte mit Hilfe des Formatsrtings:
#*********************************Menu******************************
# Vorspeise:
# Suppe         Tagessuppe von vorgestern               2.30    Euro
# Suppe deluxe  Für die große Geldbörse             1,300.50    Euro

# ********************************************************************

def Speisekarte(menulist):
    lines = ("Menu".center(66, "*"))
    # print(firstline)
    lines += ("\nVorspeisen:\n")  # .ljust(1))
    # print(secondline)
    lines += "{speisen[0]:<14} {speisen[1]:<44} {speisen[2]:<1,.2f} €\n".format(speisen=menu)
    # print(thirdline)
    lines += "{speisen[3]:<14} {speisen[4]:<40} {speisen[5]:<8,.2f} €\n".format(speisen=menu)
    # print(fourthline)
    lines += "*".center(66, "*")
    # print(lastline)
    print(lines)

menu = ["Suppe", "Tagessuppe von vorvorgestern", 2.3, "Suppe deluxe", "Für die große Geldbörse", 1300.5]

Speisekarte(menu)

# firstline = ("Menu".center(100, "*"))
# print(firstline)
# print("Vorspeise:".ljust(100))
# print("Suppe".ljust(16), "Tagessuppe von vorgester\t2.30 Euro".ljust(100))
# print("Suppe deluxe\t Für die große Geldbörse\t1,300.50 Euro".ljust(100))
# print("*".center(100, "*"))

# menu = ["Suppe", "Tagessuppe von vorvorgestern", 2.3, "Suppe deluxe", "Für die große Geldbörse", 1300.5]
#
# firstline = ("Menu".center(66, "*"))
# print(firstline)
#
# secondline = ("Vorspeisen:".ljust(70))
# print(secondline)
#
#
# thirdline = "{speisen[0]:<14} {speisen[1]:<44} {speisen[2]:<1,.2f} €".format(speisen=menu)
# print(thirdline)
#
# #print(thirdline[0], thirdline[1])
# #thirdline = "{speisen[0]:<14}".format(speisen=menu), "{speisen[1]:<40}".format(speisen=menu)
# # print("{speisen[0]:<14}".format(speisen=menu), "{speisen[1]:<40}".format(speisen=menu))
# # test = "{speisen[0]:<14}".format(speisen=menu), "{speisen[1]:<40}".format(speisen=menu)
# # print(test[0], test[1])
#
# fourthline = "{speisen[3]:<14} {speisen[4]:<40} {speisen[5]:<8,.2f} €".format(speisen=menu)
# #print(fourthline)
#
# lastline = "*".center(66, "*")
# print(lastline)

# Speisekarte = [firstline, secondline]
# print(Speisekarte[0], Speisekarte[1])

# menu = ["Suppe", "Tagessuppe von vorvorgestern", 2.3, "Suppe deluxe", "Für die große Geldbörse", 1300.5]
#
# lines = ("Menu".center(66, "*"))
# #print(firstline)
# lines += ("\nVorspeisen:\n")#.ljust(1))
# #print(secondline)
# lines += "{speisen[0]:<14} {speisen[1]:<44} {speisen[2]:<1,.2f} €\n".format(speisen=menu)
# #print(thirdline)
# lines += "{speisen[3]:<14} {speisen[4]:<40} {speisen[5]:<8,.2f} €\n".format(speisen=menu)
# #print(fourthline)
# lines += "*".center(66, "*")
# #print(lastline)
#
# print(lines)

