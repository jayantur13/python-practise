import json

# Dict as string
person = '{"name": "bob","age": "20"}'
newdict = json.loads(person)
print(newdict)
print(newdict['age'])

# Make a dictionary and pass it json.dumps(..) for json structure
pp = {"name": "bob", "age": "20"}
newdt = json.dumps(pp)
print(newdt)

# Write json to a file,using the above pp dictionary
with open('myjsnfile.txt', 'w') as jsnfile:
    json.dump(pp, jsnfile)

# To open and use json file use json.load('file.json') [Parsing]

with open('data.json') as f:
    thedata = json.load(f)

print(thedata)

# Pretty Print,sort keys True to sort in ascending order i.e a to z
print(json.dumps(thedata, indent=4, sort_keys=True))
