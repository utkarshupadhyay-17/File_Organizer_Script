# Assignment 1: File Organizer Script
#Write a Python script that organizes files in a folder by file type.

import os
import shutil

# Define file type categories
FILE_CATEGORIES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
    'Music': ['.mp3', '.wav', '.aac', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
    'Scripts': ['.py', '.js', '.html', '.css', '.java', '.cpp'],
    'Executables': ['.exe', '.msi'],
    'Others': []
}
#Function to Determine Category of a File
def get_category(extension):
    for category, extensions in FILE_CATEGORIES.items():
        if extension.lower() in extensions:
            return category
    return 'Others'

def organize_files(directory):
    if not os.path.isdir(directory):
        print("Invalid directory path!")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            _, extension = os.path.splitext(filename)
            category = get_category(extension)
            category_path = os.path.join(directory, category)

            if not os.path.exists(category_path):
                os.makedirs(category_path)

            new_path = os.path.join(category_path, filename)
            shutil.move(file_path, new_path)
            print(f"Moved: {filename} ➜ {category}/")

if __name__ == "__main__":
    target_folder = input("Enter the path of the folder to organize: ").strip()
    organize_files(target_folder)
    print("File organization complete.")
