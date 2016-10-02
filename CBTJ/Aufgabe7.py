#Erstellen Sie eine Menukarte mit Hilfe des Formatstrings

speisekarte = "Menu"
print (speisekarte.center (60, "*"))

print ('{:<20}' .format('Vorspeise:'))
# TIPP: Ich würde den Preis nicht als String speichern "€2,50" sondern als simple Zahl 2.5
# und die Formatierung dem Formatstring überlassen. "{:>20.2} €".format(2.5). Der Vorteil
# dabei ist, dass Sie mit dem Preis dann auch noch rechnen können. Z.B. die Mehrwertsteuer
# herausrechnen.
print ('{:<20}' '{:<20}' '{:>20}'.format('Suppe','Fischsuppe', '€2,50'))
print ('{:<20}' '{:<20}' '{:>20}'.format('Suppe de luxe','Meeresfrüchte satt', '€9,50'))

Ende = ""
print (Ende.center (60, "*"))