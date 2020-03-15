#! python3
#phoneandemail.py - finds phone numbers and email adresses on the clipboard

import pyperclip
import re

phoneregex = re.compile(r'''(
(\d{3}|\(\d{3})?         #area code
(\s|-|\.)?                      #separator
(\d{3})                         #first 3 digits
(\s|-|\.)                       #separator
(\d{4})                         #first 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  #extension
)''', re.VERBOSE)

#TODO : Create email regex
emailregex = re.compile(r'''(
[a-zA-Z0-9._%+-] +
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)

#TODO : Find matches in clipboard text
text = str(pyperclip.paste())

matches=[]
for groups in phoneregex.findall(text):
    phonenum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phonenum += ' x' + groups[8]
    matches.append(phonenum)
for groups in emailregex.findall(text):
    matches.append(groups[0])

# TODO : clipboard 로
if len(matches) >0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email address found.')


#TODO : Copy results to the clip board

