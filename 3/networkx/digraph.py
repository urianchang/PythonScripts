# Python 3.7
import itertools
import networkx as nx


def pairwise(iterable):
  "s -> (s0,s1), (s1,s2), (s2, s3), ..."
  a, b = itertools.tee(iterable)
  next(b, None)
  return zip(a, b)


time_duration = {
  'teemo': {
    'milliseconds': {'transform': lambda x: (50, 0),}
  },
  'milliseconds': {
    'seconds': {
        # Return result, remainder
        'transform': lambda x: divmod(x, 1000),
    },
    'teemo': {
        'transform': lambda x: (1, 0),
    }
  },
  'seconds': {
    'milliseconds': {
        'transform': lambda x: (x * 1000, 0),
    },
    'minutes': {
        'transform': lambda x: divmod(x, 60),
    },
  },
  'minutes': {
    'seconds': {
      'transform': lambda x: (x * 60, 0),
    },
    'hours': {
      'transform': lambda x: divmod(x, 60),
    },
  },
  'hours': {
    'minutes': {
      'transform': lambda x: (x * 60, 0),
    },
    'days': {
      'transform': lambda x: divmod(x, 24),
    },
  },
  'days': {
    'hours': {
      'transform': lambda x: (x * 24, 0),
    },
    'weeks': {
      'transform': lambda x: divmod(x, 7),
    },
    'teemo': {'transform': lambda x: (3, 10)}
  },
  'weeks': {
    'days': {
      'transform': lambda x: (x * 7, 0),
    },
    # 'teemo': {'transform': lambda x: (2, 0)}
  },
}

# value = 2 * 7 * 24 * 60 * 60  # 2 weeks in seconds
value = 100
g = nx.from_dict_of_dicts(time_duration, create_using=nx.DiGraph())

result = value
for from_, to_ in pairwise(nx.shortest_path(g, source='weeks', target='milliseconds')):
  result, _ = g.get_edge_data(from_, to_)['transform'](result)

print(result)