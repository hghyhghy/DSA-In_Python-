# reversing a string   by using a  function

# creating a function first


def ofreverse(string):
    # creating an empty string to store values

    st = ""

    # using a for loop

    for i in string:
        st = i + st

    return st


string = "PROGRAMMING"

print("The original string is ")

print(string)

print(f"The reversed version of the string {string } is ")

print(ofreverse(string))


# approach 2

# by using if else loop

# creating a function


def reverse(s):
    # setting the if else loop

    if len(s) == 0:
        return s

    else:
        return reverse(s[1:]) + s[0]


s = "PROGRAMMING"

print("The original string is ")

print(s)

print(f"The reversed version of the string {s } is ")

print(reverse(s))


# approach 3

# by  making the string to the list

# creating a function


def reversing(s1):
    # making the string a list

    s1 = list(s1)

    s1.reverse()

    return " ".join(s1)


s1 = "SHREYOSHI"

print("The original string is ")

print(s1)

print(f"The reversed version of the string {s1} is ")

print(reversing(s1))
