#! usr/bin/env python3
# bulletPOintAdder.py - adds wikepedia bulletpoints to start
# of each line of text on the clipboard

import pyperclip
text = pyperclip.paste()

# Separate Lines and add starts
lines = text.split('\n')
for i in range(len(lines)):  #  loop through all indexes in the "lines" list
    # add star to the start of each string in the lines list
    lines[i] = '* ' + lines[i]
text='\n'.join(lines)
pyperclip.copy(text)