import unittest
import common.config.pyd.index as INDEX


class TestIndex(unittest.TestCase):
    def test_HOME(self):
        self.assertEqual(INDEX.CONFIG(), 0)

    def test_CONFIG_BUTTON(self):
        self.assertEqual(INDEX.CONFIG_BUTTON(), 1)

    def test_BUTTON(self):
        self.assertEqual(INDEX.BUTTON(), 2)

    def test_SET_BUTTON(self):
        self.assertEqual(INDEX.SET_BUTTON(), 3)


unittest.main(argv=['first-arg-is-ignored'], exit=False)
