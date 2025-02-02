# endswith() - Returns true if the string ends with the specified value
a = "Harry Potter"
print(a.endswith("r"))

# startswith() - Returns true if the string starts with the specified value
a = "Harry Potter"
print(a.startswith("p",6,9))
print(a.startswith("H"))

# swapcase() - Swap cases, lower case becomes upper case and vice versa
a = "Harry Potter"
print(a.swapcase())

# strip() - returns a trimmed version of the string
a = "          Harry Potter          "
print(a)
print(a.strip())

# split() - Splits the string at the specified separator, and returns a list
a = "00FG#$$^&()#JBSF("
b = "hello. my name is john. i am 23 year old"
print(a.split("#"))
print(b.split("."))

# ljust() - Returns a left justified version of the string
a = "Harry Potter"
x = a.ljust(20,".")
print(x,"is my favourite")

# rjust() - Returns a right justified version of the string.
a = "Harry Potter"
y = a.rjust(40,"*")
print(y,"is my favourite")

# replace() - Returns a string where a specified value is replaced with a.
# specified value
a = "my name is john. john likes to play footbal. john i"
print(a.replace("john","lisa"))

# rindex() - Searches the string for a specified value and returns the last position of where it was found.
a = "Harry potter and the Prisoner of Azkaban"
print(a.rindex("Prisoner"))
print(a.rindex("a"))

# rfind() - Searches the string for a specified value and returns the last position of where it was found.
a = "Harry potter and the Goblet of Fire"
print(a.rfind("a"))