# Create a set of 5 unique colors. Print the set.
# Add a new color to the set, then try removing an existing color. Print the updated set.
# Create another set with 3 different colors. Find the intersection, union, and difference
# between both sets.
# Check if a specific color is in the set and print the result.
# Convert a list of fruits (with some duplicates) into a set and print the unique fruits.

data = {"name" : "Pratiksha", "age" : 22, "hobby" : "cooking"}

print("Original dictionary: ", data)

print("Name: ", data["name"])

data["favorite_food"] = "pizza"
data["hobby"] = "travelling"

print("Updated dictionary: ", data)

print("Keys: ", data.keys())
print("Values: ", data.values())

data.pop("age")

print("After removing age: ", data)