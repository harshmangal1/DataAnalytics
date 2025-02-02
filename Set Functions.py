a ={"Ironman","Hulk","Thor","Captain America","Vision"}

# add
a.add("spiderman")
print(a)

# pop
"""a.pop()
print(a)"""

# remove
a.remove("Thor")
print(a)

# discard
a.discard("Hulk")
print(a)

# copy
b = a.copy()
print(b)

a ={"Ironman","Hulk","Thor","Captain America"}
b = {"Superman","Batman","Wonder-Woman"}
c = {"Hulk","Thor","Superman","Batman"}

# isdisjoint
print(a.isdisjoint(c))

# issubset
print(c.issubset(a))

# issuperset
print(a.issuperset(c))

# update
a.update(c)
print(a)

# clear
a.clear()
print(a)

