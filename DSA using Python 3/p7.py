# different ways to clear the list in python

# creating a list first

l = [2, 1, 4, 3, 6, 5]

print("The list before clear ", l)

l.clear()

print("The list after clear", l)


# approach  2

# by using reinitialization

# creating a list first

l1 = [6, 7, 80, 90, 12]


print("The list before clear ", l1)

l1 = []  # reinitializing the list by an empty list

print("The list after reinitializintion is ", l1)


# approach 3

# by using * operator

# creating another  list

l2 = [65, 56, 54, 45, 43, 34]

print("The list before clear ", l2)

l2 *= 0  # using the * operator and multiplying the list by 0

print("The list after operation is ", l2)

# approach 4

# by using while loop

l0 = [1, 3, 4, 5, 6, 7]

print("The list before deleting is ", str(l0))

# using  a while loop

while len(l0) != 0:
    l0.pop()

print("After cklearing the list becomes ", str(l0))
