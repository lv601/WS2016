###Julie Krainer###

### Aufgabe 7: Menükarten erstellung mit Hilfe des Formatstrings

#************* Menü ********************
#Vorspeisen:
#Suppe               Tagessuppe von vorvorgestern        2.30 €
#Suppe deluxe        Für die große Geldbörse             1.300,50 €
#************************************

#erste Lösung#

print((" Menü ").center(100, '*'))
print("Vorspeisen:\n".ljust(100))
print(("Suppe").format(align="<"), ("Tagessuppe von vorvorgestern").format(align="^"), ("{euro}.{cent} €").format(euro="2",cent="30", align=">"))
print(("Suppe deluxe\tFür die große Geldbörse\t{tausend}.{hundert},{cent} €").format(tausend="1", hundert="300", cent="50"))
print(("").center(100, '*'))

print("\n")

#Schönere Lösung#

print((" Menü ").center(123, '*'))
print("Vorspeisen:\n".ljust(120))
# TIPP: anstatt Zahlen aufzusplitten können Sie mit
# "{:,.2f}".format(1500.50) ebenfalls das Tausender-
# trennzeichen ausgeben. Leider habe ich so keine
# Möglichkeit für float Zeichen gefunden, die die
# deutsche Notation verwendet. Sie können aber die
# die Zahl vorher mit locale Modul formatieren.
#
# import locale
# locale.setlocale(locale.LC_NUMERIC, 'de_DE.utf8')
# "{:,.2f}".format(1500.50)
#
# Verfügbare locals auf ihrem Computer bekommen Sie
# mit 'locale -a'
print(("Suppe deluxe").ljust(50), ("Für die große Geldbörse").ljust(50), ("{tausend}.{hundert},{cent} €").format(tausend="1", hundert="300", cent="50").rjust(20))
print(("Suppe").ljust(50), ("Tagessuppe von vorvorgestern").ljust(50), ("{euro}.{cent} €").format(euro="2",cent="30").rjust(20))
print(("").center(123, '*'))

print("\n")

#Oh Tannenbaum#

# Sehr hübsch jetzt fehlen nur noch die Kerzen "\U0001F56F"
# am Rand und ein paar Christbaumkugeln ...
for i in (range(1,22,2)):
    if i == 1:
        print(("x").center(30))
        i+=1
    elif i < 20:
        print(("#"*i).center(30))
        i+=1
    else:
        print(("H").center(30))

