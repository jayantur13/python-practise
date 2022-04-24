import os

# Make sure to have a file with specified name
if os.path.exists("Pop.txt"):
    os.remove("Pop.txt")
else:
    print("File not exists")