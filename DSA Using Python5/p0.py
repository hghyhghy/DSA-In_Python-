# python set using difference() function

# creating two sets
a = {1, 2, 3, 5, 6, 7}

b = {4, 8, 9, 10, 11}


# obtaining the difference

print(f"The difference between {a} and {b} is ")

print(a.difference(b))

print(f"The difference between {b} and {b} is ")

print(b.difference(a))


# approach 2

# by using - operator

a1 = {1, 2, 3, 5, 6, 7}

b1 = {4, 2, 3, 1, 11}

print(f"The difference between {a1} and {b1} is ")

print(a - b)

print(f"The difference between {b1} and {b1} is ")

print(b - a)
