# Creation of Modules
"""
To create a module, all you need to do is create a .py file in a similar path
to your oython file. Inside that file, you can add required functions you need
your program to perform.

To call the modules inside your program, all you need to do is use import keyword
followed by the name of your .py file.
"""
import demo01 as d
a = d.add(2,3)
print(a)

b = d.employee["Name"]
print(b)