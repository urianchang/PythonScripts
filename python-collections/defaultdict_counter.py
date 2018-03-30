from collections import defaultdict, Counter

# Basic example
# d = defaultdict(Counter)
#
# d['hi'].update(('hello',))
# d['hi'].update(('hello',))
# d['bye'].update(('good-bye',))
#
# print d.keys()
# print d.values()
#
# for k,v in d.items():
#     print k, v
#
# if 'hi' in d['asdf']:
#     print "ok"
#
# print 'hello' in d['hi']

# Create nested dictionaries
d = defaultdict(lambda: defaultdict(dict))
d['hi']['hello']['bye'] = 1
print d['hi']['hello']['bye']
d['hi']['hello'].update({'bye': 2})
print d['hi']['hello']['bye']
print d['bye'].keys()
