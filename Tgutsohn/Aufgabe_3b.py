str = input("Geben Sie einen Text ein: ")

ws = 3

for i in range(0, len(str) - ws +1):
    print(" " * i, str[i:i+ws], sep=" ")