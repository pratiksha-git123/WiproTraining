# Use the OS Module:
# Write a program that imports the os module and uses it to:
# Print the current working directory
# Create a new directory and verify its existence.
# List all files and directories in the current directory

import os
print("Current Directory: ", os.getcwd())

os.makedirs("test_folder", exist_ok = True)
if os.path.exists("test_folder"):
    print("Directory created successfully")

print("Files and folders: ")
print(os.listdir())