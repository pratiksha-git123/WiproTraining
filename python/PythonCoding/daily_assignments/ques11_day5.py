try:
    f = open("output.txt", "r")
except FileNotFoundError:
    print("Error: File not found")
finally:
    print("Program completed")