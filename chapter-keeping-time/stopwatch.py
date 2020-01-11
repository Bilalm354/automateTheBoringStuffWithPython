"""
What the program will do:
1. Track the amount of time elapsed between presses of the ENTER key, with each key press startimg a mew "lap" on the timer.
2. Print the lap number, total time, and lap time.

This menas your code will need to do the following:

1. Find the current time by calling time.time() and store it as a timestamp at the start of the program as well as at the start of each lap.
2. Keep a lap counter and imcrement it every time the user presses ENTER.
3. Calculate the elapsed time by subtracting timestamps.
4. Handle the KeyboardInterrupt exception so the iser can press ctrl c to quit.


"""
#! /usr/bin/env python3
# stopwatch.py - A simple stopwatch program.

import time

# Display the program's instructions.
print ('Press ENTER to begin. Afterward, press ENTER tp "click the stopwatch. Press CTRL+C tp quit.')
input()
print('Started.')
startTime=time.time()
lastTime=startTime
lapNum=1

# TODO: Start tracking the lap times.

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime,2)
        totalTime = round(time.time() - startTime,2)
        print('Lap #%s: %s(%s)' %(lapNum, totalTime,lapTime), end='')
        lapNum+=1
        lastTime = time.time() # reset the last lap time
except KeyboardInterrupt:
    # Hande the Ctrl-C exception to keep its error message from displaying.
    print('\nDone')

