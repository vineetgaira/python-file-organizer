import os
import shutil 
import pathlib

folder_path=input("Enter the folder path: ")

if not os.path.exists(folder_path):
    print("Folder does not exist.")
else:
    print("\nScanning folder...\n")

    files=os.listdir(folder_path)

    for file in files:
        print(files)

