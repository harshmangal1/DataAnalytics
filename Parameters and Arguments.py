# Parameters:
"""
Parameters are the variables written inside the parentheses with the name of function.
"""

# Arguments:
"""
Arguments are the values passed to the parameters while calling the function.
"""

def add(x,y):             #<----parameters
    print(x+y)

add(12,556)         #<----Arguments
add(12,22)

def rect(length,width):
    print("the area of the rectangle is", length*width)
rect(12,2)

# arbitary arguments
def hello(*name):
    print("hello, my name is",name[1])
hello("lisa","arun","minu")