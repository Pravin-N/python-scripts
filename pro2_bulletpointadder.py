#! python3
# Bullet point adder. py - Adds bullets to start of the text of each line.

import pyperclip
text = pyperclip.paste()

#TODO: Seperate lines and add stars

# Seperate lines and add stars
lines = text.split('\n')

for i in range(len(lines)): # Loop through all indexes in the lines list.
    lines[i] = '* ' + lines[i] #add star to each string in 'lines' list

text = '\n'.join(lines)

pyperclip.copy(text)
