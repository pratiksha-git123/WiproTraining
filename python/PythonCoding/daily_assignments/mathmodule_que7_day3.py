# Use the Math Module:
# Write a program that imports the math module and uses it to:
# Find the square root of a number.
# Calculate the sine of an angle .
# Find the greatest common divisor (GCD) of two numbers .

import math
num = float(input("Enter number: "))
angle = float(input("Enter angle in degrees: "))
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

print("Square root: ", math.sqrt(num))

print("Sine: ", math.sin(math.radians(angle)))

print("GCD: ", math.gcd(a, b))