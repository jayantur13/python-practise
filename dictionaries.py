# Dictionaries are unordered, changeable and not allow duplicate values
dictt = {'name': 'mohan',
         'age': 20,
         'favs': ["Anime", "Series", "Movies"],
         'vehicle': 'Scooty'}
print(type(dictt))
print(dictt)
print(len(dictt))

# Access item
print(dictt["vehicle"])
x = dictt.get("vehicle")
print(x)

# Change value
dictt.update({"name": "Prakash"})
print(dictt)
dictt["vehicle"] = "Yamaha"
print(dictt)

# Add a value (appends at last)
dictt["favColor"] = "Blue"
print(dictt)

# Remove a value favColor
dictt.pop("favColor")
print(dictt)  # favColor is removed
