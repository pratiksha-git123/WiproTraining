# Create and Use a Custom Package:
# Create a package called my_math with two modules: arithmetic.py and geometry.py.
# In arithmetic.py, define functions for addition, subtraction, multiplication, and division.
# In geometry.py, define functions to calculate the area of a circle and the area of a
# rectangle.
# Write a program that imports these functions from the my_math package and uses
# them to perform various calculations.


from daily_assignments.my_math.arithmetic import addition, multiplication, subtraction, division

from my_math.arithmetic import addition, subtraction, multiplication, division
from my_math.geometry import area_circle, area_rectangle

print("Addition: ", addition(10, 5))
print("Subtraction: ", subtraction(10, 5))
print("Multiplication: ", multiplication(10, 5))
print("Division: ", division(10, 5))

print("Area of circle: ", area_circle(7))
print("Area of rectangle: ", area_rectangle(10, 5))

