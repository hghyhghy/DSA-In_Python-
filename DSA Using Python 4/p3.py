# iterating through the set by using loops

# creating a set


s1 = set([2, 3, 4, 5, 50])

# using a for loop


for x in s1:
    print(x, end=" ")


# removing elements from  the set


s2 = set([2, 30, 4, 5, 50, 77])

print("The initial set is ")

print(s2)

# removing the elements by using  remove

s2.remove(50)

print("Äfter removal the list is ")

print(s2)


# removing elements by using discard

s2.discard(77)

print("Äfter removal the list is ")

print(s2)
