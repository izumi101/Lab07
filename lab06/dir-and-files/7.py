import shutil

def copy_file(source, destination):
    try:
        shutil.copy(source, destination)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Source file not found.")

source = input("Enter the source file path: ")
destination = input("Enter the destination file path: ")
copy_file(source, destination)