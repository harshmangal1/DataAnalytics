# Slicing
a = ("Oneplus","Vivo","Redmi","Nokia")
print(a[1:3])
print(a[:3])
print(a[2:])
print(a[1::2])
print(a[::-1])
print(a[2::-1])

# iteration
for i in a:
    print(i)

# along with range and length in for loop
for i in range(len(a)):
    print(a[i])

# along with while loop
i = 0
while i < len(a):
    print(a[i])
    i = i +1