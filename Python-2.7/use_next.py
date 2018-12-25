def_col = {'var': "a"}

machine = {'stats': [
    {'title': "b"},
    {'title': 'a', 'analytics': {'columns': [{'title': "column 1"}]}}
]}

mt_stat = next(
    (x for x in machine.get('stats', []) if x.get('title', '') == def_col['var']),
    {}
)

col_info = mt_stat.get('analytics', {}).get('columns', [{}])[0]
print col_info
