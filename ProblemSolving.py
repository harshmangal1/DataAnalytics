"""
1. Write a program to display a person's name, age and address in
three different lines."""
name = "john"
age = 23
address = "654 lake street"
print(name)
print(age)
print(address)

"""2. Write a program to swap two variables."""
# method 1
x = 12
y = 13

temp = x
x = y
y = temp
print (x)
print(y)

# method 2
a = 30
b = 20
a,b=b,a
print("value of",a)
print("value of",b)

"""3. Write a program to convert a float into integer."""
x = 12.3
print(type(x))
x = int(x)
print(type(x))

"""4. Write a program to take details from a student for ID-card and 
then print it in different lines."""

name = input("Enter the name of the Student")
grade = input("Enter the grade of the Student")
age = input("Enter the age of the Student")
email = input("Enter the email of the Student")
phone = input("Enter the phone number of the Student")
print("Student Identity Card")
print(name,email,phone,age,grade)

"""5. Write a program to take an user input as integer then convert to float.
"""
a = int(input("Enter a number here: "))
print(a)
print(type(a))
b = float(a)
print(b)
print(type(b))