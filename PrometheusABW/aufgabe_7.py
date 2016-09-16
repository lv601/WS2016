#Erstellen einer Menuekarte
#menü header
print("{:*^60}".format('Menue'))
#small menu header
print("\nVorspeisen"+" \n")
print("{:*^60}".format('Vorspeisen'))
print("{:<20}".format('Suppen')+"{:^20}".format('Suppe von vorgestern')+
      "{:>19,.2f}".format(2.3)+"€")
print("{:<20}".format('Suppen deluxe')+"{:^20}".format('Suppe Deluxe')+
      "{:>19,.2f}".format(1300,5)+"€")
#menü footnote
print("\n{:*^60}".format('*'))