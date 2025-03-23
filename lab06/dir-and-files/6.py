import string

def create_files():
    for letter in string.ascii_uppercase:
        file_name = f"{letter}.txt"
        with open(file_name, 'w') as file:
            file.write(f"This is file {file_name}\n")
    print("26 files created successfully.")

create_files()