﻿# file_organizer_bot

# README

This code is used to filter files based on their extensions and move them into folders according to their file types. The script defines a dictionary of extensions with their respective file types. It takes the user input for the folder location and checks whether the folder exists or not. It gets all the file names present in the folder using the `os` module. It filters the files based on their extensions and gets the respective file types from the dictionary. It creates a folder for each file type and moves the files into their respective folders.

## Usage

To use this script, you need to have Python installed on your system. Follow these steps to use the script:

1. Open the command prompt or terminal on your system.
2. Navigate to the directory where the script is saved.
3. Type `python script_name.py` and press Enter. Replace `script_name.py` with the name of the actual script file.
4. Enter the folder location when prompted. Use forward slashes (`/`) to separate directories.
5. Press Enter to run the script.

The script will filter the files based on their extensions and move them into their respective folders.

## Notes

* The script assumes that the files are present in a single folder. If you want to filter files from multiple folders, you will have to modify the script accordingly.
* The script may not work if there are files with extensions that are not present in the dictionary.
* The script will not overwrite any existing files with the same name in the destination folders.
* The script has been tested on Python 3.5 and above.
