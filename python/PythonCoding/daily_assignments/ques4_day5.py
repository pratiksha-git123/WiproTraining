text = input("Enter text to append: ")
with open("log.txt", "a") as f:
    f.write(text + "\n")
with open("log.txt", "r") as f:
    print("Updated file content: ")
    print(f.read())
