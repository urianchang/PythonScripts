import json
import collections

j = json.JSONDecoder(object_pairs_hook=collections.OrderedDict).decode('{"foo":1, "bar": 2}')

print j
