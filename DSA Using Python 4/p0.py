# some methods in the lists

# creating a list first

l = ["Subham", 122, "Shreyoshi", 300]

print("The original list is ")

print(str(l))

# append a value in the list

l.append(3000)

print("After appending the list becomes ")

print(str(l))


# .insert()  method

# creating a list

l1 = ["Subham", 122, "Shreyoshi", 300]

print("After inserting new element in the list ")

l1.insert(2, 199)

print(str(l1))

# .count

l2 = [
    1,
    2,
    3,
    1,
    2,
    3,
    4,
]

print(l2.count(2))


# .max/min

l3 = [3, 4, 1, 2, 90, 99]

print(min(l3))  # printing the minimum number

print(max(l3))  # printing the maximum number
