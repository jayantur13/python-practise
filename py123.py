import os.path
import inflect
import camelcase
p = inflect.engine()

filename = str(input("Enter file name with ext: \n"))
if os.path.exists(filename):
    opnf = open(filename, "r")
    readdata = opnf.read()
    c = camelcase.CamelCase()
    toadd = c.hump(p.number_to_words(readdata))
    opnapp = open(filename, "a")
    opnapp.write(" "+toadd)
    opnapp.close()

    opnread = open(filename, "r")
    print(opnread.read())
else:
    print("File not exists")
