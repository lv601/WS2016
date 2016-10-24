s1 = " Menu "
s2 = "Vorspeisen:"
s3 = "Suppe"
s4 = "Tagessuppe von vorgestern"
s5 = "Suppe deluxe"
s6 = "Für die große Geldbörse"

print(s1.center(100, "*"))
print(s2)
print(s3,"\t\t\t\t\t\t\t\t",s4,"\t\t\t\t\t\t\t\t","{e}.{c} €".format(e=2, c=30))
print(s5,"\t\t\t\t\t\t",s6,"\t\t\t\t\t\t"," ","{:>10,.2f} €".format(1300.5),"\n")
print("*".center(100, "*"))