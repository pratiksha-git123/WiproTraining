text = input("Enter text: ")
with open ("output.txt","w") as f:
    f.write(text)
with open ("output.txt","r") as f:
    content = f.read()
    print("File content: ", content)