def string_parts(start, end, step):
    print("Enter a string: ", end="")
    str = input()
    diff = end - start
    #print(len(str[start:end]))
    for codon in range(0, len(str)):
        while len(str[start:end]) == diff:
            print(str[start:end])
            start += step
            end += step

string_parts(0, 3, 3)