# This code is used to filter files based on their extensions and move them into folders according to their file types.
# It defines a dictionary of extensions with their respective file types.
# It takes the user input for the folder location and checks whether the folder exists or not.
# It gets all the file names present in the folder using the os module.
# It filters the files based on their extensions and gets the respective file types from the dictionary.
# It creates a folder for each file type and moves the files into their respective folders.

import os
import sys
import shutil

# Dictionary of file extensions with their respective file types.
extension_dict = {
    "Image": ["img", "jpg", "png", "jpeg","bmp"],
    "Music": ["mp3"],
    "Document": ["doc", "docx", "pdf", "txt"],
    "Video": ["mp4", "avi", "mkv", "mov"],
    "Spreadsheet": ["xls", "xlsx", "csv"],
    "Presentation": ["ppt", "pptx"],
    "Archive": ["zip", "rar", "7z"],
    "Executable": ["exe"],
    "Database": ["sql", "sqlite"],
    "Font": ["ttf", "otf"],
}

def main():
    folder_location = user_input()
    file_name_list = get_all_file_name(folder_location)
    extension_filter(file_name_list, folder_location)

# Gets the user input for folder location and checks whether the folder exists or not.
def user_input():
    folder_location = input("Enter the folder location: ")
    folder_location = folder_location.replace("\\", "/")
    if os.path.exists(folder_location):
        return folder_location
    else:
        sys.exit("Folder not found")

# Gets all the file names present in the folder.
def get_all_file_name(folder_location):
    return os.listdir(folder_location)

# Filters the files based on their extensions and moves them into their respective folders.
def extension_filter(file_name_list, folder_location):
    for file in file_name_list:
        extension = file.split(".")[-1]
        file_type = check_file_type(extension)
        file_saving(file_type, folder_location, file)

# Moves the files into their respective folders.
def file_saving(file_type, folder_location, file_name):
    folder = str(folder_location) + "/" + str(file_type)
    file = str(folder_location) + "/" + str(file_name)
    if os.path.exists(folder):
        shutil.move(file, folder)
    else:
        os.makedirs(folder)
        shutil.move(file, folder)

# Gets the file type based on the file extension.
def check_file_type(extension):
    for key in sorted(extension_dict.keys()):
        for item in extension_dict[key]:
            if extension.lower() == item:
                return key

    return "Unknown"

main()