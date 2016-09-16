### Aufgabe 7: Menükarten erstellung mit Hilfe des Formatstrings

#************* Menü ********************
#Vorspeisen:
#Suppe               Tagessuppe von vorvorgestern        2.30 €
#Suppe deluxe        Für die große Geldbörse             1.300,50 €
#************************************


print(("Menü").center(50, '*'))
print("Vorspeisen:")
print()
print(("Suppe").format(align="<"), ("Tagessuppe von vorvorgestern").format(align="^"), ("{euro}.{cent} €").format(euro="2",cent="30", align=">"))
print(("Suppe deluxe\tFür die große Geldbörse\t{tausend}.{hundert},{cent} €").format(tausend="1", hundert="300", cent="50"))
print(("").center(50, '*'))
