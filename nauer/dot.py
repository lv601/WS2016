# Create simple dot plot
def dot_plot(seq1, seq2):
    for c1 in seq1:
        print(c1, end="|")
        for c2 in seq2:
            if c2 == c1:
                print("*", end="|")
            else:
                print(" ", end="|")
        print()
    print("  " + "|".join([c for c in seq2]))

dot_plot("ABCDEFGHIKLMO", "CBAABCFHJKLNOEDC")