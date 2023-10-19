# slicing of tuples

# creating a tuple first

tus = "SUBHAMANDSHREYOSHI"

print("Before operation the original tuple is ")

print(tus)

# removal of first element from the tuple

print(f"After  removing the first element from the tuple {tus} it becomes ")

print(
    tus[1 : len(tus)]
)  # that takes characters from index 1 to  the length of the tuple

# reversing the tuple

print(f"After  reversing the tuple {tus} it becomes ")

print(tus[::-1])

# printing elements of a range

print(f"After  printing  the tuple {tus} from a range  it becomes ")

print(tus[4:9])
