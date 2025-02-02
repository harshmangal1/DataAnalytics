# Iteration in Dictionary
student = {"name":"John","class":"6th","roll_no":37}

# printing all the key names one by one
for x in student:
    print(x)

# printing all the value names one by one
for x in student:
    print(student[x])

# using value function
for x in student.values():
    print(x)

# using items function
for x,y in student.items():
    print(x,y)