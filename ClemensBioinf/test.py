class A:
    def __init__(self):
        self.data = {1:2, 3:4}
    def __repr__(self):
        return "A()"
    def __str__(self):
        return "Ich bin vom Typ A"
    def __bytes__(self):
        return b"Ich bin vom Typ A"
    def __len__(self):
        return len(self.data)
    def __getitem__(self, item):
        return self.data[item]
    def __iter__(self):
        for item in self.data:
            print(self.data[item])

a = A()
print(str(a))
print(repr(a))
print(hash(a))
print(a)
print(len(a))
print(a[1])
for element in a:
    print(element)
