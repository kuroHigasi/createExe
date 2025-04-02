import unittest
import common.end.pyd.index as INDEX


class TestIndex(unittest.TestCase):
    def test_HOME(self):
        self.assertEqual(INDEX.END(), 0)

    def test_BUTTON(self):
        self.assertEqual(INDEX.BUTTON(), 1)


unittest.main(argv=['first-arg-is-ignored'], exit=False)
