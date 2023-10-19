# deleting a tuple

# creating a tuple first

tus = "SUBHAMANDSHREYOSHI"

print(tus)

del tus

# print(tus)  # it will give an error


#  creating  a tuple from string  and  list

testlist = ["Messi", "Is"]

teststr = "Great"

# printing the original list and string before operation

print("The original list before operation  is ", str(testlist))

print("The original string  before operation  is ", teststr)

# operation

rest = tuple(testlist + [teststr])

print("The tuple after operatio is ", str(rest))

# approach 2

# creating a tuple first


testlist1 = ["Messi", "Is"]

teststr1 = "A Legend"


print("The original list before operation  is ", str(testlist1))

print("The original string  before operation  is ", teststr1)

#  doing the operation by using tuple conversion

res = tuple(testlist1) + (teststr1,)

print("The tuple after operation is ", str(res))

# approach 3

# creating a tuple first


t = ["Messi", "Is"]

t1 = "A Legend"

newlist = t.copy()

newlist.append(t1)

# creating a new tuple

newtups = tuple(newlist)

print("The modified tuple is ", newtups)
