# Python 3.6
from abc import ABCMeta


class MyClass(object):

    @property
    def schema(self) -> None:
        """Some help text here...

        - **a**: 'A' property
        - *b*: 'B' property (list)

        """
        return {
            "a": 1,
            "b": [1, 2, 3]
        }

class MyMeta(metaclass=ABCMeta):

    @property
    def schema(self) -> None:
        """Some help text here...

        - **a**: 'A' property
        - *b*: 'B' property (list)

        """
        return {
            "a": 1,
            "b": [1, 2, 3]
        }

print(MyClass().schema['a'])
print(MyClass().schema['b'][1])

print(MyMeta().schema['a'])
print(MyMeta().schema['b'][2])
print(MyMeta.schema)
