# 0 1 1 2 3 5 8
lim = int(input("Enter the limit to print fibonacci series"))
a = 0
b = 1
print(a, b)
for val in range(lim - 2):
    c = a + b
    print(c)
    a = b
    b = c
