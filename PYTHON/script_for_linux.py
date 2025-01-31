# Introductory Python Code
import os,sys

print("Hello, Python Enthusiast!")
# 3. Simple I/O
user_name = input("What's your name? ")
print(f"Welcome, {user_name}!\n\n\n\n\n")

# 7. File Input/Output
# Writing to a file
print(f"Writing to a file >> example.txt\n\n\n\n\n")

with open("example.txt", "w") as file:
    file.write("Hello!\n")
    file.write("This is an example file.\n")
    file.write("You can now close this!")

# List files in the current directory
print("These files are in current directory:", os.listdir("."))
print("Below is an absolute path of every file ...")
for f in os.listdir("."):
    print(os.path.abspath(f))
