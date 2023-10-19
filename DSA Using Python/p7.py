from operator import itemgetter

# accessing front and rear elements in python tuples

# creating a tuple first

testtup = (10, 3, 19, 30, 6)

print("The original tuple is ", str(testtup))

# accessing the front and rear elements

res = (testtup[0], testtup[-1])

print(f"The front and rear elements of the tuple {testtup} are ", str(res))

# approach 2

# by using inbuilt function itemgetter

# creating a tuple first

test = (10, 3, 19, 30, 6, 8)

print("The original tuple is ", str(test))

# stroring the value in a temporary variable

temp = itemgetter(0, -1)(test)

# printing the elements

print(f"The front and rear elements of the tuple {test} is ", str(temp))

# approach 3

# creating a tuple


t = ("Subham", 3, 19, 30, 6, "Shreyoshi ")

# storing the values in the temporary variable

t1 = (t[0], t[len(t) - 1])

print(f"The values of the front and rear elements in the tuple {t} is ", str(t1))

# printing the second last element from the tuple

temp1 = (t[0], t[len(t) - 2])

print(
    f"The values of the front and the 2nd last element  elements in the tuple {t} is ",
    str(temp1),
)


# approach  4

# using tuple  constructor


# creating a  tuple first


t0 = ("Subham", 3, 19, 30, 6, "Shreyoshi ")

front = t0[0]

rear = t0[-1]

tempu = tuple([front]) + tuple([rear])


print("The front and rear elements of the tuple is ", str(tempu))
