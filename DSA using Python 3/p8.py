# reversing a list using python

# creating a function first


def ofreverse(r):
    newr = r[::-1]

    return newr


r = [1, 2, 3, 4, 5, 6]

print(ofreverse(r))


# approach 2

# using reverse ()

# creating another list

lst = [40, 50, 60, 70, 80, 90]

print("The original list is ", lst)

lst.reverse()

print("The reversed version of the list is ", lst)


# approach 3

# by using a for loop

# creating another list

l3 = [10, 20, 30, 40, 50]

# creating an empty  list to store the values

store_l = []

# using a for loop

for i in l3:
    store_l.insert(0, i)

print("The reversed order is ", store_l)
