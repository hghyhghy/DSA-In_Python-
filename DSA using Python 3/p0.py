# list slicing using python

# creating a list first


l1 = [2, 3, 4, 1, 6]

print("The original list")

print(l1)

# slicing the list by using list slicing


sliced_list = l1[0:2]

print(f"The sliced list from the list {l1} is  ")

print(sliced_list)

# creating another list of string

l2 = [
    "s",
    "u",
    "b",
    "h",
    "a",
    "m",
    "l",
    "o",
    "v",
    "e",
    "s",
    "s",
    "h",
    "r",
    "e",
    "y",
    "o",
    "s",
    "h",
    "í",
]

sl1 = l2[3:8]

print("THE sliced list is")

print(sl1)

# reversing the string

print("The sliced version of that string is ")

print(l2[::-1])
