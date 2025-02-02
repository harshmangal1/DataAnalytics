# loops
# Write a program to get Fibonacci series upto 10 numbers.
from itertools import repeat

a = 0
b = 1
n = int(input("Enter a number here: "))
if n == 1:
    print(1)
else:
    print(a)
    print(b)
    for i in range (2,n):
        c = a+b
        a = b
        b = c
        print(c)
# Write a program to check if a number is prime or not.
num = int(input("Enter a number here: "))
if num <= 1:
    print("it is not a prime number")
else:
    for i in range (2, num):
        if num % i == 0:
            print("Number is not a prime number")
            break
    else:
        print("It is a prime number")

# Write a program to find a palindrome of integers.
num = int(input("Enter a number here: "))
temp = num
rev = 0
while num> 0:
    dig = num%10
    rev = rev*10 + dig
    num = num // 10
if rev == temp:
    print("it is palidrome number")
else:
    print("it is not a palidrome number")

# Write a program to create an area calculator
print ("***AREA CALCULATOR***")
while True:
    print ('''press 1 to get the area of square
    press 2 to get the area of rectangle
    press 3 to get the area of circle
    press 4 to get the area of triangle''')

    choice = int(input("Enter a number between 1-4: "))

    if choice == 1:
        while True:
            side = float(input("Enter the length of one side: "))
            area = side ** 2
            print ("The area of square is ", area)
            repeat = input("Do you want to try again with Square? ")
            if repeat == "no":
                break

    elif choice == 2:
        while True:
            length = float(input("Enter the length of the rectangle"))
            width = float(input("Enter the length of the rectangle"))
            area = length * width
            print("The area of rectangle is ", area)
            repeat = input("Do you want to try again with Rectangle? ")
            if repeat == "no":
                break

    elif choice == 3:
        while True:
            radius = float(input("Enter the radius of the circle"))
            area = (22/7)*(radius**2)
            print("The area of circle is ", area)
            repeat = input("Do you want to try again with Circle? ")
            if repeat == "no":
                break

    elif choice == 4:
        while True:
            base = float(input("Enter the base of the triangle"))
            heigth = float(input("Enter the height of the triangle"))
            area = 0.5*base*heigth
            print("The area of triangle is ", area)
            repeat = input("Do you want to try again with Triangle? ")
            if repeat == "no":
                break
    else:
        print("invalid input")
#
# repeat1 = input("Do you want to repeat the menu again? ")
# if repeat1 == "no"
# break
