L1 = [30,40,50,60]

L2 = []
for i in L1:
    if i>45:
        L2.append(i)
print(L2)

# In list Comprehensive method we use
L3 = [i for i in L1]
print(L3)

L4 = [i for i in L1 if i>45]
print(L4)