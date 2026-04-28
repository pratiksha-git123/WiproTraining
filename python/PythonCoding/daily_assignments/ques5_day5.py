num = input("Enter a number: ")
try:
    value = int(num)
    print("Integer: ", value)
except ValueError:
    print("Error: Invalid number entered")