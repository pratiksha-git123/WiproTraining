# Create a set of 5 unique colors. Print the set.
# Add a new color to the set, then try removing an existing color. Print the updated set.
# Create another set with 3 different colors. Find the intersection, union, and difference
# between both sets.
# Check if a specific color is in the set and print the result.
# Convert a list of fruits (with some duplicates) into a set and print the unique fruits.


colors = {"red", "blue", "green", "yellow", "black"}
print("Original set: ", colors)

colors.add("white")
colors.remove("black")
print("Updated set: ", colors)

more_colors = {"pink", "orange", "blue"}

print("Union: ", colors.union(more_colors))
print("Intersection: ", colors.intersection(more_colors))
print("Difference: ", colors.difference(more_colors))

check_color = "red"
if check_color in colors:
    print(check_color, "is present in the set")
else:
    print(check_color, "is NOT present in the set")

fruits_list = ["apple", "banana", "apple", "mango", "banana"]
unique_fruits = set(fruits_list)
print("Unique fruits: ", unique_fruits)