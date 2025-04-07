
# It attempts to open a file and read its content, handling the case where the file does not exist or cant be read.
# File Read & Write Challenge
file_path = input("Enter the filename: ")  # Prompt the user for a filename
try:
    # Attempt to open the file in read mode
    with open(file_path, 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
   print(f"The file '{file_path}' does not exist.")

except IOError:
    print(f"The file '{file_path}' can't be read.")
