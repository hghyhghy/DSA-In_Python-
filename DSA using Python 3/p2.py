# creating a list by a given


# creating a function


def oflist(r1, r2):
    return [item for item in range(r1, r2 + 1)]


# driver code

r1 = -1

r2 = 1

print(oflist(r1, r2))

# approach 2

# by using if else and while loop


def ofl(r, r0):
    # running a if else loop

    if r == r0:
        return r
    else:
        temp = []  # creating a temporary list to store data

        while r < r0 + 1:
            temp.append(r)

            r = r + 1  # incrementing the value

    return temp


r = -1

r0 = 1

print(ofl(r, r0))


# approach 3

# by using list()

# creating a function


def ofcreate(s, s1):
    return list(range(s, s1 + 1))


s = -2
s1 = 2

print(ofcreate(s, s1))
