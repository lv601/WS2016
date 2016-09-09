# Angabe nicht gefunden...

def get_segments(sequence, window_size):
    # Possible number of seqs are string length - window size + 1
    for i in range(0, len(sequence) - window_size + 1):
        # " " * i - create a nice indent for each line
        print(" " * i, sequence[i:i + window_size], sep="")

get_segments("ATGCTTGGACCACCACCTTGTGACA", 4)