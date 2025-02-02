a = ["Thor","Hulk","Ironman","Captain America"]
# To create a copy of a List
b =[]
print(b)
b = a.copy()
print(b)

# To access an element
print(a.index("Ironman"))

# To extend the list
c = ["vision","spiderman"]
a.extend(c)
print(a)

# To reverse the list
a.reverse()
print(a)

# To sort the list
a.sort()
print(a)

# To clear all the data from the list
a.clear()
print(a)