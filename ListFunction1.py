a = ["Thor","Hulk","Ironman","Caption America","Hulk"]
print(a)
# To find the length of a List.
print(len(a))

# To count an Occurence of a particular element.
print(a.count("thor"))

# To add to the list.
a.append("spiderman")
print(a)

# To add to a specific location.
a.insert(-4,"Vision")
print(a)

# To remove from a list.
a.remove("spiderman")
print(a)

# To remove from a certain location.
print(a.pop(-1))
print(a)