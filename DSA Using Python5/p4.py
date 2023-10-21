# importing array

import array as ar


# creating an array

a = ar.array("i", [1, 2, 3, 4])

print("The original array is ")

for i in range(0, 4):
    print(a[i], end=" ")

print()

# inserting an element at index 1

a.insert(1, 99)

for i in a:
    print(i, end=" ")

print()
