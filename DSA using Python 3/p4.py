# accessing the values and index from a list


# creating a list

l = [3, 4, 5, 6, 7]

print("The list before accessing all elements are ", str(l))


print("list index values are ")


# using a for loop to iterate

for i in range(len(l)):
    
    print(i, end=":")

    print(l[i])


# approach  2

# by using enumerator ()

# creating another list

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Original list is ", str(l1))

print("The original list with index values are ")

# using  enumerator  and for loop


for index, values in enumerate(l1):
    print(index, values)
