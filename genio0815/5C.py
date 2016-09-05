def get_segments(sequence, size):
    for i in range(0, len(sequence) - size + 1):
        print(" " * i, sequence[i:i + size], sep="")

get_segments("ATGCTTGGACCACCACCTTGTGACA", 3)