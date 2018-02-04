import sys
import simplejson
import yaml
import ruamel.yaml as y
from pprint import pprint

conf = raw_input().strip()

with open(conf, 'rb') as f:
    # config = yaml.safe_load(f)
    config = y.load(f, Loader=y.RoundTripLoader)
print type(config)
# x = y.dump(config, Dumper=y.RoundTripDumper, allow_unicode=True, default_flow_style=False, indent=2)
d = simplejson.loads(simplejson.dumps(config))
print type(d)
print d

# print yaml.load("""
# test:
# - tester_name: asdf
#   type: local
#   completed: true
#   errors: 1
# """)

""" From: https://github.com/fmenabe/python-yamlordereddictloader
# LOADERS
def construct_yaml_map(self, node):
    data = OrderedDict()
    yield data
    value = self.construct_mapping(node)
    data.update(value)

def construct_mapping(self, node, deep=False):
    if isinstance(node, yaml.MappingNode):
        self.flatten_mapping(node)
    else:
        msg = 'expected a mapping node, but found %s' % node.id
        raise yaml.constructor.ConstructError(None,
                                              None,
                                              msg,
                                              node.start_mark)

    mapping = OrderedDict()
    for key_node, value_node in node.value:
        key = self.construct_object(key_node, deep=deep)
        try:
            hash(key)
        except TypeError as err:
            raise yaml.constructor.ConstructError(
                'while constructing a mapping', node.start_mark,
                'found unacceptable key (%s)' % err, key_node.start_mark)
        value = self.construct_object(value_node, deep=deep)
        mapping[key] = value
    return mapping

class Loader(yaml.Loader):
    def __init__(self, *args, **kwargs):
        yaml.Loader.__init__(self, *args, **kwargs)

        self.add_constructor(
            'tag:yaml.org,2002:map', type(self).construct_yaml_map)
        self.add_constructor(
            'tag:yaml.org,2002:omap', type(self).construct_yaml_map)

    construct_yaml_map = construct_yaml_map
    construct_mapping = construct_mapping

class SafeLoader(yaml.SafeLoader):
    def __init__(self, *args, **kwargs):
        yaml.SafeLoader.__init__(self, *args, **kwargs)

        self.add_constructor(
            'tag:yaml.org,2002:map', type(self).construct_yaml_map)
        self.add_constructor(
            'tag:yaml.org,2002:omap', type(self).construct_yaml_map)

    construct_yaml_map = construct_yaml_map
    construct_mapping = construct_mapping

# DUMPERS
def represent_ordereddict(self, data):
    return self.represent_mapping('tag:yaml.org,2002:map', data.items())

class Dumper(yaml.Dumper):
    def __init__(self, *args, **kwargs):
        yaml.Dumper.__init__(self, *args, **kwargs)
        self.add_representer(OrderedDict, type(self).represent_ordereddict)

    represent_ordereddict = represent_ordereddict

class SafeDumper(yaml.SafeDumper):
    def __init__(self, *args, **kwargs):
        yaml.SafeDumper.__init__(self, *args, **kwargs)
        self.add_representer(OrderedDict, type(self).represent_ordereddict)

    represent_ordereddict = represent_ordereddict
"""