# fincding the length of a list in python

# creating a list first

l = [1, 3, 5, 7, 9]

print("The original list is ", str(l))

# initializing the counter

counter = 0

# using a for loop

# to iterate

for i in l:
    if i % 2 != 0:  # checking   wheather it is odd or even
        counter += 1

print(f"The length of the list {l} is ", counter)


# approach 2

# by using len()

l2 = [2, 4, 3, 5, 4]

print("The length of the list is ")

print(len(l2))


# approach 3

# by creating a function


def ofcount(list1):
    count = 0

    for i in list1:
        count += 1

    return count


list1 = [6, 5, 4, 3, 9, 2, 0, 1]

print(ofcount(list1))


# approach 4

# by using enumerator


# creating another list

li = ["subham", "loves", "Shreyoshi", 45, 67, 32]

# creating an  variable to count the number and initializing th variable with  0

s = 0

for i, n in enumerate(li):
    s = s + 1  # incrementing the value of s

print(s)
