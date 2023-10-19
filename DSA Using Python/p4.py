# accessing the elements of tuple by using python


tup = ("Subham", "Love", "Shreyoshi")

print("The first element of the tuple is ")

print(tup[0])

tup1 = ("Subham", "Love", "Shreyoshi")


# this line unpack values of the tuple

a, b, c = tup1

print("The values of the tuple after unpacking is :")

print(a)

print(b)

print(c)


# concatenation of two tuples

t1 = ("Subham", "Love", "Shreyoshi")


t2 = (2, 3, 4, 5, 6)

print("Before concatenation the tuple is ")

print(t1)

print("Before concatenation the tuple is ")

print(t2)

print("After concatenation the tuple becomes ")

t3 = t1 + t2

print(t3)
