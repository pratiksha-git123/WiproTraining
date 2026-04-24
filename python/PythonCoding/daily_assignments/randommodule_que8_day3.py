# Use the Random Module:
# Write a program that imports the random module and uses it to:
# Generate and print a random integer between 1 and 100.
# Create a list of random numbers  and print the list.
# Shuffle a list of numbers and print the shuffled list.


import random
num = random.randint(1,100)
print("Random number: ", num)

rand_list = []
for i in range(5):
    n = random.randint(1, 100)
    rand_list.append(n)
print("Random list: ", rand_list)

numbers = [1,2,3,4,5,6,7,8,9]
random.shuffle(numbers)
print("Shuffled list: ", numbers)
