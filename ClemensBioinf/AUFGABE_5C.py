def string_parts(start, end, step):
    print("Enter a string: ", end="")
    # TIPP: Sie können input direkt einen String übergeben, der angezeigt werden
    # soll
    # string = input("Enter a string: ")
    # ACHTUNG: passen sie auf das Sie keine Funktionsnamen überschreiben, wie
    # str hier. Sie wären sehr verplüfft, wenn sie später vielleicht ein int
    # Value in einen String konvertieren möchten str(10)
    # id ist hier ein gern verwendeter Variabelname
    str = input()
    diff = end - start
    #print(len(str[start:end]))
    for codon in range(0, len(str)):
        # Interessante denkweise aber würde nicht start und step reichen?        
        while len(str[start:end]) == diff:
            print(str[start:end])
            start += step
            end += step

string_parts(0, 3, 3)
