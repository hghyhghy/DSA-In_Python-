

# implementation of linked list by using structlinks

import structlinks

from structlinks import LinkedList

lst=LinkedList


lst=lst.LinkedList([1,10,20,"Subham and Shreyoshi"])

# the created linked list is 

print(lst)

# printing  all the elements from the linked list 

for x in lst:

       print(x)

# printing the length of the list 

print(f"The length of the list {lst}  is ",len(lst))

# setting a new item in the linked list 

# setting an item to the position 0

print("Set items ")

lst[0]=0

print(lst)

# appending and inserting elements in the linked list 

print("Append and insert operation ")

lst.append("They love each other")

lst.insert(1,3)

# printing the updated list 

print(lst)

# removing a specific element from the list 

lst.remove(0)

print(lst)


