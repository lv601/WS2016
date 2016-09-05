# User nach Input fragen
string = input("Geben Sie einen Text ein: ")

# Länge Substring
ss = 3

# Mögliche Anzahl von Sequenzen: Stringlänge - Substring + 1
for i in range(0, len(string) - ss + 1):
    # " " * i - create a nice indent for each line
    print(" " * i, string[i:i + ss], sep="")