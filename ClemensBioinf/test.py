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
#print(a[1])
for item in a:
    print(item)
