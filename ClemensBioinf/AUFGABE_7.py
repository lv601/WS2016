menu = [["Suppe", "Suppe von vorgestern", 2.30],["Suppe deluxe", "für die große Geldbörse", 1300.5]]

print("*" * 32 + " Menu " + "*" * 32 + "\n\nVorspeisen:")
for dish in menu:
    print('{:<12}\t\t\t{:>12}\t\t{:>12.2f} Eur'.format(dish[0], dish[1], dish[2]))
print("\n" + "*" * 70)
