# checking subset or superset

# creating a function to check that


def ofsubset():
    set1 = {1, 2, 3, 4, 5, 6}

    set2 = {2, 3, 4}

    myset = set2.issubset(set1)

    print(myset)


# creating a function to cheeck issuperset


def ofsuperset():
    s1 = {1, 2, 3, 4, 5}

    s2 = {2, 3, 4}

    m1 = s1.issuperset(s2)

    print(m1)


ofsubset()

ofsuperset()
