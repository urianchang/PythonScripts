# Exercise 8.1

def chop(a) :
    del a[0]
    del a[-1]

def middle(a) :
    return a[1:-1]

num = ["a", "b", "c", "d"]
result = middle(num)
print result