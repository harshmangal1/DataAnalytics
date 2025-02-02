# 1. Write a function to find maximum of three numbers in python.
def maximum_num(val1,val2,val3):
    if val1>val2 and val1>val3:
        print(val1,"is the greatest number")
    elif val2>val1 and val2>val3:
        print(val2,"is the greatest number")
    else:
        print(val3,"is the greatest number")

maximum_num(21,43,121)

# 2. Write a python Function to create and print a list where the values
#    are square of numbers between 1 and 30.
def create_list():
    l =[]
    for i in range(1,31):
        l.append(i**2)

    return l
print(create_list())


# 3. Write a Python function that takes a number as a parameter and check
#    if the number is prime or not.
def check_prime(num):
    if num==1:
        print("It is the prime number")
    if num == 2:
        print("it is not the prime number")
    if num > 2:
        for i in range (2,num):
            if num % i ==0:
                print("It is not a Prime Number")
                break
        else:
            print("It is a Prime Number")

check_prime(2)

# 4. Write a Python function to sum all the numbers in a list.
def add(numbers):
    total = 0
    for i in numbers:
        total = total+i
    return(total)
print(add([12,23,334,56,1]))

# Solution 2 (using Recursion)
def add(numbers):
    if len(numbers)==1:
        return(numbers[0])
    else:
        return(numbers[0]) + add(numbers[1:])

print(add([12,23,334,56,1]))

# 5. Write a Python program to solve the Fibonacci Sequence using
#    Recursion.
def fs(num):
    if num == 1:
        return(0)
    elif num == 2:
        return(1)
    else:
        return(fs(num-1)+ fs(num-2))
print(fs(3))

