from organizer import organize_folder
from utlis import folder_exists


folder_path = input("Enter folder path: ")

if not folder_exists(folder_path):
    print("Folder does not exist")

else:
    print("\nScanning folder...\n")
    organize_folder(folder_path)