numbers = [1, 2, 3, 4, 5, 6, 7, 10, 20, 40]
for val in numbers:
    print(val)
    if val == 5:
        break  # prints up to 5 only

for val in numbers:
    if val == 5:
        continue  # prints upto 4; skips 5 and continues to print
    print(val)

# range
for x in range(5):
    print(x)  # prints upto 4 || range(20,40) prints from 20 to 39
