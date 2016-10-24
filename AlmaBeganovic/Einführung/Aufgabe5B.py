# coding=utf-8
from random import randint

# Nein, Sie sollten das ganze Spiel in eine Funnktion einbetten. Nur randint
# einzubetten ist das gleiche wenn Sie gleich randint ausführen
# Sie können 'bereich' und 'versuche' als parameter verwenden
def run_game(bereich):
    zufazahl = randint(1, bereich)
    #return zufazahl

    # Von @auer eingerückt
    bereich = input ("Definieren Sie den Bereich für die Zufallszahl zwischen 1 und n ein: ")

    versuche = input ("Bitte geben Sie Anzahl von Versuchen ein: ")

    print ("Bereich ist zwischen 1 und ", bereich)
    print ("Anzahl von Versuchen ist ", versuche)

    #zufal_global = run_game(bereich)
    #print (zufal_global)

    # TIPP: Das selbe bekommen Sie auch so
    # for i in range (versuche):
    for i in range (1, versuche+1):
        zahl = input("Bitte geben Sie eine Zahl aus dem Bereich: ")
        # Achtung: Sie vergleichen hier int mit str Zahl 5 != '5'
        if zahl == zufal_global:
            print ("Zahl ist erraten", zufal_global)
            # TIPP: Hier können Sie gleich auch die Funktion verlassen anstratt
            # nur die Schleife und gleich noch dazu einen Rückgabewert, wie die
            # erratene Zahl oder None, wenn Sie nicht erraten wurde
            # return zahl
            break;

        if zahl < zufal_global:
            print ("Zahl ist kleiner als Zufallszahl")

        if zahl > zufal_global:
            print ("Zahl ist grosser als Zufallszahl")

    # TIPP: Sie können wenn die Schleife komplett durchlaufen ist und das Spiel
    # verloren ist, noch eine 'else' Zweig noch einbauen, der nur dann
    # ausgeführt wird. So können Sie z.B. noch eine GAME OVER Message ausgeben
