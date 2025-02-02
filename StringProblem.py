A = "OOTD.YOLO.ASAP.BRB.GTG.OTW"
Z= "F.R.I.E.N.D.S."
# 1. Write a program to separate the following string into coma(,) separated values.
"""B = A.split('.')
print(B)

# 2. Write a program to sort strings alphabetically in python
a = input("Enter anything here: ")
b = sorted(a)
print(b)

# 3. Write a program to remove a given character from a string.
a = "hello"
b = a.replace("e","i")
print(b)

# 4. Write a program to remove dot(.) from the following string.
BA = Z.replace(".","")
print(BA)

# 5. Write a program to check the number of occurence of substrings
A = "She sells seashells on the sea shore"
bb = A.count("sea")
print(bb)"""

# 6. Take an input from a user as a string then, reverse it.
"""a = input("Enter anything here: ")
print(a[::-1])"""

# 7. Write a program to check if a string contains only digits.
"""a = input("Enter anything here: ")
b=(a.isdigit())
if b == True:
    print("it contains only digits")
else:
    print("it does not contain only digit")"""

# 8. Write a program to check if a string is palindrome.
"""a = input("Enter anything here: ")
rev = a[::-1]
if a == rev:
    print("it is palidrome")
else:
    print("it is not palidrome")
"""

# 9. Write a program to find number of vowels in a string.
"""
a = input("Enter anything here: ")
vowels = 0
for i in a:
    if i=="a" or i=="e" or i=="i" or i=="o" or i=="u" or i=="A" or i=="E" or i=="I" or i=="O" or i=="U":
        vowels +=1
print("The number of vowels in the following string are ",vowels)
"""

# 10. Write a program to check if every word in a string begins with a capital letter.
a = input("Enter anything here: ")
print(a.istitle())