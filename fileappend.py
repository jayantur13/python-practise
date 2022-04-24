# open a file and add at last; a for append mode
f = open("example.txt", "a")
f.write("\nThis line will be added at last")
f.close()

f = open("example.txt", "r")
print(f.read())
f.close()

# if you open a file in write mode i.e w it will overwrite everything and a single input you gave will remain
