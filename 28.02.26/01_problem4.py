import os

# Specify the directory path
path = "/jokes.py"

try:
    # Get list of files and directories
    contents = os.listdir(path)  # os.listdir() lists items in the directory :contentReference[oaicite:1]{index=1}

    print(f"Contents of directory '{path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")