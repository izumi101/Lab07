import os

def check_path(path):
    if os.path.exists(path):
        print(f"Path exists: {path}")
        print(f"Directory: {os.path.dirname(path)}")
        print(f"Filename: {os.path.basename(path)}")
    else:
        print("The specified path does not exist.")

path = input("Enter the path to check: ")
check_path(path)