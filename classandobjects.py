# A class cannot be empty use pass in the block
# init is like a constructor
# self is treated as this for current instance
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def message(self):
        print("My name is " + str(self.name) + " age " + str(self.age))


# Creating and passing value to params and calling methods
h1 = Human("Mohan", 60)

print(h1.name)
print(h1.age)

h1.message()

# delete an object
del h1
h1.name = "Sohan"
h1.age = 22
h1.message()
