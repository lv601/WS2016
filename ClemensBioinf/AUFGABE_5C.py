def string_parts(start, end, step):
    id = input("Enter a string: ")
    for char in id:
        print(id[start:end])
        start += step
        end += step

string_parts(0, 3, 3)
