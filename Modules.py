# Modules
"""
Modules are the (.py) files, that contains set functions you want to include in your program
"""

# In-built Modules in Python
"""
Datetime
Random
math
"""
import datetime

x = datetime.datetime.now()
print(x)



import random

# for integer
y = random.randint(1,10)
print(y)

# for strings
l = ["Heads","Tails"]
z= random.choice(l)
print(z)



import math
x = max(13,67,45)
print("The maximum value is", x)

y = min(13,2,27,1,0,27)
print("The minimum value is", y)

a = pow(2,5)      # power
print(a)

b = math.sqrt(256)   #square root
print(b)

c = abs(-12)       #absolute = it converted negative value into positive
print(c)

# floor & ceil = floor will get the minimum closet value of division and ceil will get the value in maximum closet value
k = math.ceil(2.4)
print(k)
m = math.floor(2.4)
print(m)
