#pw.py - An insecure password locker program:
PASSWORDS = {'emails':'F723982398429daosidf',
             'blog':'Wdofiajsodifjw1232',
             'luggage':'123521'}

import sys, pyperclip
if len(sys.argv)<2:
    print('Usage:python pw.py[account] - copy account password')
    sys.exit()

account = sys.argv[1]

if account in PASSWORDS :
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard')
else :
    print('Ther is no account named ' + account)