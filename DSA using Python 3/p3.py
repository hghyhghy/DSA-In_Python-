# returns a list of a given range

# by using numpy

import numpy as na

import itertools

# creating a function


def ofcreate(r, r1):
    return na.arange(r, r1 + 1, 1)  # the 1 is the interval between two numbers


r = -2

r1 = 2

print(ofcreate(r, r1))


# approach 2

# by using  itertools

d = -2
d1 = 2

number = list(itertools.chain(range(d, d1 + 1)))

print("The numbers are ", number)
