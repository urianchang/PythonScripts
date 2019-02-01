import unittest

from approvaltests.approvals import verify
from approvaltests.reporters.generic_diff_reporter_factory import GenericDiffReporterFactory


class GettingStartedTest(unittest.TestCase):
    def setUp(self):
        self.reporter = GenericDiffReporterFactory().get_first_working()

    def test_simple(self):
        # Need to include the newline character at the end because
        # it's automatically appended at the end of the approved.txt file
        verify("This is what's expected!\n", self.reporter)


""" NOTES:
* Expected files look like this: "GettingStartedTest.test_simple.approved.txt"
* "approvaltests_config.json" configures the subdirectory that contains approved
and received text files
"""


if __name__ == "__main__":
    unittest.main()
