# String Manipulation
"""
Strings are the combination of number, symbols and letters, enclosed inside quotations.

Creation of a String : Strings can be created by enclosing numbers, letters or special
symbols inside double quotations.
it means assigning a string value to a variables.
a = ("hello world")
print(a)

methods : 1. length - To find length of the string.
          2. count - To find the number of times character is occuring.
          3. upper - To convert each letter into uppercase.
          4. lower - To convert each letter into lowercase.
          5. index - To find the index of any character.
          6. capitalize - To convert the first letter to capital.
          7. casefold - to convert a string in to lowercase.
          8. find - to find the index of a character.
          9. format - To write variables inside a string.
          10. centre - if fills the given characters and centralizes a string.
          11. isalnum - Returns True if all characters in the string are alphanumeric.
          12. isalpha - Returns True if all characters in the string are in the alphabet.
          13. isdecimal - Returns True if all characters in the string are decimal.
          14. isdigit - Returns True if all characters in the string are digits.
          15. isnumeric - Returns True if all characters in the string are numeric.
          16. islower - Check if the string is lower case or not.
          17. isupper - Returns True if all characters in the string are upper case.
          18. isspace - Returns True if all characters in the string are whitespaces.
          19. istitle - Returns True if all string follows the rules of a title.




a = "hello world"
length: print(len(a))

count: print (a.count("l")

upper: print(a.upper())

lower: print(a.lower())

index: print(a.index("o")

capitalize: print(a.capitalize())

casefold: print(a.casefold())

find: print(a.find("o",1,7))

format: name = "john"
age = 23
b = "my name is {}. and my age is {}"
print(b.format(name,age))

centre: print (name.center(20,"*"))

isalnum: a = "hello"
         b = "123hello"
         c = "123456"
         d = "HELLO"
         e = " "
         f = "Hello 123"
         g = "1.234"
         print(a,a.isalnum())
         print(b,b.isalnum())
         print(c,c.isalnum())
         print(d,d.isalnum())
         print(e,e.isalnum())
         print(f,f.isalnum())
         print(g,g.isalnum())

isalpha: print(a,a.isalpha())
         print(b,b.isalpha())

isdecimal: print(a,a.isdecimal())
           print(b,b.isdecimal())
           print(c,c.isdecimal())

isdigit: print(a,a.isdigit())
         print(b,b.isdigit())
         print(c,c.isdigit())

isnumeric: print(a,a.isnumeric())
           print(b,b.isnumeric())
           print(c,c.isnumeric())

islower: print(a,a.islower())
         print(b,b.islower())
         print(d,d.islower())

isupper: print(a,a.isupper())
         print(b,b.isupper())
         print(d,d.isupper())

isspace: print(e,e.isspace())
         print(f,f.isspace())

istitle: h = "Harry Poter An The Goblet Of Fire"
         print(h,h.istitle())


"""

a = "hello world"
print(len(a))
print(a.count("l"))
print(a.upper())
print(a.lower())
print(a.index("l"))
print(a.capitalize())
print(a.casefold())
print(a.find("o",1,7))
name = "john"
age = 23
b = "my name is {}. and my age is {}"
print(b.format(name,age))
print (name.center(20,"*"))

a = "hello"
b = "123hello"
c = "123456"
d = "HELLO"
e = " "
f = "Hello 123"
g = "1.234"

print(a,a.isalnum())
print(b,b.isalnum())
print(c,c.isalnum())
print(d,d.isalnum())
print(e,e.isalnum())
print(f,f.isalnum())
print(g,g.isalnum())

print(a,a.isalpha())
print(b,b.isalpha())

print(a,a.isdecimal())
print(b,b.isdecimal())
print(c,c.isdecimal())

print(a,a.isdigit())
print(b,b.isdigit())
print(c,c.isdigit())

print(a,a.isnumeric())
print(b,b.isnumeric())
print(c,c.isnumeric())
print(g,g.isnumeric())

print(a,a.islower())
print(b,b.islower())
print(d,d.islower())

print(a,a.isupper())
print(b,b.isupper())
print(d,d.isupper())

print(e,e.isspace())
print(f,f.isspace())

h = "Harry Poter An The Goblet Of Fire"
print(h,h.istitle())