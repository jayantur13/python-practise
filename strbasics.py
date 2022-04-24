# a = 'apple' or a = "apple" both valid

# you can use double quotes in the same as below
a = '''Multiline 
value
for
variable 
a
'''

print(a)

# String in python is an array
x = "Hello World"

print("First character is " + x[0])  # prints H for index 0
print(len(x))  # length with space
print("d" in x)  # Check if x has d returns True/False
print(x[:5])  # Slice a string => hello or x[2:5]
print(x[2:5])  # Start from 2 to 5
print(x[2:])  # Start from 2 to end
print(x[-5:-2])  # Negative index slice
print(x.upper())  # x.lower()

# lets loop it,comment out and indent
# for val in x:
# print(val)

y = "Taj Mahal  "
print(y.strip())  # Remove whitespace
print(y.replace("T", "Mer"))  # Replace T with Mera
print(y.split(","))  # Split Taj, Mahal becomes Taj Mahal

# Concatenate
o = "Bike"
p = "Car"

print(o + " " + p)
