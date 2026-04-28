class NegativeNumberError(Exception):
    pass
try:
    num = int(input("Enter a positive number: "))
    if num < 0:
        raise NegativeNumberError("Negative number entered")
    print("Valid number: ", num)
except NegativeNumberError as e :
    print("Error: ", e)
except ValueError:
    print("Error: Invalid input")