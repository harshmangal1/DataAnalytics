# Loops
"""
A loop means to repeat something in the exact same way.
Types of loops are:
    1. For Loop
    2. While Loop
    3. While True
    4. Nested Loop

# For Loop: * For loop is a loop that repeats something in a given range.
            * The range has a starting point, ending point and a step/gap in it.
            * +1 is added to the ending point while defining a range.
Example: for i in range (1,10):
              print("hello world")

        multiplication:
        n = int(input("Enter a number here: "))
        for i in range (1,11):
            print(n,"*",i,"=",n*i)

# While Loop: * While Loop executes till the given condition is true.
              * In while loop, the increment is done inside the loop.
Example: n= 0
         while n<= 5:
             print(n)
             n +=1

        Multiplication table:
             n = 1
             a = int(input("Enter a number here: "))
             while n<= 10:
                print(a,"x",n,"=",n*a)
                n +=1

# While true: * It is an infinite loop
              * To break a while true loop, break statement is used.
Example: while True:
           print("hello world") // infinite loop

// if you stop these infinite loop then use break statement
while True:
    num1 = int(input("Enter a number here: "))
    num2 = int(input("Enter another number here: "))
    print(num1+num2)
    repeat = input("Do you want to stop the program: ")
    if repeat == "yes":
        break

# Nested Loops: * A loop inside a loop is called as nested loop.
                  Nested loops are also used to solve pattern problems.
Structure:
    for loop:
        for loop:
            body of inner for loop
        body for outer for loop
Example:
    for i in range (1,4):
         for j in range(1,11):
              print(j, end=" ")
         print()

pattern problem :
for i in range (1, 6):
    for j in range (1,i+1):
        print(j, end=" ")
    print()

# For Loop with conditional statements: The use of if-else statement increase the ability of for loop
                                        to completes the task effectively. By using if-else statements
                                        we can provide with special conditions inside for loop.
Example:

using for loop:
          for i in range (1, 11):
             if i == 3:
                 print ("add this song to the favs")
             else:
                print(i)

using while loop:
          n= 1
          while n<=10:
              if n ==3:
                 print("add this in my favs")
              else:
                print(n)
              n+=1
              
multiplication of 2 numbers:
for i in range (1,101):
    if i % 8==0 and i % 12 == 0:
        print(i)
"""
n = 1
while n <= 10:
    if n == 3:
        print("add this in my favs")
    else:
        print(n)
    n += 1