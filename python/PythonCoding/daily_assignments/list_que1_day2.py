# Do the following in sequence and record the results in a single program
# Create a list with 5 different types of fruits. Print the list.
# Add two more fruits to the list, then remove one fruit from it. Print the updated list.
# Access the second and fourth fruits in the list. Print them.
# Slice the list to get the first three fruits and print the result.
# Find and print the length of your list.


fruits = ["apple", "banana", "mango", "orange", "grapes"]
print("Original list: ", fruits)

fruits.append("pineapple")
fruits.append("kiwi")
fruits.remove("banana")
print("Updated list: ", fruits)

print("Second fruit: ", fruits[1])
print("Fourth fruit: ", fruits[3])

print("First three fruits: ", fruits[:3])

print("Length of list: ", len(fruits))