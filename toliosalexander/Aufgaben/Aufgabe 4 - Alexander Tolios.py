### Aufgabe 4 - Alexander Tolios - last modified 06.09.2016 ; siehe Mitschrift vom 05.09.2016 ###


var1 = 1
var2 = 2
var3 = 4
var4 = 8
var5 = 16
var6 = 32
var7 = 64
var8 = 128

flags = var1 | var3 | var8 | var5 # -> verknüpfen, daher mit oder (|)

print(flags)


for i in range(8):
    if flags & 2**i: # -> prüfen, daher mit und (&)
        print("Flag ", 2**i, " was set.")

flags & var1 # 1, weil gesetzt
flags & var2 # 0, weil nicht gesetzt
flags & 0b100 # 4, weil gesetzt

# beim Kombinieren/verknüpfen verwendet man das oder (|)
# beim Prüfen verwendet man das und (&)
