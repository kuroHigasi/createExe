import unittest
import pyd.createPass as cPass
import pyd.hitJudge as hitJudge
import pyd.calc as CALC
import pyd.save as SAVE
import pyd.status as STATUS
import pyd.indexHome as INDEX_HOME
import pyd.indexConfig as INDEX_CONFIG
import pyd.indexEnd as INDEX_END
import pyd.imgNum as IMG_NUM
import pyd.indexSave as INDEX_SAVE
import pyd.indexDungeon as INDEX_DUNGEON
import pyd.way as WAY
import pyd.mask as MASK
import pyd.typeAction as ACTION
import pyd.typeEnemy as ENEMY_TYPE
import pyd.typeEvent as EVENT_TYPE
import pyd.typeItem as ITME_TYPE


class TestCreatePass(unittest.TestCase):
    def test_1(self):
        self.assertEqual(cPass.getImgPass("test", "BUTTON", 0), "data\\img\\test\\BUTTON\\BUTTON0.png")

    def test_2(self):
        self.assertEqual(cPass.getFontPass("DotGothic16-Regular.ttf"), "data\\fonts\\DotGothic16-Regular.ttf")

    def test_3(self):
        self.assertEqual(cPass.getMp3Pass("test", "BUTTON", 0), "data\\mp3\\test\\BUTTON\\BUTTON0.mp3")


class TestHitJudge(unittest.TestCase):
    def test_1(self):
        self.assertTrue(hitJudge.hitJudgeSquare(0, 0, 10, 10, 5, 5))

    def test_2(self):
        self.assertFalse(hitJudge.hitJudgeSquare(0, 0, 10, 10, 5, 15))

    def test_3(self):
        self.assertFalse(hitJudge.hitJudgeSquare(0, 0, 10, 10, 15, 15))

    def test_4(self):
        self.assertTrue(hitJudge.hitJudgeSquare(0, 0, 10, 10, 0, 5))

    def test_5(self):
        self.assertTrue(hitJudge.hitJudgeSquare(0, 0, 10, 10, 5, 0))


class TestStatus(unittest.TestCase):
    def test_EXIT(self):
        self.assertEqual(STATUS.EXIT(), 0)

    def test_HOME(self):
        self.assertEqual(STATUS.HOME(), 2)

    def test_END(self):
        self.assertEqual(STATUS.END(), 1)

    def test_CONFIG(self):
        self.assertEqual(STATUS.CONFIG(), 3)

    def test_SAVE(self):
        self.assertEqual(STATUS.SAVE(), 4)

    def test_DUNGEON(self):
        self.assertEqual(STATUS.DUNGEON(), 5)

    def test_CHECK_TRUE(self):
        self.assertTrue(STATUS.existStatus(1))

    def test_CHECK_FALSE(self):
        self.assertFalse(STATUS.existStatus(100))


class TestCalc(unittest.TestCase):
    # MASK AND RIGHT_SHIFT
    def test_maskAndRight_1(self):
        self.assertEqual(CALC.maskAndRight(0x0010, 0x0011, 4), 1)

    def test_maskAndRight_2(self):
        self.assertEqual(CALC.maskAndRight(0x0010, 0x1100, 4), 0)

    def test_maskAndRight_3(self):
        self.assertEqual(CALC.maskAndRight(0x0100, 0x0011, 8), 0)

    def test_maskAndRight_4(self):
        self.assertEqual(CALC.maskAndRight(0x0100, 0x1100, 8), 1)

    def test_maskAndRight_5(self):
        self.assertEqual(CALC.maskAndRight(0x1000, 0x1100, 12), 1)

    # MASK AND LEFT_SHIFT
    def test_maskAndLeft_1(self):
        self.assertEqual(CALC.maskAndLeft(0x0010, 0x0011, 4), 0x0100)

    def test_maskAndLeft_2(self):
        self.assertEqual(CALC.maskAndLeft(0x0010, 0x1100, 4), 0)

    def test_maskAndWLeft_3(self):
        self.assertEqual(CALC.maskAndLeft(0x0100, 0x0011, 8), 0)

    def test_maskAndLeft_4(self):
        self.assertEqual(CALC.maskAndLeft(0x0100, 0x1100, 8), 0)

    def test_maskAndLeft_5(self):
        self.assertEqual(CALC.maskAndLeft(0x1000, 0x1100, 12), 0)

    # BITMASK(0x...)
    def test_bitmask_1(self):
        self.assertEqual(CALC.bitmask(0x0010, 0x0001), 0x0011)

    def test_bitmask_2(self):
        self.assertEqual(CALC.bitmask(0x0010, 0x0100), 0x0110)

    def test_bitmask_3(self):
        self.assertEqual(CALC.bitmask(0x0010, 0x0020), 0x0030)

    def test_bitmask_4(self):
        self.assertEqual(CALC.bitmask(0x0010, 0x0008), 0x0018)

    # BITMASK(0b...)
    def test_bitmask_5(self):
        self.assertEqual(CALC.bitmask(0b0010, 0b0001), 0b0011)

    def test_bitmask_6(self):
        self.assertEqual(CALC.bitmask(0b0010, 0b0010), 0b0010)

    def test_bitmask_7(self):
        self.assertEqual(CALC.bitmask(0b0010, 0b0100), 0b0110)

    def test_bitmask_8(self):
        self.assertEqual(CALC.bitmask(0b0010, 0b1000), 0b1010)


