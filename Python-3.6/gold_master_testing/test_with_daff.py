import csv
from datetime import datetime
import numbers
import os
import re
import sys
from typing import Any, List
import unittest

import daff
import numpy as np
import pandas as pd
import pytz
from pprint import pprint


Table = List[List[Any]]


def encode_value(value: Any) -> str:
    if isinstance(value, numbers.Number):
        return repr(value)
    elif isinstance(value, str):
        # Encode strings inside single quotes so that they are represented
        # differently from other values. Otherwise the diff will omit changes
        # from strings to other types or vice versa.
        return f"'{value}'"
    elif isinstance(value, (datetime, np.datetime64, pd.Timestamp)):
        # As far as FactoryTX is concerned all datetime types are equivalent.
        if isinstance(value, np.datetime64):
            value = value.astype(datetime)
        elif isinstance(value, pd.Timestamp):
            value = value.to_pydatetime()
        if value.tzinfo is not None:
            value = value.astimezone(pytz.utc)
        return value.strftime("%Y-%m-%d %H:%M:%S.%f")
    elif isinstance(value, list):
        parts = []
        parts.append('[')
        for element in value:
            parts.append(encode_value(element))
            parts.append(', ')
        parts.append(']')
        return ''.join(parts)
    else:
        raise TypeError(f'Unsupported type "{type(value).__name__}": {value}')


def encode_table(table: Table) -> Table:
    encoded = [table[0]]  # Don't encode values in the header row.
    encoded.extend([encode_value(x) for x in row] for row in table[1:])
    return encoded


REQUIRES_ESCAPE_RE = re.compile('[",\n]')

def escape_value(value: str) -> str:
    if REQUIRES_ESCAPE_RE.search(value):
        value = f'''"{value.replace('"', '""')}"'''
    return value


def escape_table(table: Table) -> Table:
    escaped = [[escape_value(x) for x in row] for row in table]
    return escaped


def format_table(table: Table) -> str:
    """Convert tabular data to an aligned quasi-CSV format."""
    assert all(len(row) == len(table[0]) for row in table), \
        "All rows in a table must have the same number of columns"
    escaped = escape_table(table)
    widths = [0] * len(table[0])
    for row in escaped:
        for colno, value in enumerate(row):
            widths[colno] = max(widths[colno], len(value))
    parts = []
    for row in escaped:
        for colno, value in enumerate(row):
            if colno > 0:
                parts.append(',')
            parts.append(value)
            parts.append(' ' * (widths[colno] - len(value)))
        parts.append('\n')
    output = ''.join(parts)
    return output


def load_table(s: str) -> Table:
    """Convert an aligned table from `format_table` back to an encoded table."""
    reader = csv.reader(
        s.split('\n'),
        delimiter=',',
        doublequote=True,
        quotechar='"',
        strict=False
    )
    # All strings are wrapped in single quotes so we can safely strip values.
    table = [[x.rstrip() for x in row] for row in reader if row]
    return table


ANSI_ESCAPE_RE = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -/]*[@-~]')

def strip_ansi_escapes(s: str) -> str:
    return ANSI_ESCAPE_RE.sub('', s)


def format_diff(a: Table, b: Table, index: List[str] = []) -> str:
    flags = daff.CompareFlags()
    for name in index:
        flags.addPrimaryKey(name)
    diff = daff.Coopy.diff(a, b, flags=flags)

    if len(diff.data) > 1:
        output = daff.TerminalDiffRender().render(diff)
    else:
        output = ""

    return output


def dataframe_to_table(df: pd.DataFrame) -> Table:
    rows = [df.columns.tolist()]
    for idx, row in df.iterrows():
        rows.append(row.tolist())
    return rows


def test_with_daff(capsys, snapshot):
    input_df = pd.read_csv(
        './approved_files/csv_file3.csv',
        header=0,
        index_col=0
    )

    input_table = encode_table(dataframe_to_table(input_df))

    res = snapshot.module[snapshot.test_name]
    if not snapshot.update and res:
        expected_table = load_table(res)
        output = format_diff(input_table, expected_table, index=['col1'])

        if output:
            with capsys.disabled():
                if not os.isatty(sys.stdout.fileno()):
                    output = strip_ansi_escapes(output)
                raise ValueError(f'\n{output}')

    # Format the DataFrame to a good format for Git diff
    formatted_table = format_table(input_table)
    snapshot.assert_match(formatted_table)
