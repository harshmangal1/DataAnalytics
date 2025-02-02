# Iteration using For Loop
a = ["Hulk","Thor","Ironman","America"]
for i in a:
    print(i)

# Iteration Using For loop with Range and Length function
for i in range(len(a)):
    print(i,a[i])

# Iteration Using While Loop.
i = 0
while i <(len(a)):
    print(a[i])
    i = i+1

# Using Short-Hand For Loop.
[print(i) for i in a]