## Date: 05.09.2016
## Author: Anna Majewski
## Description: Bitweise Opertoren und ihre Anwendung
## Ich habe 2 Funktionen geschrieben, weil ich nicht nur abfragen wollte, welche Flags gesetzt sind,
## sondern auch selbst welche setzen wollte.
## Mit set() kann man jetzt Flags aufaddieren und mit isset() anzeigen welche Flags gesetzt sind.

# gesetzte Flags kombinieren: flag1 | flag3

def isset(flag):
    """Checks which flag is set, prints set flags"""
    for i in range(8):
        # jede Iteration den Wert um 1 verschieben
        if flag &2**(i):
            print("Flag", i, "was set.")

def set(*settings):
    """Setting flags and returning the total"""
## Der User sagt mir welche Flags er setzen möchte,
## ich returne ihm welche Summe daraus gebildet wird.

    # TIPP: Verwenden Sie für Konstanten wie diese uppercase Notation FLAG1, FLAG2, ...
    # Sehen sie z.B. das Modul re
    # import re
    # re.IGNORECASE
    flag1 = 2
    flag2 = 4
    flag3 = 8
    flag4 = 16
    flag5 = 32
    flag6 = 64
    flag7 = 128
    flag8 = 256
    add = 0
## Ich gebe jedem Flag einen Wert vor.

    flaglist = [flag1, flag2, flag3, flag4, flag5, flag6, flag7, flag8]
## Liste mit den flags, damit die Variablen verwendet werden können
    for x in settings:
        x = flaglist[x-1]
## x wird dann mit der Eingabe einer Zahl eine Variable zugewiesen
        add += x
## die Werte werden addiert, damit man intern damit dann arbeiten kann.
    return "The code for the chosen flags is", add

## Wert wird zurückgegeben, damit der User weiß, welche Zahl dabei herauskommt.
## Dieser Wert kann mit isset() überprüft werden.
print(set(1, 2, 3))
isset(14)