class TestSave(unittest.TestCase):
    def test_saveHead_0(self):
        self.assertEqual(SAVE.SAVE_HEAD(0), "dEr0O0e")

    def test_saveHead_1(self):
        self.assertEqual(SAVE.SAVE_HEAD(1), "dEr1O1e")

    def test_saveHead_2(self):
        self.assertEqual(SAVE.SAVE_HEAD(2), "dEr2O2e")

    def test_saveTail_0(self):
        self.assertEqual(SAVE.SAVE_TAIL(0), "cLe0R0i")

    def test_saveTail_1(self):
        self.assertEqual(SAVE.SAVE_TAIL(1), "cLe1R1i")

    def test_saveTail_2(self):
        self.assertEqual(SAVE.SAVE_TAIL(2), "cLe2R2i")

    def test_confHead_0(self):
        self.assertEqual(SAVE.CONF_HEAD(), "cOnsCon")

    def test_confTail_0(self):
        self.assertEqual(SAVE.CONF_TAIL(), "cOntCon")

    def test_pass_0(self):
        self.assertEqual(SAVE.PASS(), "save\\save.dat")

    def test_folder_0(self):
        self.assertEqual(SAVE.FOLDER(), "save")


class TestIndexHome(unittest.TestCase):
    def test_HOME(self):
        self.assertEqual(INDEX_HOME.HOME(), 0)

    def test_BUTTON(self):
        self.assertEqual(INDEX_HOME.BUTTON(), 1)


class TestIndexConfig(unittest.TestCase):
    def test_HOME(self):
        self.assertEqual(INDEX_CONFIG.CONFIG(), 0)

    def test_CONFIG_BUTTON(self):
        self.assertEqual(INDEX_CONFIG.CONFIG_BUTTON(), 1)

    def test_BUTTON(self):
        self.assertEqual(INDEX_CONFIG.BUTTON(), 2)

    def test_SET_BUTTON(self):
        self.assertEqual(INDEX_CONFIG.SET_BUTTON(), 3)


class TestIndexEnd(unittest.TestCase):
    def test_HOME(self):
        self.assertEqual(INDEX_END.END(), 0)

    def test_BUTTON(self):
        self.assertEqual(INDEX_END.BUTTON(), 1)


class TestNum(unittest.TestCase):
    def test_BUTTON(self):
        self.assertEqual(IMG_NUM.BUTTON(), 16)

    def test_CONFIG(self):
        self.assertEqual(IMG_NUM.CONFIG(), 1)

    def test_CONFIG_BUTTON(self):
        self.assertEqual(IMG_NUM.CONFIG_BUTTON(), 3)

    def test_CONFIG_SET_BUTTON(self):
        self.assertEqual(IMG_NUM.CONFIG_SET_BUTTON(), 13)

    def test_SAVE_LIST(self):
        self.assertEqual(IMG_NUM.SAVE_LIST(), 2)

    def test_SAVE(self):
        self.assertEqual(IMG_NUM.SAVE(), 1)

    def test_SAVE_BUTTON(self):
        self.assertEqual(IMG_NUM.SAVE_BUTTON(), 9)

    def test_END(self):
        self.assertEqual(IMG_NUM.END(), 1)

    def test_HOME(self):
        self.assertEqual(IMG_NUM.HOME(), 1)


