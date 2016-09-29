#Erstellen Sie eine Menukarte mit Hilfe des Formatstrings

speisekarte = "Menu"
print (speisekarte.center (60, "*"))

print ('{:<20}' .format('Vorspeise:'))
print ('{:<20}' '{:<20}' '{:>20}'.format('Suppe','Fischsuppe', '€2,50'))
print ('{:<20}' '{:<20}' '{:>20}'.format('Suppe de luxe','Meeresfrüchte satt', '€9,50'))

Ende = ""
print (Ende.center (60, "*"))