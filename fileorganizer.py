import os
import shutil

# Folder to organize
source_folder = input("Enter folder path: ")

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Docs": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov"]
}

# Create folders if they don't exist
for folder in file_types:
    os.makedirs(os.path.join(source_folder, folder), exist_ok=True)

# Organize files
for file in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file)

    if os.path.isfile(file_path):
        _, extension = os.path.splitext(file)

        for folder, extensions in file_types.items():
            if extension.lower() in extensions:
                destination = os.path.join(source_folder, folder, file)
                shutil.move(file_path, destination)
                print(f"Moved: {file} -> {folder}")
                break

print("File organization completed!")