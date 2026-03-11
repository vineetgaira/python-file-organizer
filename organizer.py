import os
import shutil
from config import EXTENSION_MAP


def organize_folder(folder_path):

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