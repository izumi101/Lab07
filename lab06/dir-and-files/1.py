import os

def list_contents(path):
    try:
        print("Directories:")
        print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

        print("\nFiles:")
        print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

        print("\nAll Items:")
        print(os.listdir(path))
    except FileNotFoundError:
        print("The specified path does not exist.")

path = input("Enter the directory path: ")
list_contents(path)