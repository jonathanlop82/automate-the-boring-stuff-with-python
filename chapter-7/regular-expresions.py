import re

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

print('Is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))

message = 'Call me at (415)-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')

### Using Regex
# Create a regex object
phoneNumRegex = re.compile(r'(\(\d\d\d\))-(\d\d\d-\d\d\d\d)')
# Pass the string you want to search, in to the regex object search() method
mo = phoneNumRegex.search(message)
# Call the match object group() method to return a string
print('Phone number found: ' + mo.group() )
print('group 1: ' + mo.group(1) )
print('group 2: ' + mo.group(2) )
print('group 0: ' + mo.group(0) )
print(mo.groups() )
