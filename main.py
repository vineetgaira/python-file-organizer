import os
import shutil

EXTENSION_MAP = {
    "jpg": "Images",
    "png": "Images",
    "jpeg": "Images",
    "gif": "Images",
    "mp4": "Videos",
    "mkv": "Videos",
    "avi": "Videos",
    "pdf": "Documents",
    "docx": "Documents",
    "txt": "Documents",
    "zip": "Archives",
    "rar": "Archives"
}

folder_path = input("Enter folder path: ")

if not os.path.exists(folder_path):
    print("Folder does not exist")

else:

    files = os.listdir(folder_path)

    for file in files:

        full_path = os.path.join(folder_path, file)

        if not os.path.isfile(full_path):
            continue

        extension = os.path.splitext(file)[1].lower().replace(".", "")

        category = EXTENSION_MAP.get(extension, "Others")

        category_folder = os.path.join(folder_path, category)

        os.makedirs(category_folder, exist_ok=True)

        shutil.move(full_path, os.path.join(category_folder, file))

        print(f"Moved {file} -> {category}")