from pprint import pprint

COLS = int(input('Number of columns: ').strip())
ROWS = int(input("Number of rows: ").strip())

res = ""

for i in range(1, ROWS+1):
    for j in range(1, COLS+1):
        if i == 1:
            res += f'col{j},'
        else:
            res += f'c{j}r{i-1},'
    res += '\r'

pprint(res)
