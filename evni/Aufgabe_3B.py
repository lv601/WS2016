sequenz = input('Geben sie die Sequenz ein: ')
#print (sequenz)
drei = 3
for i in range(0, len(sequenz) - drei+1):
    print(' '*i, sequenz[i:i+drei])
