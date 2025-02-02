# conversion
a = ("Oneplus","Nokia","Redmi")
print("before Conversion",type(a))

a = list(a)
print("after conversion",type(a))
a.append("vivo")
print(a)
print(type(a))
a = tuple(a)
print(type(a))

# Functions
print(a.count("Redmi"))

print("the index of redmi is",a.index("Redmi"))