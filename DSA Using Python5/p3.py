# creating an array

import array as ar


# creating an array with integer type

a = ar.array("i", [1, 2, 3])

print("The new created array is ", end=" ")

for i in range(0, 3):
    print(a[i], end=" ")

print()

# creating another array  with float values

b = ar.array("d", [1.2, 2.4, 3, 5])

print("The second created array is", end=" ")

for i in range(0, 3):
    print(b[i], end=" ")

print()
