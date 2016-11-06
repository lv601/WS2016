#!/usr/bin/env python3    # shebang needed in executeable files. chmod 755


### Aufgabe 7: Menükarten erstellung mit Hilfe des Formatstrings

#************* Menü ********************
#Vorspeisen:
#Suppe               Tagessuppe von vorvorgestern        2.30 €
#Suppe deluxe        Für die große Geldbörse             1.300,50 €
#************************************

#erste Lösung#

print((" Menü ").center(124, '*'))
print("Vorspeisen:\n".ljust(100))
#print(("Suppe").format(align="<"), ("Tagessuppe von vorvorgestern").format(align="^"), ("{euro}.{cent} €").format(euro="2",cent="30", align=">"))
print(("Suppe").ljust(50), ("Tagessuppe von vorvorgestern").ljust(50), ("{euro}.{cent} €").format(euro="2",cent="30").rjust(20))

#print(("Suppe deluxe\tFür die große Geldbörse\t{tausend}.{hundert},{cent} €").format(tausend="1", hundert="300", cent="50"))
print(("Suppe deluxe").ljust(50), ("Für die große Geldbörse").ljust(50), ("{tausend},{hundert},{cent} €").format(tausend="1", hundert="300", cent="50").rjust(20))
print(("").center(124, '*'))

#print("\n")


for i in range (30):
	print(("x"*i).center(50))
print(("I I").center(50))









