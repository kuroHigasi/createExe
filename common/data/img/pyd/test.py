import unittest
import common.data.img.pyd.num as num


class TestCreatePass(unittest.TestCase):
    def test_BUTTON(self):
        self.assertEqual(num.BUTTON(), 16)

    def test_CONFIG(self):
        self.assertEqual(num.CONFIG(), 1)

    def test_CONFIG_BUTTON(self):
        self.assertEqual(num.CONFIG_BUTTON(), 2)

    def test_CONFIG_SET_BUTTON(self):
        self.assertEqual(num.CONFIG_SET_BUTTON(), 10)

    def test_SAVE_LIST(self):
        self.assertEqual(num.SAVE_LIST(), 2)

    def test_SAVE(self):
        self.assertEqual(num.SAVE(), 1)

    def test_SAVE_BUTTON(self):
        self.assertEqual(num.SAVE_BUTTON(), 9)

    def test_END(self):
        self.assertEqual(num.END(), 1)

    def test_HOME(self):
        self.assertEqual(num.HOME(), 1)


unittest.main(argv=['first-arg-is-ignored'], exit=False)
