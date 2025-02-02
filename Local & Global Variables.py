# Local Variables
"""
Local variables are restricted to only one block of code and
cannot be changed throughout the program.
"""
x = 24
print("first variable x ",x)
def hello():
    x = 25
    return x
print(hello())
print(x)

# Global Variables
"""
Global variables are not restricted to one block of code they
can be changed throughout the program. """

x = 24
print("first variable x ",x)
def hello():
    global x
    x = 25
    return x
print(hello())
print(x)