import os
import shutil 
import pathlib

FILE_CATEGORIES = {
    "Images": ["jpg", "png", "jpeg", "gif"],
    "Videos": ["mp4", "mkv", "avi"],
    "Documents": ["pdf", "docx", "txt"],
    "Archives": ["zip", "rar"]
}

folder_path=input("Enter the folder path: ")

    

if not os.path.exists(folder_path):
    print("Folder does not exist.")
else:
    print("\nScanning folder...\n")

    files=os.listdir(folder_path)

    for item in files:

        full_path=os.path.join(folder_path, item)
        
        if not os.path.exists(full_path):   
            continue


        if os.path.isfile(full_path):
            
            extension=item.split(".")[-1].lower()
            
            catogory_found=False

            for category, extensions in FILE_CATEGORIES.items():

                if extension in extensions:

                    catogory_folder=os.path.join(folder_path,category)

                    os.makedirs(catogory_folder,exist_ok=True)

                    shutil.move(full_path, os.path.join(catogory_folder,item)) 

                    print(f"Moved {item} -> {category}")   

                    catogory_found=True    

                    break   

            if not catogory_found:

                other_folder=os.path.join(folder_path,"Others")

                os.makedirs(other_folder, exist_ok=True)

                shutil.move(full_path, os.path.join(other_folder,item))

                print(f"Moved {item} -> Others")






