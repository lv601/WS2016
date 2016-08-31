print("Enter a string: ", end = "")
str = input()

start = 0
end = 3
step = 1
for codon in range(0, len(str)):
    while len(str[start:end]) == 3:
        print(str[start:end])
        start += step
        end += step