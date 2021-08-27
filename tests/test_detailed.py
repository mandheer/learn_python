# -*- coding: utf-8 -*-

from .context_set import sample

import unittest


class DetailedTestSuite(unittest.TestCase):
    """Detailed test cases."""

    def test_something(self):
        self.assertIsNone(sample.hmm())


if __name__ == '__main__':
    unittest.main()