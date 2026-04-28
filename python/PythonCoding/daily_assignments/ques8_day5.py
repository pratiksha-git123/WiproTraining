numbers = [10, 20, 30, 40, 50]
try:
    index = int(input("Enter index: "))
    print("Element: ", numbers[index])
except IndexError:
    print("Error: Invalid index")
except ValueError:
    print(("Error: Please enter a valid integer"))
