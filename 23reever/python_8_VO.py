# # Normale Funktion
# def no_generator_func(n):
#     i = 1
#     result = []
#     while i < n:
#         result.append(i ** 2) # ** = hoch
#         i += 1
#     return result
#
# sequence = no_generator_func(10)
#
# for item in sequence:
#     print(item)

# def generator_func(n):
#     i = 1
#     while i < n:
#         yield i ** 2 # Creates generator
#         yield i / 2
#         yield i * 2
#         i += 1
#
# # gen is iterable generator object
# gen = generator_func(10)
#
# print(next(gen)) # 1st result
# print(next(gen)) # next result
# print(next(gen)) # and so on

# class A:
#     pass
# a = A()
# print(str(a))
# print(repr(a))
# # bytes(a) # TypeError: A Object is not iterable
# print(a)

# class A:
#     def __repr__(self):
#         return "A()"
#     def __str__(self):
#         return "Ich bin vom Typ A"
#     def __bytes__(self):
#         return b"Ich bin vom Typ A"
# a = A()
# print(str(a))
# print(repr(a))
# print(bytes(a))
# print(a)

# class A:
#     def __init__(self, x, y):
#         self.X = x
#         self.Y = y
#     def __add__(self, other):
#         if isinstance(other, A):
#             return A(self.X + other.X, self.Y + other.Y)
#         elif isinstance(other, (int, float)):
#             return A(self.X + other, self.Y + other)
#         else:
#             # Important for calling __radd__ in other class
#             return NotImplemented
#     # def __radd__(self, other): # call __add__ ­ same code
#     #     return self.__add__(other)
#
# a = A(x=5, y=2)
# print((a + 1).X)
# print((1 + a).X)

#
# class A:
#     def __init__(self, x, y):
#         self.X = x
#         self.Y = y
#     def __iadd__(self, other):
#         if isinstance(other, A):
#             self.X += other.X
#             self.Y += other.Y
#             return self
#         elif isinstance(other, (int, float)):
#             self.X += other
#             self.Y += other
#             return self
#         else:
#             return NotImplemented
#
# a = A(x=5, y=2)
# a += 4
# print(a.X,a.Y)

class A:
    def __init__(self, *args):
        self.data = args
    def __getitem__(self, key):
        return self.data[key]
    def __setitem__(self, key, value):
        self.data[key] = value
    def __iter__(self):
        for item in self.data:
            yield item

a = A("Hello", "World", "!")
print(a[1]) #getitem

a[2] = 5

for item in a:
    print(item)




































