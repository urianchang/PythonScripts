import unittest

from snapshottest import TestCase


@unittest.skip("Works")
class SnapTest(TestCase):

    def setUp(self):
        with open('approved_files/csv_file1.csv', 'r') as f:
            self.data = f.read()

    def test_snap1(self):
        """
        Currently running into an issue with updating snapshots
        """
        self.assertMatchSnapshot(self.data)
