# checking if two lists are identical or not

import collections

t1 = [1, 2, 3, 4, 6, 5]

t2 = [1, 2, 3, 4, 6, 5]

print("The first list is ", t1)

print("The second list is", t2)

# sorting the lists

t1.sort()

t2.sort()

# using a if else loop to check


if t1 == t2:
    print("The two lists are identical")
else:
    print("The two lists are not identical ")


# approach 2


# by using collections

t1 = [1, 2, 3, 4, 6, 5]

t2 = [1, 2, 3, 4, 6, 5]


print("The first list is ", t1)

print("The second list is", t2)

if collections.Counter(t1) == collections.Counter(t2):
    print("The two lists are identical")
else:
    print("The two lists are not identical ")
