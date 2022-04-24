# iterables are list,tuple and dictionaries
# iterator calls iter and next

dd = ('car', 'bike', 'scooter', 'jeep')
myIt = iter(dd)
print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))


class Numbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myClass = Numbers()
myItt = iter(myClass)
print(next(myItt))
print(next(myItt))
print(next(myItt))
