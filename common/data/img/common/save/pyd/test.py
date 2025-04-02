import unittest
import common.save.pyd.index as INDEX


class TestIndex(unittest.TestCase):
    def test_SAVE(self):
        self.assertEqual(INDEX.SAVE(), 0)

    def test_BUTTON(self):
        self.assertEqual(INDEX.BUTTON(), 1)

    def test_LIST(self):
        self.assertEqual(INDEX.LIST(), 2)


unittest.main(argv=['first-arg-is-ignored'], exit=False)
