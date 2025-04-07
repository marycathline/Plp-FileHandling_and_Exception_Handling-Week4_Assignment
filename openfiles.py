# File Read & Write Challenge 

# Defining  file paths
file_path = 'example.txt'  
new_file_path = 'modified_example.txt'  

# Opening the file in read mode and read its content
with open(file_path, 'r') as file:
    content = file.read()


modified_content = content + "This is a new one in existing file."

# Writing the modified content to a new file
with open(new_file_path, 'w') as new_file:
    new_file.write(modified_content)

print("File has been modified and saved.")


    