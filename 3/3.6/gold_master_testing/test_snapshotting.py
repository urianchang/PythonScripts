import unittest

import pandas as pd
import pprint as pp
# import snapshottest
# from snapshottest.file import FileSnapshot    # Throws ModuleNotFoundError

@unittest.skip("Works")
def test_snap1(snapshot):
    snapshot.assert_match('Hello')


@unittest.skip("Works")
def test_snap2(snapshot):
    with open('approved_files/csv_file1.csv', 'r') as f:
        data = f.read()
        snapshot.assert_match(data)


@unittest.skip("Works, but not preferred")
def test_snap3(snapshot):
    """
    Snapshots keep updating if a String object is not used.
    """
    df = pd.read_csv(
            './approved_files/csv_file1.csv',
            header=0,
            index_col=0
        )
    snapshot.assert_match(df.to_dict(orient='records'))


@unittest.skip("Works")
def test_snap4(snapshot):
    df = pd.read_csv(
            './approved_files/csv_file1.csv',
            header=0,
            index_col=0
        )
    df_formatted_dict_string = pp.pformat(df.to_dict(orient='records'))
    snapshot.assert_match(df_formatted_dict_string)

@unittest.skip("Works")
def test_snap5(snapshot):
    print(type(snapshot.module[snapshot.test_name]))
    snapshot.assert_match('hello world')
    # assert False


# def test_multiple_files(snapshot, tmpdir):
#     """
#     Each file is stored separately with the snapshot's name inside the module's file snapshots folder.
#     """
#     temp_file1 = tmpdir.join('example1.txt')
#     temp_file1.write('Hello, world 1!')
#     snapshot.assert_match(FileSnapshot(str(temp_file1)))
#
#     temp_file1 = tmpdir.join('example2.txt')
#     temp_file1.write('Hello, world 2!')
#     snapshot.assert_match(FileSnapshot(str(temp_file1)))
