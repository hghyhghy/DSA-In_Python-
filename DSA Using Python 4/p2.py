# adding new elements to the list

# creating an empty set

s = set()

print("The empty set is ")

print(s)

# adding new elements to the set

s.add(4)

s.add(9)

s.add(8)

s.add((6, 7))

print("After addition of elements the set becomes ")

print(s)

# adding elements to the set by using iterator

for i in range(1, 6):
    s.add(i)


print("After addition of new elements the set becomes ")

print(s)


# by using update()

s1 = set([2, 3, 4, 5])

print("The set before update ")

print(s1)

s1.update([10, 11])

print("The set after update ")

print(s1)
