def write_list_to_file(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(f"{item}\n")
    print("List written to file successfully.")

data = ["apple", "banana", "cherry", "date"]
file_path = input("Enter the file path to save the list: ")
write_list_to_file(file_path, data)