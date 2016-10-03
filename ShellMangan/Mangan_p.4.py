#Aufgabe 4
#Erstellen Sie 8 Variablen, die je einer Bit Position von 1 bis 256 entsprechen.
#Verknüpfen Sie einige Variablen mit dem bitweisen ODER Operator.
#Erstellen Sie eine Schleife und fragen Sie die gesetzten Flags ab.

flag1=2
flag2=4
flag3=8
flag4=16
flag5=32
flag6=64
flag7=128
flag8=256

flags=flag1|flag2|flag7
print(flags)

for i in range(8):
    if flags & 2**i:
        print("Flag ", 2**i, " was set.")
for i in range(8):
    if flags & 0b1000:
        print("Yes")
        
for i in range(8):
    if flags | 0b1000:
        print("Ja")

if flags & flag1:
    print(flag1)
elif flags & flag2:
    print(flag2)
elif flags & flag3:
    print(flag3)
else:
    print("Flags doesnt include flag1, flag2 or flag3")
    
