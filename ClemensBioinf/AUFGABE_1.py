### Was passiert wenn sie mit Strings rechnen? ###
# Grundsaetzlich nicht moeglich. Eine Ausnahme stellen Addition und Multiplikation dar.
# Bei der Multiplikation wird die Symbolkette an sich selbst so oft angehaengt wie es
# der Faktor angibt.
#zB
print("string" * 3)
#  Bei der Addition werden die Symbolketten an einander gehaengt.
# zB
print("string1" + "string2")


### Multiplizieren Sie einen String mit einer Zahl ###
print("string" * 3) # siehe Frage 1


### Addieren Sie Strings ###
print("string1" + "string2") # siehe Frage 1


### Subtrahieren Sie Strings ###
try:
    print("string1" - "string2") # siehe Frage 1
except TypeError:
    print("TypeError: Subtraktion von Strings nicht moeglich")


### Was ergibt eine Division von einer Ganzzahl (integer) durch eine Gleitkommazahl (float)? ###
# Eine Gleitkommazahl. siehe
print(type(10 / 2.5))
