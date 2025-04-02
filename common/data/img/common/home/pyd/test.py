import unittest
import common.home.pyd.index as INDEX


class TestIndex(unittest.TestCase):
    def test_HOME(self):
        self.assertEqual(INDEX.HOME(), 0)

    def test_BUTTON(self):
        self.assertEqual(INDEX.BUTTON(), 1)


unittest.main(argv=['first-arg-is-ignored'], exit=False)
