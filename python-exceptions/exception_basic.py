def f(num):
    if num == 1:
        raise RuntimeError("It's a one.")
    else:
        return num

a = f(2)
if a:
    print("a is ok")
print("a: {}".format(a))

b = f(1)
if b:
    print("b is ok")
print("b: {}".format(b))

for i in xrange(10):
    if i == 4:
        raise ValueError("I hate 4's")
    print i
