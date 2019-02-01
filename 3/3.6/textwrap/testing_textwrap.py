# Python 3.6.4
import textwrap

para = '''\
    hello
    world
    HI
'''

d = textwrap.dedent(para)

print("==With Dedent==")
print(d)
print("==Without Dedent==")
print(para)
