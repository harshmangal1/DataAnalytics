# Write a program to find a sum of all the even numbers up to 50
sum = 0
for i in range (1,51):
    if i % 2==0:
        sum +=i
print ("The summ of all even number up to 50 is", sum)

# Write a program to write first 20 numbers and their squared numbers.
for i in range (1,21):
    print(i,i**2)

# Write a program to find sum of first 10 odd numbers using while loop.
sum = 0
n= 0
while n<=20:
    if n % 2 != 0:
        sum += n
    n += 1
print("sum of first 10 odd numbers is ",sum)

# Write a program to check if a number is divisible by 8 and 12, up to 100 numbers.
for i in range (1,101):
    if (i % 8==0) and (i % 12 == 0):
        print(i)

# Write a program to create a billing system at supermarket.
while True:
    name = input("Enter customer's name: ")
    phone = (int(input("Enter here Phone no: ")))
    total = 0
    while True:
        print("Enter the Item name, amount and quantity")
        item = (input("Enter item name: "))
        amount = float(input("Enter amount: "))
        quantity = float(input("Enter quantity: "))
        total += amount * quantity
        repeat = input('Do you want to add more item? (yes/no): ')
        if repeat == "no" or repeat == "No":
            break
    print("-"*50)
    print("Name", name)
    print("Phone no", phone)
    print("-"*50)
    print("Items: ", item, "Amount to be paid: ", total)
    print("-"*50)
    print("**********HAPPY SHOPPING**********")

    repeat1 = input("Do you want to go to next customer? (yes/no): ")
    if repeat1 == "no" or repeat == "No":
        break