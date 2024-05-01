# This is where the script to generate a .md file containing the appropriate question to ask in a community.

import os
import time

# Get the current working directory
cwd = os.getcwd()
print(f"Current working directory: {cwd}")

file_name = input("What is the name of the file you want to create? ")
print("[*] Creating file...")
file_path = cwd + "/" + file_name + ".md"   # Create an empty file
time.sleep(2)
print(f"[*] Created file: {file_path}")
print("[*] Creating the structure of the file...")

with open(file_path, "w") as file:
    file.write("# Question\n")
    file.write("What is the question you want to ask?\n\n\n")
    file.write("## Context\n")
    file.write("What is the context of the question?\n\n\n")
    file.write("## Possible Answers\n")
    file.write("What are the possible answers to the question?\n\n\n")
    file.write("## Additional Information\n")
    file.write("Any additional information to provide?\n\n\n")
    file.write("## Tags\n")
    file.write("What are the tags for the question?\n\n\n")
    file.write("## Related Questions\n")
    file.write("Are there any related questions to this question?\n\n\n")
    file.write("## References\n")
    file.write("Any references to include?\n\n\n")
    file.write("## Notes\n")
    file.write("Any notes to include?\n\n\n")
    file.write("## Conclusion\n")
    file.write("What is the conclusion of the question?\n\n\n")
    file.write("## Next Steps\n")
    file.write("What are the next steps?\n\n\n")
    file.write("## Acknowledgements\n")
    file.write("Any acknowledgements to include?\n\n\n")
    file.close()

time.sleep(2)
print("[*] Finished writing to file.")
time.sleep(2)
print("--------------------------------------------------------")
time.sleep(1)
print("[*] Please open the file '{}.md'' to begin.".format(file_name))
time.sleep(2)
print("[!] Exiting.")
time.sleep(1)