class TestIndexSave(unittest.TestCase):
    def test_SAVE(self):
        self.assertEqual(INDEX_SAVE.SAVE(), 0)

    def test_BUTTON(self):
        self.assertEqual(INDEX_SAVE.BUTTON(), 1)

    def test_LIST(self):
        self.assertEqual(INDEX_SAVE.LIST(), 2)


class TestIndexDungeon(unittest.TestCase):
    def test_0(self):
        self.assertEqual(INDEX_DUNGEON.RIGHT(), 0)

    def test_1(self):
        self.assertEqual(INDEX_DUNGEON.CENTER(), 1)

    def test_2(self):
        self.assertEqual(INDEX_DUNGEON.LEFT(), 2)

    def test_3(self):
        self.assertEqual(INDEX_DUNGEON.FLAME(), 3)

    def test_4(self):
        self.assertEqual(INDEX_DUNGEON.WALL(), 4)

    def test_5(self):
        self.assertEqual(INDEX_DUNGEON.PLAYER(), 5)

    def test_6(self):
        self.assertEqual(INDEX_DUNGEON.PATH(), 6)

    def test_7(self):
        self.assertEqual(INDEX_DUNGEON.BOARD_S(), 7)

    def test_8(self):
        self.assertEqual(INDEX_DUNGEON.TEXT3(), 8)

    def test_9(self):
        self.assertEqual(INDEX_DUNGEON.BOARD_M(), 9)

    def test_10(self):
        self.assertEqual(INDEX_DUNGEON.TEXT5(), 10)

    def test_11(self):
        self.assertEqual(INDEX_DUNGEON.BUTTON(), 11)

    def test_12(self):
        self.assertEqual(INDEX_DUNGEON.ACTION(), 13)

    def test_13(self):
        self.assertEqual(INDEX_DUNGEON.ITEM(), 14)

    def test_BOX(self):
        self.assertEqual(INDEX_DUNGEON.BOX(), 15)

    def test_COMPASS(self):
        self.assertEqual(INDEX_DUNGEON.COMPASS(), 16)

    def test_15(self):
        self.assertEqual(INDEX_DUNGEON.UP_POS(), 0)

    def test_16(self):
        self.assertEqual(INDEX_DUNGEON.CENTER_POS(), 1)

    def test_17(self):
        self.assertEqual(INDEX_DUNGEON.DOWN_POS(), 2)

    def test_18(self):
        self.assertEqual(INDEX_DUNGEON.ACTION(), 13)

    def test_19(self):
        self.assertEqual(INDEX_DUNGEON.TEXT6(), 12)


class TestWay(unittest.TestCase):
    def test_0(self):
        self.assertEqual(WAY.UP()(), 0)

    def test_1(self):
        self.assertEqual(WAY.RIGHT()(), 1)

    def test_2(self):
        self.assertEqual(WAY.LEFT()(), 2)

    def test_3(self):
        self.assertEqual(WAY.DOWN()(), 3)

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
        self.assertEqual(MASK.L(), 0xF000)

    def test_1(self):
        self.assertEqual(MASK.C(), 0x0FF0)

    def test_2(self):
        self.assertEqual(MASK.R(), 0x000F)

    def test_3(self):
        self.assertEqual(MASK.LU(), 0x1000)

    def test_4(self):
        self.assertEqual(MASK.LC(), 0x2000)

    def test_5(self):
        self.assertEqual(MASK.LD(), 0x1000)

    def test_6(self):
        self.assertEqual(MASK.RU(), 0x0001)

    def test_7(self):
        self.assertEqual(MASK.RC(), 0x0002)

    def test_8(self):
        self.assertEqual(MASK.RD(), 0x0001)


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
