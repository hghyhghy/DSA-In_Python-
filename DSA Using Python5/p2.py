#  symmetric difference between two sets in python

# creating two sets

s1 = {1, 2, 3, 4}

s2 = {2, 3, 4, 5}

print(f"The symmetric difference between sets {s1} and {s2} is")

print(s1.symmetric_difference(s2))


s0 = {1, 2, 30, 4}

s = {2, 3, 4, 5}

print(f"The symmetric differnce  sets {s0} and {s} is")

result = s0.symmetric_difference(s)

print(result)


# by using ^ operator


# creating two lists

l = {3, 4, 5, 6, 7}

l1 = {4, 5, 6, 7, 8}

print(f"The symmetric difference betwen sets {l} and {l1} is ")

print(l ^ l1)
