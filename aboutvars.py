# Variables can be a single letter
# Or Variables can be a meaningful word like age
# Variables starts with _ or letter (letter & number) but not with a number or space in between

x = 1  # int
y = "String"  # or put in single quotes

# Type casting
a = str(x)
b = float(x)

print(a, b)

# verify type
print(type(a))  # output <class 'str'>
print(type(b))  # output <class 'float'>

# case sensitive variables
c = 2
C = 4
print(c)  # output 2
print(C)  # output 4

# Override values
p = 2
p = "John"

print(p)  # Expected John

# Valid ways to declare and define variable or in single lines

t, u, v = 1, 2, 3
print(t, u, v)

# Assign same value to a variable
xx = yy = zz = "apples"  # Print x y z will have same value apples
