# Ref: https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
def simple_generator_function():
    yield 1
    yield 2
    yield 3

# Two ways of using it...
for value in simple_generator_function():
    print(value)

our_generator = simple_generator_function()
next(our_generator)
next(our_generator)
next(our_generator)
