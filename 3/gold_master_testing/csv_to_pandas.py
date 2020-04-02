import ast
import logging

import numpy as np
import pandas as pd
import pprint as pp
from testfixtures import compare


log = logging.getLogger(__name__)

df = pd.read_csv(
    './approved_files/csv_file2.csv',
    header=0,
    index_col=None,
)

# Change to readable list of dictionaries
d = df.to_dict(orient='records')

# Change to a pprint string
sd = pp.pformat(d)

# Change back to list
l = ast.literal_eval(sd)

# Change back to dataframe
df2 = pd.DataFrame.from_dict(l, orient='columns')

# Check for any differences
# df2 = pd.read_csv(
#     './approved_files/csv_file3.csv',
#     header=0,
#     index_col=None,
# )

# print(df != df2)
# print(df != df_revert)
# print(pd.concat([df, df2]).drop_duplicates(keep=False))

# Using testfixtures.compare...
# d2 = df2.to_dict(orient='records')
# compare(d, d2)

# https://stackoverflow.com/questions/17095101/outputting-difference-in-two-pandas-dataframes-side-by-side-highlighting-the-d
"""
def contrast_dataframes(observed_df: DataFrame, expected_df: DataFrame) -> DataFrame:
    # Compare two DataFrames and return a DataFrame with value differences. Please note that
    # the DataFrames have to be identically named or else a value error will be thrown.

    stacked_diff = (observed_df != expected_df).stack()
    changed = stacked_diff[stacked_diff]
    changed.index.names = ['id', 'column']

    diff_indexes = np.where(observed_df != expected_df)
    changed_observed = observed_df.values[diff_indexes]
    changed_expected = expected_df.values[diff_indexes]

    diff_df = DataFrame(
        {
            'Observed': changed_observed,
            'Expected': changed_expected,
        },
        index=changed.index
    )
    return diff_df
"""

# print(df)
# print(df2)

ne_stacked = (df != df2).stack()
changed = ne_stacked[ne_stacked]
changed.index.names = ['id', 'col']
# print(changed)

locate_diff_idx = np.where(df != df2)
# print(locate_diff_idx)
changed_from = df.values[locate_diff_idx]
print(changed_from)
changed_to = df2.values[locate_diff_idx]
# print(changed_to)

diff = pd.DataFrame({'from': changed_from, 'to': changed_to}, index=changed.index)

if diff.empty:
    print('no differences')
else:
    log.error(f'Differences:\n{diff}')
