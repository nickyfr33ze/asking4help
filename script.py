# This is where the script to generate a .md file containing the appropriate question to ask in a community.

import os

# Get the current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

file_name = input("What is the name of the file you want to create? ")

file_path = cwd + "/" + file_name + ".md"

# Create an empty file
with open(file_path, "w") as file:
    pass

print(f"Created file: {file_path}")
