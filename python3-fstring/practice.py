# Python 3.6
import sys
import decimal
from datetime import datetime

name = "Urian"
age = 29

print(f'{name} is {age} years old')         # Urian is 29 years old
print(F'{name!r} was here')                 # 'Urian' was here
print(f'{{age}} is a number')               # {age} is a number

# Backslashes are not allowed in format expressions --> SyntaxError
# To include a value with a backslash, create a temporary variable
newline = '\n'
print(f'newline: {newline}')                # newline:

# nested fields
width = 8
precision = 3
num = decimal.Decimal("3.14")
print(f'result: {num:{width}.{precision}}') # result:     3.14

# time
today = datetime.today()
print(f'{today:%B %d, %Y}')                 # March 30, 2018
