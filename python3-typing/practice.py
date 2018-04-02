# Python 3.6
# https://docs.python.org/3/library/typing.html
import typing

# Need to run script with mypy to catch TypeErrors: `mypy practice.py`

def greeting(name: str) -> str:
    return 'Hello {}'.format(name)

print(greeting("Bobby"))

my_string: str

my_string = 123     # TypeError should be thrown here
print(my_string)
