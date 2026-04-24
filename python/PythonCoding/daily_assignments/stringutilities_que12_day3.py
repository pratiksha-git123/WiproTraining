# Create a Package for String Utilities:
# Create a package called string_utils with two modules: string_operations.py and
# string_validations.py.
# In string_operations.py, define functions for reversing a string, converting a string to
# uppercase, and finding the length of a string.
# In string_validations.py, define functions to check if a string is a palindrome and if it
# contains only alphabetic characters.
# Write a program that imports and uses these functions from the string_utils package.

from string_utils.string_operations import reverse_string, to_uppercase, string_length
from string_utils.string_validations import is_palindrome, is_alphabetic

text = "madam"

print("Original text: ", text)
print("Reversed: ", reverse_string(text))
print("Uppercase: ", to_uppercase(text))
print("Length: ", string_length(text))

print("Is Palindrome: ", is_palindrome(text))
print("Is Alphabetic: ",is_alphabetic(text))