#! usr/bin/env python3
# countodwn.py - A simple countdown script. 

import time, subprocess

print('Input timer length (seconds):')
timeLeft = int(input())  
print('Timer Starting for %s seconds' % (timeLeft))
#TODO: ask for time input 
while timeLeft > 0: 
    print(timeLeft, end='\n')
    time.sleep(1)
    timeLeft = timeLeft-1

# At the end of the countdown, play a sound file. 
# subprocess.Popen(['open', 'alarm.wav']) Commented out because annoying for testing. 
print('Time is up')