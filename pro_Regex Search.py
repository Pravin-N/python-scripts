#! python3
#! Write a program that opens all .txt files in a folder and searches for any line that matches a user-supplied regular expression.
# The results should be printed to the screen.

import re, os, glob
from pathlib import Path
# user supplied regex pattern
regexinput = '.*' + str(input('Please enter search criteria: ')) + '.*'

print(F"You are searching for: {regexinput}")


#Open all .txt files in a folder.

os.chdir(r'C:\Users\ACE\Desktop\Python')

p = Path.cwd()

for file in list(p.glob('*.txt')):
    readfile = open(file)
    content = readfile.readlines()
    for line in content:
        regexsearch = re.search(regexinput, line)
        if regexsearch is not None:
            print(regexsearch.group())
    readfile.close()





                        
