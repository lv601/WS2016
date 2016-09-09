sequenz = input("Gib eine Sequenz ein: ")
window = 3
i = 0
for i in range(0, len(sequenz)-window+1):
    print(" " * i, sequenz[i:i+window], sep="")
    i += 1