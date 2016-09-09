def get_segments(sequence, window_size):
    for i in range(0, len(sequence)-window_size+1):
        print(" "*i, sequence[i:i+window_size], sep="")
get_segments("ATGCTTGGACCACCACCTTGTGACA",3)
