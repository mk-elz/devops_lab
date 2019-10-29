from unittest import TestCase

import HamDistScript


class TestHamDistScript(TestCase):

    def test_ham_dist_func(self):
        """Test for is _prime"""
        self.assertEqual(HamDistScript.ham_dist_func(2, 4), 2)
