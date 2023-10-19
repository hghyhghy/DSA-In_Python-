# printing the length  of the list

# creating the list first

l = []

print(len(l))

l = [2, 1, 4, 3]

print("After entering new elements in the thr list the length is ", len(l))


# taking user input for creating   a list

string = input("Enter elements ")

lst = string.split()

print("The list is ", lst)

# inserting new  elements to the list

# creating a list first

lis = [2, 1, 3, 4]

print("The list before insertion is ")

print(lis)

# inserting new element in the list by using insert ()

lis.insert(3, "Century By")

lis.insert(4, "Virat Kohli")

print("After inserting the list becomes ")

print(lis)

# enetring elements at the beginning of the list

lis.insert(0, "NO 18")

print(lis)
