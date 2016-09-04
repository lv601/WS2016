## Date: 04.09.2016
## Author: Anna Majewski
## Description: Eine Funktion um die in Aufgabe 3b erstellte Schleife legen.

## Zuerst Code von Aufgabe 3b kopieren, da sie ausführbar bleiben soll.

def substring_gen(sublen, string = ""):
    # sublen ist die Länge in die der String zerlegt werden soll.
    # string ist nicht von vornherein erforderlich,
    # a) sollte er nicht eingegeben werden, wird er durch input erfragt.
    # b) wird er angegeben, wird er sofort zerlegt
    if string == "":
        eingabe = input("Geben Sie eine DNA-Sequenz ein:")
        # Eingabe in Variable eingabe gespeichert.
    else:
        eingabe = string
    length = sublen
    # Länge des Substrings
    strlen = len(eingabe)
    # Länge des eingegebenen Strings

    for index, char in enumerate(eingabe):
        print(" "*index, eingabe[index:index+length])
        # damit es jeweils einrückt um ein " " pro Zeile
        if strlen-index <= length:
            break

##substring_gen(4,"CGCGTGATGACGATCGACGAT")
# Mit Eingabe eines Strings wird dieser in die Substrinlänge zerlegt.

##substring_gen(4,)
# Ohne Eingabe eines Strings, wird zuerst mit input danach gefragt.
