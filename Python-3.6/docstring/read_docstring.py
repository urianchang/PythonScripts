import json


def my_func():
    """
    {
        "a": 1,
        "b": "2",
        "c": ["hello", "'world'"]
    }
    """
    pass

# print(my_func.__doc__)  # help(my_func) works too!

# NOTE: Use double quotes or else JSON decoder will throw an error
d = json.loads(my_func.__doc__)
print(d['a'])
print(d['b'])
print(d['c'])
