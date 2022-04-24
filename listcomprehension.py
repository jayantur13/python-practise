fruits = ["apple", "mango", "orange", "banana"]
# list from a list

newFruits = [x for x in fruits if "a" in x]  # 1
print(newFruits)  # apple mango orange banana all have "a"

newFruitstwo = [x for x in fruits if x != "banana"]  # 2
print(newFruitstwo)  # expect banana print everything

newFruitsthree = [x for x in fruits]  # 3
print(newFruitsthree)  # copy exactly the same

newFruitsfour = [x.upper() for x in fruits]  # 4
print(newFruitsfour)

newFruitsfive = [x for x in range(4)]  # 5 you can also have if x<2
print(newFruitsfive)

newFruitssix = [x if x != "mango" else "orange" for x in fruits]  # mango is not equals so replace with orange
print(newFruitssix)
