import common.common as cmn
import common.config.convert as convert
import common.pyd.status as STATUS
import common.pyd.save as SAVE


class Status:
    def nextStatus(statusForm, opeForm, configForm):
        nextStatus = STATUS.CONFIG()
        (x, y) = opeForm.MOUSE()
        (clickX, clickY) = opeForm.leftClickMoveMouse()
        (okX, okY) = configForm.OK_BUTTON()
        (buckX, buckY) = configForm.BUCK_BUTTON()
        if okX != -1 and okY != -1:  # OKボタンは設定が変更されたタイミングしか表示されない
            if (cmn.Judge.click(okX, okY, 200, 80, x, y, clickX, clickY, opeForm.isLeftClick())):
                saveMethod = cmn.SaveMethod()
                saveMethod.save(convert.Convert.createInput(configForm), SAVE.CONF_HEAD(), SAVE.CONF_TAIL())
                nextStatus = configForm.PRE_STATUS()
        if (cmn.Judge.click(buckX, buckY, 200, 80, x, y, clickX, clickY, opeForm.isLeftClick())):
            configForm.buckKeyType()
            nextStatus = configForm.PRE_STATUS()
        statusForm.updateStatus(nextStatus)

    def updatePreStatus(configForm, status):
        configForm.updatePreStatus(status)

    def loadConfig(configForm):
        saveMethod = cmn.SaveMethod()
        convert.Convert.convertOutput(configForm, saveMethod.load(SAVE.CONF_HEAD(), SAVE.CONF_TAIL()))
