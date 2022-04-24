# Map function maps a function with respect to the iterable

def square(x):
    return x * x


getsquares = [1, 2, 3, 4, 5]
squared = map(square, getsquares)  # getsquares is iterable here
print(list(squared))
