## Date: 04.09.2016
## Author: Anna Majewski
## Description: Input von String, der dann Substrings ausgibt.

eingabe = input("Geben Sie eine DNA-Sequenz ein:")
# Eingabe in Variable eingabe gespeichert.
length = 3
# Länge des Substrings
strlen = len(eingabe)
# Länge des eingegebenen Strings

for index, char in enumerate(eingabe):
    print(" "*index, eingabe[index:index+length])
    # damit es jeweils einrückt um ein " " pro Zeile
    if strlen-index <= length:
        break
    # da sonst die Länge des Substrings nicht eingehalten wird
    # Sprich: Die Substrings sind kürzer als 3.
