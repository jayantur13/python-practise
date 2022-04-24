# tuple uses ( ) brackets
# tuple is ordered, unchangeable and allow duplicate values
# unchangeable i.e append (add) or change
mytup = (1, 2, 3, "Mohan", True, 8.00, 3)
print(mytup)
print(len(mytup))
print(type(mytup))

# A tuple with only one value is str ex = ("car")
# To make it a tuple ex = ("car",)
ex = ("car")
print(type(ex))  # outputs "str" now try ex=("car",) will return type tuple

# Access elements
tple = ("car", 44, "bike", True)
print(tple[2])  # outputs bike
print(tple[1:3])  # outputs 44 and bike

# To edit a tuple 1) Change tuple to list 2) Change via list 3) Change back to tuple
ez = (3.4, 5, "lol", True)  # tuple
x = list(ez)  # ez converted to list
x[2] = "Ladder"  # Change index 2 from lol to Ladder
y = tuple(x)  # Back to tuple
print(y)
