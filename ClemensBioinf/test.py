def generator_func(n):
    i = 1
    while i < n:
        yield i ** 2 # Creates generator
        i += 1
for result in generator_func(10):
    print(result)