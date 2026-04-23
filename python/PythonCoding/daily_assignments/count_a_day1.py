s = input("Enter a string: ")
count = 0
for index, char in enumerate(s):
    if char == "a":
        count += 1
print("Total a appears: ", count)