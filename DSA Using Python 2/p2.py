# formatting the string by using .format()  method

# formatting a string in a default order

string1 = "{}{}{}".format("Subham", "Loves", "Shreyoshi")

print("The string in a default order is ")

print(string1)

# formatting a string by using position

s1 = "{1}{0}{2}".format("Love", "Subham", "Shreyoshi")

print("The  string formatted in a positional order is ")

print(s1)

# formatting the  string by keyword formatting

s2 = "{0}{l}{s1}".format("Subham", l="Loves", s1="Shreyoshi")

print("The string formatted in a order of keyword is  ")

print(s2)
