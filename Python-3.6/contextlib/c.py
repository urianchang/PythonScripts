import logging
from contextlib import ContextDecorator

log = logging.getLogger(__name__)


class MyException(Exception):
    pass


def function_1():
    # raise AssertionError(1)
    print("function 1")
    # raise AssertionError(1)


def function_3():
    # raise AssertionError(3)
    # print("function 3")
    # raise AssertionError(3)
    try:
        raise MyException("uh-oh")
        print("function 3")
        # raise AssertionError
    except MyException:
        log.exception("error in function 3")
        # raise


class providecontext(ContextDecorator):
    def __enter__(self):
        # raise MyException("in __enter__")
        # try:
        #     function_3()
        # except Exception:
        #     raise
        return self

    def __exit__(self, *exc):
        raise MyException("in __exit__")
        function_1()
        return False


@providecontext()
def function_2():
    # raise AssertionError(2)
    print("function 2")
    # raise AssertionError(2)


if __name__ == "__main__":
    print("START")

    try:
        function_2()
    except MyException:
        print("not ok")

    print("END")
