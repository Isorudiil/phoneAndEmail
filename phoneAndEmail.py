#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# Phone number regex
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # separator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension       
    )''', re.VERBOSE)

# Email address regex
emailRegex = re.compile(r'''(
    \w+               # username
    @                               # @ symbol
    \w+                  # domain name
    \.\w+               # dot-something
)''', re.VERBOSE)

# Find matches in clipboard text
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = groups[1] + '-' + groups[3] + '-' + groups[5]
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups)

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copies to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found')