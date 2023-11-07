#install: "pip install pyshorteners"

import pyshorteners

userUrlInput = input("Enter URL for Shortening: \n")
result = pyshorteners.Shortener().tinyurl.short(userUrlInput)

print(f'Before {userUrlInput} ')
print('After ', result)
