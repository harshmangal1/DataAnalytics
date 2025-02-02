# Type Casting
"""
Conversion of one datatypes to another is called as type-casting.

There are two types of type-casting:
1. Implicit Type Conversion: where python itself converts one datatype to another.
2. Explicit Type Conversion: where the user converts one data type to another.
"""

# implicit
a = 123
b = 1.23
print(type(a))
print(type(b))

c = a+b
print(c)
print(type(a+b))

# Explicit
a = "123"
b = 1.23
A = int(a)
print(type(A))
print(type(b))