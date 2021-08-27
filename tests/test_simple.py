# -*- coding: utf-8 -*-

from .context_set import sample

import unittest


class SimpleTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()