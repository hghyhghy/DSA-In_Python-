# merging two list in a python

# initializing the lists

testl = [2, 3, 4, 5, 6]

testl1 = [1, 70, 80, 90, 20]

# iterating the values on the lists

for i in testl1:
    testl.append(i)

print("The concatenated lists are ", testl)


# approach 2

# by using + operator

# creating another lists

l1 = [1, 2, 3, 4, 5]

l2 = [6, 7, 8, 9, 10]

l1 = l1 + l2

print("The concatenated lists are ", l1)


# approach 3

# by using extend()  function


# creating  two other lists

l3 = [20, 30, 40, 50, 60]

l4 = [12, 23, 34, 45, 56]

# extending one list values by another

l3.extend(l4)

print("The extnded and concatenated list is ", l3)
