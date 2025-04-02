import unittest
import dungeon.pyd.index as INDEX
import dungeon.pyd.way as WAY
import dungeon.pyd.mask as mask
import dungeon.pyd.action as ACTION
import dungeon.pyd.enemyType as ENEMY_TYPE
import dungeon.pyd.eventType as EVENT_TYPE
import dungeon.pyd.itemType as ITME_TYPE


class TestIndex(unittest.TestCase):
    def test_0(self):
        self.assertEqual(INDEX.RIGHT(), 0)

    def test_1(self):
        self.assertEqual(INDEX.CENTER(), 1)

    def test_2(self):
        self.assertEqual(INDEX.LEFT(), 2)

    def test_3(self):
        self.assertEqual(INDEX.FLAME(), 3)

    def test_4(self):
        self.assertEqual(INDEX.WALL(), 4)

    def test_5(self):
        self.assertEqual(INDEX.PLAYER(), 5)

    def test_6(self):
        self.assertEqual(INDEX.PATH(), 6)

    def test_7(self):
        self.assertEqual(INDEX.BOARD_S(), 7)

    def test_8(self):
        self.assertEqual(INDEX.TEXT3(), 8)

    def test_9(self):
        self.assertEqual(INDEX.BOARD_M(), 9)

    def test_10(self):
        self.assertEqual(INDEX.TEXT5(), 10)

    def test_11(self):
        self.assertEqual(INDEX.BUTTON(), 11)

    def test_12(self):
        self.assertEqual(INDEX.ACTION(), 13)

    def test_13(self):
        self.assertEqual(INDEX.ITEM(), 14)

    def test_BOX(self):
        self.assertEqual(INDEX.BOX(), 15)

    def test_COMPASS(self):
        self.assertEqual(INDEX.COMPASS(), 16)

    def test_15(self):
        self.assertEqual(INDEX.UP_POS(), 0)

    def test_16(self):
        self.assertEqual(INDEX.CENTER_POS(), 1)

    def test_17(self):
        self.assertEqual(INDEX.DOWN_POS(), 2)

    def test_18(self):
        self.assertEqual(INDEX.ACTION(), 13)

    def test_19(self):
        self.assertEqual(INDEX.TEXT6(), 12)


class TestWay(unittest.TestCase):
    def test_0(self):
        self.assertEqual(WAY.UP(), 0)

    def test_1(self):
        self.assertEqual(WAY.RIGHT(), 1)

    def test_2(self):
        self.assertEqual(WAY.LEFT(), 2)

    def test_3(self):
        self.assertEqual(WAY.DOWN(), 3)

    def test_UP_0(self):
        self.assertEqual(WAY.isUp(0), True)

    def test_UP_1(self):
        self.assertEqual(WAY.isUp(1), False)

    def test_RIGHT_0(self):
        self.assertEqual(WAY.isRight(1), True)

    def test_RIGHT_1(self):
        self.assertEqual(WAY.isRight(0), False)

    def test_LEFT_0(self):
        self.assertEqual(WAY.isLeft(2), True)

    def test_LEFT_1(self):
        self.assertEqual(WAY.isLeft(0), False)

    def test_DOWN_0(self):
        self.assertEqual(WAY.isDown(3), True)

    def test_DOWN_1(self):
        self.assertEqual(WAY.isDown(0), False)


class TestMask(unittest.TestCase):
    def test_0(self):
        self.assertEqual(mask.L(), 0xF000)

    def test_1(self):
        self.assertEqual(mask.C(), 0x0FF0)

    def test_2(self):
        self.assertEqual(mask.R(), 0x000F)

    def test_3(self):
        self.assertEqual(mask.LU(), 0x1000)

    def test_4(self):
        self.assertEqual(mask.LC(), 0x2000)

    def test_5(self):
        self.assertEqual(mask.LD(), 0x1000)

    def test_6(self):
        self.assertEqual(mask.RU(), 0x0001)

    def test_7(self):
        self.assertEqual(mask.RC(), 0x0002)

    def test_8(self):
        self.assertEqual(mask.RD(), 0x0001)


class TestAction(unittest.TestCase):
    def test_0(self):
        self.assertEqual(ACTION.GO_UP_THE_STAIRS(), 0)

    def test_1(self):
        self.assertEqual(ACTION.SEARCH(), 1)


class TestEnemyType(unittest.TestCase):
    def test_DANGER(self):
        self.assertEqual(ENEMY_TYPE.DANGER(), 0)


class TestEventType(unittest.TestCase):
    def test_INFO_0(self):
        self.assertEqual(EVENT_TYPE.INFO(), 0)

    def test_INFO_1(self):
        self.assertEqual(EVENT_TYPE.getText(EVENT_TYPE.INFO()), "[INFO]")

    def test_WARNING_0(self):
        self.assertEqual(EVENT_TYPE.WARNING(), 1)

    def test_WARNING_1(self):
        self.assertEqual(EVENT_TYPE.getText(EVENT_TYPE.WARNING()), "[WARN]")

    def test_FLAVOR_0(self):
        self.assertEqual(EVENT_TYPE.FLAVOR(), 2)

    def test_FLAVOR_1(self):
        self.assertEqual(EVENT_TYPE.getText(EVENT_TYPE.FLAVOR()), "")

    def test_ITEM_0(self):
        self.assertEqual(EVENT_TYPE.ITEM(), 3)

    def test_ITEM_1(self):
        self.assertEqual(EVENT_TYPE.getText(EVENT_TYPE.ITEM()), "[INFO]")


class TestItemType(unittest.TestCase):
    def test_COMPASS_0(self):
        self.assertEqual(ITME_TYPE.COMPASS(), 0)

    def test_COMPASS_1(self):
        self.assertEqual(ITME_TYPE.getText(ITME_TYPE.COMPASS()), "COMPASS")


unittest.main(argv=['first-arg-is-ignored'], exit=False)
