# concatenation of tuple using python

# creating two tuple first

t = (2, 3, 1)

t1 = (1, 4, 5)

print("The first tuple is ", str(t))

print("The Second tuple is ", str(t1))

# concatenating two tuple

a = t + t1

print("The concatenation of two tuple is ", str(a))

# approach 2

# by using list

# creating two lists


t0 = (20, 3, 10)

t2 = (1, 40, 5)

print("The first tuple is ", str(t0))

print("The Second tuple is ", str(t2))

# ways to concatenate tuples

x = list(t0)

y = list(t2)

# extending the value of y to x

x.extend(y)

# making the list to tuple

res = tuple(x)

print("The tuple after concatenation is ", str(res))

# approach 3

# creating two tuples

t3 = (20, 3, 10)

t4 = (1, 40, 5)

t3 += t4

print("The tuple after concatenation is ", t3)
