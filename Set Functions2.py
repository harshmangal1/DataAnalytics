a ={"Ironman","Hulk","Thor","Captain America"}
b = {"Superman","Batman","Wonder-Woman"}
c = {"Hulk","Thor","Superman"}

# union
print(a.union(c))

# Difference
print(a.difference(c))

# Difference update
"""a.difference_update(c)
print(a)"""

# Intersection
x =(a.intersection(c))
print(x)
# Intersection Update
"""a.intersection_update(c)
print(a)
"""
# Symmetric Difference
x = a.symmetric_difference(c)
print(x)

# Symmetric Difference Update
a.symmetric_difference_update(c)
print(a)