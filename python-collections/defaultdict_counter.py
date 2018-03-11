from collections import defaultdict, Counter

d = defaultdict(Counter)

d['hi'].update(('hello',))
d['hi'].update(('hello',))
d['bye'].update(('good-bye',))

print d.keys()
print d.values()

for k,v in d.items():
    print k, v

if 'hi' in d['asdf']:
    print "ok"

print 'hello' in d['hi']
