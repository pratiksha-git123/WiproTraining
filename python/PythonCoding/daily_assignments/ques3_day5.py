with open ("output.txt", "r") as src:
    data = src.read()
with open ("destination.txt", "w") as dest:
    dest.write(data)
print("Content copied successfully")
