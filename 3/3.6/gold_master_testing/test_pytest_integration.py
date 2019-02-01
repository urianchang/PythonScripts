import unittest

from approvaltests.approvals import verify
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory

@unittest.skip("Broken")
class IntTesst(unittest.TestCase):
    """
    This isn't working as expected because vim is never opened for the diff.
    The test will fail due to an "Approval Mismatch", but the user won't be
    able to see what's different and breaking the test.
    """
    def setUp(self):
        self.reporter = GenericDiffReporterFactory().get_first_working()

    def test_int(self):
        verify("Uh-oh", self.reporter)
