# creating tuple with mixed datatype


tup = (
    "Subham",
    6,
    "Love",
    "Shreyoshi",
    4,
    5,
)

print("The tuple with mixed datatype is ")

print(tup)

# creating tuple with nested tuple

t1 = (1, 2, 8, 0, 9)

t2 = ("Python", "Pymongo", "Tkinter")

t3 = (t1, t2)

print("The tuple with nested tuple is ")

print(t3)

# creating  a tuple with repetition
tups = ("Subham love shreyoshi") * 3

print("Tuple with repetition is ")

print(tups)


# printing the tuple with the help of for loops

t = "Shreyoshi"

# taking the range

n = 3

for i in range(int(n)):
    t = (t,)

    print(t)
