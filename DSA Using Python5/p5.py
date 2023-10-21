# accessing the elements in python

import array as arr

a = arr.array("i", [1, 2, 3, 4, 5, 6])

print("The  original elements are ")

for i in range(0, 6):
    print(a[i], end=" ")

print()

# accessing the elements

print("The first element of the array ")

print(a[0])

print("The second element of the array ")

print(a[1])

# creating an array with float type values

b = arr.array("d", [1.0, 2.0, 3.4, 5.4])

print("The float elements are:")

for x in range(0, 4):
    print(b[x], end=" ")

print()

print(f"The first element of the {b} is ")

print(b[0])
