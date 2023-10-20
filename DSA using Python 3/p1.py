# finding the odd values from the list

# creating an empty list

oddsqr = []

# using an for loop to iterate over 1 to 11

for i in range(1, 11):
    if i % 2 != 0:
        oddsqr.append(i**2)  # taking the square of those values

print("The square of odd numbers from the range 1 to 11 is ", oddsqr)
