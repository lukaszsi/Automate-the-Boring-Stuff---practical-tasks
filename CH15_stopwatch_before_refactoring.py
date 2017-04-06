#! python3
# stopwatch.py - A simple stopwatch program.
import time, pyperclip

# Display the program's instructions.
print('Press ENTER to begin. Afterwards, press ENTER to "click" the \
stopwatch.Press Ctrl-C to quit.')
input()                     # press Enter to begin.
print('Started.')
startTime = time.time()     # get the first lap's start time
lastTime = startTime
lapNum = 1
lapList = []
# Start tracking the lap times.
try:
    while True:
        input()
        lapTime = str(round(time.time() - lastTime, 2)).rjust(5)
        totalTime = str(round(time.time() - startTime, 2)).rjust(5)
        lapNumStr = str(lapNum).rjust(2)
        lapStr = 'Lap #%s: %s (%s)' % (lapNumStr, totalTime, lapTime)
        print(lapStr, end='')
        lapList.append(lapStr)
        pyperclip.copy('\n'.join(lapList))
        lapNum += 1
        lastTime = time.time()  # reset the last lap time
except KeyboardInterrupt:
    # Handle the Ctr-C exception to keep its error message from displaying.
    print('\nDone')
