# Write a user-defined function "find_largest(a, b, c)" that takes three numbers as
# arguments and returns the largest of the three. Use the function in a program to find and
# print the largest of three given numbers.
def find_largest(a,b,c):
    return max(a,b,c)
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
print("Largest num: ", find_largest(a,b,c))