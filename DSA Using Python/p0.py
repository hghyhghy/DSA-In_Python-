
# implementation of linked list by using deque() package 

import collections

# initializing a deque with a arbitary  length 

linkedlist=collections.deque()

# filling deque with elements 

linkedlist.append("Subham")

linkedlist.append("Shreyoshi")

linkedlist.append("Sukriti")

linkedlist.append("Sneha")

# printing the elements present in the list 

print("The elements present in the list is ")

print(linkedlist)

# adding a  new element in a position of the list 

linkedlist.insert(2,"Shreya")

linkedlist.insert(5,"Sristi")


print(linkedlist)

# deleting an element from the list 


linkedlist.pop()

print(linkedlist)

# removing a specific  element from a list 

linkedlist.remove("Sukriti")


print(linkedlist)











