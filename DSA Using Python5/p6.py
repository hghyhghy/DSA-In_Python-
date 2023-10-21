# creating an array

import array as ar

a = ar.array("i", [2, 3, 4, 5])

print("The original array is ")


# using a for loop

for i in range(0, 4):
    print(a[i], end=" ")

print()

# popping an  element

print("The popped element is ", end=" ")

print(a.pop(2))

print(a)

# deleting an element by using remove

a.remove(3)

print("After removing the element the array becomes ")

print(a)
