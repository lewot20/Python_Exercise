import pyautogui

print('Press Ctrl-C to quit.')
# Todo: Get and print the mouse coordinates.

try:
    while True:
        # Todo : Get and print the mouse coordinates.
        x, y = pyautogui.position()
        positionStr = 'X:' + str(x).rjust(4) + 'Y:' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b'*len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\nDone.')