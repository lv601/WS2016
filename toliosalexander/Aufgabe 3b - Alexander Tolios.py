### Aufgabe 3b - Alexander Tolios - last modified 06.09.2016 ; siehe Mitschrift vom 29.08.2016 ###

text = input("Bitte Sequenz eingeben: ")

fenster = input("Bitte Fenstergröße eingeben: ")
fenster = int(fenster)
position = 0

for position in range(0, len(text) - fenster + 1):
    print("_" * position, text[position:position + fenster], sep="")
    position += 1


### Lösung für Aufgabe 3b von nauer

# Ask for input

string = input("Geben Sie einen Text ein: ")

# Set window size
ws = 3
i = 0
# Possible number of sequences are string length - window size + 1
for i in range(0, len(string) - ws + 1):
    # " " * i - create a nice indent for each line
    print(" " * i, string[i:i + ws], sep="")
    i = i + 1
