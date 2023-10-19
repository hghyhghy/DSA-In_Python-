# python clearing a tuple

# creating a tuple first

t = (20, 3, 10)

print("The original tuple is ", str(t))

# tuples are immutable

# to remove we have to make it list first

# setting up a temp variable to store the values

temp = list(t)

# clearing the list by using clear()

temp.clear()

# making the list again tuple

t = tuple(temp)

print("After removing elements the tuple becomes ", str(t))


# approach 2

# by using reinitialization + tuple()

t2 = (1, 40, 5)

print("The original tuple before removal is ", str(t2))

# claring up a tuple

t2 = tuple()

print("After removing elements the tuple becomes ", str(t2))

# approach 3

# by using * operator

# creating a tuple

tu = (1, 40, 50, 0)

print("The original tuple before removal is ", str(tu))

tu = tu * 0

print("After removing elements the tuple becomes ", str(tu))
