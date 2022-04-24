# To open a file use open("path/name.format","mode")
f = open("example.txt", "r")  # open file in read mode
# print(f.read())  # Will read the complete file
# print(f.read(20))  # f.read(20) read 20 first 20 characters
# print(f.readline())  # read first line
# print(f.readline())  # read second line
# print(f.readline(5) # read first 5 characters of a line

# Similar to f.read()
for x in f:
    print(x)

f.close();
