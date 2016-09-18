## https://pyformat.info

string=("Menue,Vorspeisen:,Suppe-Tagessuppe von vorvorgestern-2.30 €,Suppe deluxe Für die große Geldboerse-1300.50 €")
s = string.split(",")

menue = (s[0])
vors = (s[1])


tages = s[2].split("-")
deluxe = s[3].split("-")

suppe = tages[0]
tages_name = tages[1]
tages_preis = tages[2]

deluxe_name = deluxe[0]
deluxe_preis = deluxe[1]

print(menue.center(40, ' '),"\n",vors.ljust(40, ' '),"\n",tages_name.ljust(40, ' '),"\n",tages_preis.ljust(40, ' '),"\n",deluxe_name.ljust(40, ' '),"\n",deluxe_preis.ljust(40, ' '))

#print(vors)
#print(suppe)
#print(tages_name)
#print(tages_preis)
#print(deluxe_name)
#print(deluxe_preis)

