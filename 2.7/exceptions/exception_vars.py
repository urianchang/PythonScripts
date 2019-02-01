import logging

try:
    assert False
    a = 2
except AssertionError:
    a = 1
    msg = "test test"
    logging.exception(msg)

print a
