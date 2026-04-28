filename = input("Enter filename: ")
try:
    with open (filename, "r") as f:
        print("File Content: ")
        print(f.read())
except FileNotFoundError:
    print("Error: File does not exist")