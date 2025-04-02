import common.pyd.status as STATUS
import common.operation.form as opeForm
import common.status.form as statusForm
import common.common as cmn


class TestOperation():
    def test_init(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_click_right_0(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.rightClickOn()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert True is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (0, 0)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_click_right_1(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.rightClickOn()
        testForm.rightClickOff()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_click_left_0(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.leftClickOn()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert True is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (0, 0)
        assert testForm.MOUSE() == (0, 0)

    def test_click_left_1(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.leftClickOn()
        testForm.leftClickOff()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_UP_0(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.upOn()
        # 検証
        assert True is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_UP_1(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.upOn()
        testForm.upOff()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_RIGHT_0(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.rightOn()
        # 検証
        assert False is testForm.UP()
        assert True is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_RIGHT_1(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.rightOn()
        testForm.rightOff()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_LEFT_0(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.leftOn()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert True is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_LEFT_1(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.leftOn()
        testForm.leftOff()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_DOWN_0(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.downOn()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert True is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_DOWN_1(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.downOn()
        testForm.downOff()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_MOUSE_0(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.setMouse(100, 100)
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (100, 100)

    def test_MOUSE_1(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.setMouse(100, 100)
        testForm.setMouse(200, 300)
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (200, 300)

    def test_RIGHT_CLICK_0(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.setMouse(100, 100)
        testForm.rightClickOn()
        testForm.setMouse(10, 10)
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert True is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (100, 100)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (10, 10)

    def test_RIGHT_CLICK_1(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.setMouse(10, 10)
        testForm.rightClickOn()
        testForm.setMouse(100, 100)
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert True is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (10, 10)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (100, 100)

    def test_LEFT_CLICK_0(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.setMouse(100, 100)
        testForm.leftClickOn()
        testForm.setMouse(10, 10)
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert True is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (100, 100)
        assert testForm.MOUSE() == (10, 10)

    def test_LEFT_CLICK_1(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.setMouse(10, 10)
        testForm.leftClickOn()
        testForm.setMouse(100, 100)
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert True is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (10, 10)
        assert testForm.MOUSE() == (100, 100)

    def test_ENTER_0(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.enterOn()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert True is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_ENTER_1(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.enterOn()
        testForm.enterOff()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_ENTER_2(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.enterOn()
        testForm.enterOff()
        testForm.enterOn()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert True is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_SPACE_0(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.spaceOn()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert True is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_SPACE_1(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.spaceOn()
        testForm.spaceOff()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert False is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)

    def test_SPACE_2(self):
        # 事前準備
        testForm = opeForm.OperationForm()
        testForm.spaceOn()
        testForm.spaceOff()
        testForm.spaceOn()
        # 検証
        assert False is testForm.UP()
        assert False is testForm.RIGHT()
        assert False is testForm.LEFT()
        assert False is testForm.DOWN()
        assert False is testForm.ENTER()
        assert True is testForm.SPACE()
        assert False is testForm.isRightClick()
        assert testForm.rightClickMoveMouse() == (-1, -1)
        assert False is testForm.isLeftClick()
        assert testForm.leftClickMoveMouse() == (-1, -1)
        assert testForm.MOUSE() == (0, 0)


class TestStatus():
    def test_init_0(self):
        testForm = statusForm.Form(STATUS.HOME())
        assert testForm.NOW_STATUS(), STATUS.HOME()
        assert testForm.PRE_STATUS(), STATUS.HOME()
        assert False is testForm.diffStatus()

    def test_init_1(self):
        testForm = statusForm.Form(STATUS.SAVE())
        assert testForm.NOW_STATUS(), STATUS.SAVE()
        assert testForm.PRE_STATUS(), STATUS.SAVE()
        assert False is testForm.diffStatus()

    def test_update_0(self):
        testForm = statusForm.Form(STATUS.HOME())
        testForm.updateStatus(STATUS.SAVE())
        assert testForm.NOW_STATUS(), STATUS.SAVE()
        assert testForm.PRE_STATUS(), STATUS.HOME()
        assert True is testForm.diffStatus()


class TestCommon():
    def test_judge_0(self):
        jdgFlg = cmn.Judge.click(0, 0, 100, 100, 0, 0, 0, 0, True)
        assert True is jdgFlg

    def test_judge_1(self):
        jdgFlg = cmn.Judge.click(0, 0, 100, 100, 0, 150, 0, 0, True)
        assert False is jdgFlg

    def test_judge_2(self):
        jdgFlg = cmn.Judge.click(0, 0, 100, 100, 100, 100, 0, 0, True)
        assert True is jdgFlg

    def test_judge_3(self):
        jdgFlg = cmn.Judge.click(0, 0, 100, 100, 150, 0, 0, 0, True)
        assert False is jdgFlg

    def test_judge_error_0(self):
        jdgFlg = cmn.Judge.click(-1, -1, 100, 100, 150, 0, 0, 0, True)
        assert False is jdgFlg

    def test_flash_0(self):
        testFlash = cmn.Flash(10, 2)
        assert testFlash.flash() == 0
        testFlash.countup()
        assert testFlash.flash() == 0
        testFlash.countup()
        assert testFlash.flash() == 0
        testFlash.countup()
        assert testFlash.flash() == 0
        testFlash.countup()
        assert testFlash.flash() == 0
        testFlash.countup()
        assert testFlash.flash() == 0
        testFlash.countup()
        assert testFlash.flash() == 0
        testFlash.countup()
        assert testFlash.flash() == 0
        testFlash.countup()
        assert testFlash.flash() == 0
        testFlash.countup()
        assert testFlash.flash() == 0
        testFlash.countup()
        assert testFlash.flash() == 1
        testFlash.countup()
        assert testFlash.flash() == 1

    def test_flash_1(self):
        testFlash = cmn.Flash(5, 3)
        assert testFlash.flash() == 0
        testFlash.countup()
        assert testFlash.flash() == 0
        testFlash.countup()
        assert testFlash.flash() == 0
        testFlash.countup()
        assert testFlash.flash() == 0
        testFlash.countup()
        assert testFlash.flash() == 0
        testFlash.countup()
        assert testFlash.flash() == 1
        testFlash.countup()
        assert testFlash.flash() == 1
        testFlash.countup()
        assert testFlash.flash() == 1
        testFlash.countup()
        assert testFlash.flash() == 1
        testFlash.countup()
        assert testFlash.flash() == 1
        testFlash.countup()
        assert testFlash.flash() == 2
        testFlash.countup()
        assert testFlash.flash() == 2
        testFlash.countup()
        assert testFlash.flash() == 2
        testFlash.countup()
        assert testFlash.flash() == 2
        testFlash.countup()
        assert testFlash.flash() == 2
        testFlash.countup()
        assert testFlash.flash() == 0
