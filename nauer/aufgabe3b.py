# Ask for input
string = input("Geben Sie einen Text ein: ")

# Set window size
ws = 3

# Possible number of sequences are string length - window size + 1
for i in range(0, len(string) - ws + 1):
    # " " * i - create a nice indent for each line
    print(" " * i, string[i:i + ws], sep="")
