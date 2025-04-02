import common.debug.debug as dbg
import common.common as cmn


class Action:
    def update(configForm, opeForm):
        (x, y) = opeForm.MOUSE()
        (clickX, clickY) = opeForm.leftClickMoveMouse()
        wayKeyType = configForm.WAY_KEY_TYPE()
        goKeyType = configForm.GO_KEY_TYPE()
        wayKeyType1Click = cmn.Judge.click(50, 180, 200, 80, x, y, clickX, clickY, opeForm.isLeftClick())
        wayKeyType2Click = cmn.Judge.click(260, 180, 200, 80, x, y, clickX, clickY, opeForm.isLeftClick())
        GoKeyType1Click = cmn.Judge.click(50, 320, 200, 80, x, y, clickX, clickY, opeForm.isLeftClick())
        GoKeyType2Click = cmn.Judge.click(260, 320, 200, 80, x, y, clickX, clickY, opeForm.isLeftClick())
        StepKeyType1Click = cmn.Judge.click(50, 460, 200, 80, x, y, clickX, clickY, opeForm.isLeftClick())
        StepKeyType2Click = cmn.Judge.click(260, 460, 200, 80, x, y, clickX, clickY, opeForm.isLeftClick())
        # キータイプ1_設定
        Action.__setWaykeyType(configForm, wayKeyType, wayKeyType1Click, wayKeyType2Click)
        # キータイプ2_設定
        Action.__setGokeyType(configForm, goKeyType, GoKeyType1Click, GoKeyType2Click)
        # キータイプ3_設定
        Action.__setStepkeyType(configForm, goKeyType, StepKeyType1Click, StepKeyType2Click)

    def __setWaykeyType(configForm, wayKeyType, click1, click2):
        if (wayKeyType != 1 and click1):
            configForm.updateNowWayKeyType(1)
        elif (wayKeyType != 2 and click2):
            configForm.updateNowWayKeyType(2)
        elif (click1 or click2):
            dbg.LOG("[ConfigAction.update]" + str(wayKeyType) + "再設定")
            if wayKeyType < 0 or 2 < wayKeyType:
                dbg.ERROR_LOG("[ConfigAction.update]存在しないKeyType")

    def __setGokeyType(configForm, goKeyType, click1, click2):
        if (goKeyType != 1 and click1):
            configForm.updateNowGoKeyType(1)
        elif (goKeyType != 2 and click2):
            configForm.updateNowGoKeyType(2)
        elif (click1 or click2):
            dbg.LOG("[ConfigAction.update]" + str(goKeyType) + "再設定")
            if goKeyType < 0 or 2 < goKeyType:
                dbg.ERROR_LOG("[ConfigAction.update]存在しないKeyType")

    def __setStepkeyType(configForm, goKeyType, click1, click2):
        if (goKeyType != 2 and click1):
            configForm.updateNowGoKeyType(2)
        elif (goKeyType != 1 and click2):
            configForm.updateNowGoKeyType(1)
        elif (click1 or click2):
            dbg.LOG("[ConfigAction.update]" + str(goKeyType) + "再設定")
            if goKeyType < 0 or 2 < goKeyType:
                dbg.ERROR_LOG("[ConfigAction.update]存在しないKeyType")
