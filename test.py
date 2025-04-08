import unittest
import lib.createPass as cPass
import lib.hitJudge as hitJudge
import lib.calc as CALC
import lib.save as SAVE
import lib.status as STATUS
import lib.indexHome as INDEX_HOME
import lib.indexConfig as INDEX_CONFIG
import lib.indexEnd as INDEX_END
import lib.imgNum as IMG_NUM
import lib.indexSave as INDEX_SAVE


class TestCreatePass(unittest.TestCase):
    def test_1(self):
        self.assertEqual(cPass.getImgPass("test", "BUTTON", 0), "data\\img\\test\\BUTTON\\BUTTON0.png")

    def test_2(self):
        self.assertEqual(cPass.getFontPass("DotGothic16-Regular.ttf"), "data\\fonts\\DotGothic16-Regular.ttf")


class TestHitJudge(unittest.TestCase):
    def test_1(self):
        self.assertEqual(hitJudge.hitJudgeSquare(0, 0, 10, 10, 5, 5), True)

    def test_2(self):
        self.assertEqual(hitJudge.hitJudgeSquare(0, 0, 10, 10, 5, 15), False)

    def test_3(self):
        self.assertEqual(hitJudge.hitJudgeSquare(0, 0, 10, 10, 15, 15), False)

    def test_4(self):
        self.assertEqual(hitJudge.hitJudgeSquare(0, 0, 10, 10, 0, 5), True)

    def test_5(self):
        self.assertEqual(hitJudge.hitJudgeSquare(0, 0, 10, 10, 5, 0), True)


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


class TestCreatePass(unittest.TestCase):
    def test_BUTTON(self):
        self.assertEqual(IMG_NUM.BUTTON(), 16)

    def test_CONFIG(self):
        self.assertEqual(IMG_NUM.CONFIG(), 1)

    def test_CONFIG_BUTTON(self):
        self.assertEqual(IMG_NUM.CONFIG_BUTTON(), 2)

    def test_CONFIG_SET_BUTTON(self):
        self.assertEqual(IMG_NUM.CONFIG_SET_BUTTON(), 10)

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


unittest.main(argv=['first-arg-is-ignored'], exit=False)
