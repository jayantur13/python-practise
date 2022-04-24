# list is a collection of similar or different type of data
# list is ordered,changeable and allow duplicate values
liste = [1, 2, 3.0, "car", "bike", True, False, "bike"]
print(len(liste))
print(type(liste))
print(liste[5])  # outputs to True
print(liste[2:5])  # print from index 2 to 5 (i.e 4)

# Changing an item from 2 to 20
liste[1] = 20
print(liste)

# Changing in a range 3:5 (i.e 4)
liste[3:5] = ["Bus", "Tractor"]  # outputs car -> Bus and bike -> Tractor
print(liste)

# insert item to a certain position .insert(pos,item)
arr = [2, 4, 6, 8, 8, 10]
arr.insert(0, 1)  # Insert 1 to index 0

# append,adds to the last of list
arr.append(15)  # [ 1, 2 , 4 , 8 , 8 ,10 ,15]
arr.remove(4)  # remove element 4
print(arr)
