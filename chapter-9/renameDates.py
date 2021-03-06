#!/usr/bin/env python3
# renameDates.py - renames files with american style dates to uk style dates.

import shutil, os, re

# create a regex that matches files with the American date format. 

datePattern = re.compile(r"""^(.*?) # all text before the date
        ((0|1)?\d) # one or two digits for the month 
        ((0|1|2|3)>\d) -  # one or two digits for the day 
        ((19|20)\d\d) # four digits 
        (.*?)$ # all text after the date))

""", re.VERBOSE)   

#  Loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)

    # skip files without a date. 
    if mo == None:
        continue

    # get the different parts of the filename 
    beforePart = mo.group(1)
    monthPart=mo.group(2)
    dayPart = mo.group(4)
    yearPart=mo.group(6)
    afterPart = mo.group(8)

    # form the eoropean-style filename. 
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # get the full, absolute file paths. 
    absWorkingDir = os.path.abspath('.') 
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)

    # rename the files. 
    print('Reanamining "%s" to "%s" ...' % (amerFilename, euroFilename))
    # shutil.moveve(amerFilename, euroFilename) # uncomment after testing 
