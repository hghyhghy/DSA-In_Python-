# iterarte over multiple lists simultaneously

import itertools

# creating three lists

num = [1, 2, 3]

color = ["Red", "Örange", "Yellow"]

value = [233, 332]

# using a for loop  to iterate over the three lists simultaneously

for a, b, c in zip(num, color, value):
    print(a, b, c)


# approach 2

# by using itertools

# creating three lists

num1 = [1, 2, 3]

color11 = ["Red", "Örange", "Yellow"]

value1 = [233, 332]

# using a for loop

for i, j, k in itertools.zip_longest(num1, color11, value1):
    print(i, j, k)


# approach 3

# by using enumerator

num2 = [1, 2, 3]

color2 = ["Red", "Örange", "Yellow"]

value2 = [233, 332, 211]

for i, element in enumerate(num2):
    print(element, color2[i], value2[i])
