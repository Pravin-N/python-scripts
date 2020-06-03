#! Python3
# Write a program that walks through a folder tree and searches for files with a certain file extension
# (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.

#import necessary modules to be used.

import os, shutil
from pathlib import Path

# create function that moves user specified files from the user specified folder to a user specified new folder.

def movefile(folder, filetype, newfolder):
    if not os.path.exists(newfolder):
        os.mkdir(newfolder)
    if os.path.exists(folder):
        for root, subfolder, files in os.walk(folder):
            print(f"Searching {filetype} in {root}")
            for file in files:
                if file.endswith(filetype):
                    print(str(os.path.join(root, file)) + ' moved to ' + (newfolder))
                    shutil.copy(os.path.join(root, file),  newfolder)
                else:
                    continue

# Request input from user from the folder the folders need to be moved.

oldfolderpath = input(r'Please enter the full path of the folder to be moved: ')
print(oldfolderpath)

# Request input from user for the type of files need to moved.

typeoffile = '.' + str(input(r'Please enter the extention of the file to be moved (pdf, txt, doc, jpg, docx, py): '))
print(typeoffile)

# Request the folder name that would be saved on the desktop.

newfoldername = str(Path(r'C:\Users\ACE\Desktop', str(input(r'Enter the name of the folder to where the files will be moved. This will be on the desktop: '))))
print(newfoldername)

movefile(oldfolderpath, typeoffile, newfoldername)







