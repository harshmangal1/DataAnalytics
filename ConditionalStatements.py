"""
Conditional Statement allow computer to execute a certain condition
if only if it is true:
Types of conditional statements:
1. if the statement
2. if-else statement
3. if-elif-else statement
4. Nested statement
5. Short Hand if statement
6. Short Hand if-else statement

# IF Statement=> The if statement is the most fundamental decision-making statement
                 The is statement in python has the subsequent syntax:
                 if expression
                 statement
                 Example: marks = 87
                          if marks >= 90:
                             print ("you will get a mobile phone")
                          print ("thankyou")
# If-else Statement=> If-else statement is used when you want to give two conditions to the computer.
                      Here if one condition is false, program executes the another condition.
                      if condition:
                             # will executes this block if the condition is true
                      else:
                             # will executes this block if the condition is false

                      Example: marks = 87
                               if marks >= 90:
                                   print("you will get a phone")
                               else:
                                   print("no phone for 1 week")
                               print("thank you")

# If-elif-else Statement=> In this case, the if condition is evaluated first. if it is false, the elif statement will
                           be executed, if it also comes false then else statement will be executed.
                           For multiple conditions, more elif statements are added.
                           if condition :
                                  Body of if
                           elif condition:
                                  Body of elif
                           else:
                                  Body of else

                           Example: marks = 87
                                    if marks >= 90:
                                          print ("you can go to a trip")
                                    elif marks >=80 and marks <90:
                                          print ("you will get a new phone")
                                    elif marks >=70 and marks <80:
                                          print ("you will get a new book")
                                    else:
                                          print ("you will not get your phone back")

# Nested if Statement=> A Nested if statement is one in which an if statement is  nestled
                        inside another if statement. This is used when a variable must be
                        processed more than once. The Nested if statement in python has the
                        following syntax:
                        if (condition1):
                        #Executes if condition 1 is true
                        if (condition2):
                        #Executes if condition 2 is true
                        #Condition 2 ends here
                        #Condition 1 ends here

                        Example: marks = 99
                                 if marks >= 80:
                                         print("you will get a new phone")
                                         if marks >=95;
                                              print("you can not go to a trip")
                                 else:
                                      print ("no phone for 1 week")

# Short Hand if Statement=> Short Hand if statement is used when only one statement needs to be executed inside the
                          if block. This statement can be mentioned in the same line which holds the if statment.
                                  The Short Hand if statement in python has the following syntax:
                          if condition: statement
                          Example: marks = 97
                                   if marks >= 90: print("you will get a new phone")

# Short Hand If-else statement=> it is used to mention if-else statements in one line in which there is only one
                                 statement to execute in both if and else blocks. In simple words, If you have
                                 only one statement to execute, one for if, and one for else, you can put it all
                                 on the same line.

                                 Example: marks = 97
                                          print ("you will go to a trip") if marks >=90 else print("no phone for a month")


"""