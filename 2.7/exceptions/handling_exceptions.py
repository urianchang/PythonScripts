import logging

a = "blah"

try:
    1/0
except:
    a = "what"
    logging.exception("something")

# Usually `finally` is used for code cleanup

print a
