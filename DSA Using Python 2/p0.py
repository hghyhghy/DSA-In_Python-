# slicing the string using python

# by using  string slicing method

s = "Subhamandshreyoshi"

print("The originl string before slicing is ")

print(s)

print("Slicing the character from 3-12 is ")

print(s[3:12])

print("slicing characters between 3rd to second last element of the character ")

print(s[3:-2])


# program to reverse a string

# taking a string first

s1 = "kubernetes"

print(s1[::-1])


# reversing a string by using .join and reversed

gfg = "pythonprogramming"

gfg = " ".join(reversed(gfg))

print("The reverse version of the string is", gfg)
