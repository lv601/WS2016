### Aufgabe 5c - Alexander Tolios - last modified am 06.09.2016 ; siehe Mitschrift vom 29.08.2016 ###

### Kopie von Aufgabe 3b - Alexander Tolios - last modified 06.09.2016 ; siehe Mitschrift vom 29.08.2016 ###

text = input("Bitte Sequenz eingeben: ")

fenster = input("Bitte Fenstergröße eingeben: ")
fenster = int(fenster)
position = 0

for position in range(0, len(text) - fenster + 1):
    print("_" * position, text[position:position + fenster], sep="")
    position += 1




### ab hier neuer Code ###


def sequenz(text, fenster):
    for position in range(0, len(text) - fenster + 1):
        print("_" * position, text[position:position + fenster], sep="")
        position += 1

sequenz("1234567890", 3)

