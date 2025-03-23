import os

def delete_file(file_path):
    if os.path.exists(file_path):
        if os.access(file_path, os.W_OK):
            os.remove(file_path)
            print("File deleted successfully.")
        else:
            print("No write permission to delete the file.")
    else:
        print("File does not exist.")

file_path = input("Enter the file path to delete: ")
delete_file(file_path)