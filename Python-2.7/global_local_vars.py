def s2(d):
    d.setdefault('a', 2)

def something(a):
  a = a.copy()
  a.pop('a')
  s2(a)
  return a

a = {'a': 1, 'b': 2}
print a
a = something(a)
print a
