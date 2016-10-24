class A:
    def __repr__(self):
        return "A()"
    def __str__(self):
        return "Ich bin vom Typ A"
    def __bytes__(self):
        return b"Ich bin vom Typ A"
a = A()
str(a)
repr(a)
print(hash(a))
print(a)