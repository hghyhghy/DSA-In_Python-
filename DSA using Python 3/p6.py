# checking wheather a particular element is present in the list or not

# creating aa list first

list1 = [6, 5, 4, 3, 9, 2, 0, 1]


print("The original list is ")

print(str(list1))


# seeting up the number to be searched

y = 3

# using a if else loop

if y in list1:
    print(f"Yes the element {y} is present  in list {list1}")
else:
    print(f"No the element {y} is not present in list {list1}")


# approach 2

# by using for loop

l = [20, 5, 4, 30, 99, 29, 0, 1]

# checking if i = 4 exists in the list or not

# iterating by using for loop

for i in l:
    if i == 4:
        print(f"Yes the element  is present  in list {l}")


# approach 3

# by using count

testlist = [10, 1, 12, 13, 34]

print("The original list is ", str(testlist))

exist_count = testlist.count(13)

# using a if else loop

if exist_count > 0:
    print("The element is present")

else:
    print("The element is not present in the list ")
