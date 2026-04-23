# Do the following in sequence and record the results in a single program
# Create a tuple with the names of 3 different cities you’d like to visit. Print the tuple.:
# Access and print the first and last elements of the tuple.:
# Create another tuple with 2 more cities. Concatenate both tuples and print the result.
# Try changing one element of the tuple. What happens?
# Unpack the elements of the tuple into separate variables and print them.


cities = ("Delhi", "Mumbai", "Bangalore")
print("Original tuple: ", cities)

print("First city: ", cities[0])
print("Last city: ", cities[-1])

more_cities = ("Chennai", "Kolkata")
all_cities = cities + more_cities
print("After concatenation: ", all_cities)

print("Tuples are immutable cannot be changed")

city1, city2, city3 = cities
print("Unpacked values: ")
print(city1)
print(city2)
print(city3)