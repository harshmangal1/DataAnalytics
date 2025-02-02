# Return Statement
"""
Return keyword in python is used to exit a function and return the value of the function
"""
def hello():
    return("hello world")
print(hello())

def add(a,b):
    return("The addition of two numbers",a+b)
print(add(12,23))

# Recursion:
"""
Recursion in most commonly used mathematical and programming concept.

In Simple words, recursion means a function can call itself, giving us a
benefit of looping through dta in order to get a result.
"""

# example
"""def hello():
    print("hello")
    return hello()
print(hello())"""

# factorial
def fact (n):
    if n == 1:
        return 1
    else:
        return(n*fact(n-1))
print(fact(5))
