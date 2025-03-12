''' Original isPhoneNumber program while going through chapter
def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
'''


''' 2nd program while learning about reducing the length of regexes
import re

regex_obj = re.compile(r'\d{3}-\d{3}-\d{4}')
match_obj = regex_obj.search('Hi! My phone number is 243-342-6543! Have a great day!')
print('Your phone number: ' + match_obj.group())
'''


''' Actual coding project
Phone number and email address extractor

What will the program do?
Get the text off the clipboard
Find all phone numbers and email addresses in the text
Paste them onto the clipboard

How will this work in code?
Will need to use pyperclip module to copy and paste strings
Create two regexes, one for phone numbers, one for email addresses
Find all matches of both regexes
Format matched strings into a single string to paste
Display some kind of message if no matches were found
'''

# JK we gonna do it in another doc.