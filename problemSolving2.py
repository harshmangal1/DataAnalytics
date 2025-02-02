# 1. Write a program to check if a number is positive.
"""num = int(input("Enter a number here: "))
if num>0:
    print("it is positive")"""

# 2. Write a program to check whether a number is odd or even.
"""num = int(input("Enter a number here: "))
if num % 2 ==0:
    print (" it is an even number")
else:
    print(" it is an odd number")"""

# 3. Write a program to create area calculator.
"""
print ("***AREA CALCULATOR***")
print ('''press 1 to get the area of square
press 2 to get the area of rectangle
press 3 to get the area of circle
press 4 to get the area of triangle''')

choice = int(input("Enter a number between 1-4: "))
if choice == 1:
    side = float(input("Enter the length of one side: "))
    area = side ** 2
    print ("The area of square is ", area)
elif choice == 2:
    length = float(input("Enter the length of the rectangle"))
    width = float(input("Enter the length of the rectangle"))
    area = length * width
    print("The area of rectangle is ", area)
elif choice == 3:
    radius = float(input("Enter the radius of the circle"))
    area = (22/7)*(radius**2)
    print("The area of circle is ", area)
elif choice == 4:
    base = float(input("Enter the base of the triangle"))
    heigth = float(input("Enter the height of the triangle"))
    area = 0.5*base*heigth
    print("The area of triangle is ", area)
else:
    print("invalid input")
"""

# 4. Write a program check whether the passed letter is a vowel or not.
"""letter = input("Enter a letter here: ")
if (letter in "aeiou") or (letter in "AEIOU"):
    print("it is a vowel")
else:
    print("it is not a vowel")"""

# 5. Write a program to check if a number is a single digit number, 2-digit
#    number and so on.. , up to 5 digits.
"""
num = int(input("Enter a number here up to 5 digit: "))
if num >= 0 and num <= 9:
    print("it is a single digit number")
elif num >= 10 and num <= 99:
    print("it is a two digit number")
elif num >= 100 and num <= 999:
    print("it is a three digit number")
elif num >= 1000 and num <= 9999:
    print("it is a four digit number")
elif num >= 10000 and num <= 99999:
    print("it is a five digit number")
else:
    print("Digit is OutOff range")"""
