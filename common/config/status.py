import common.common as cmn
import common.config.convert as convert
import pyd.status as STATUS
import pyd.save as SAVE


class Status:
    def nextStatus(statusForm, opeForm, configForm):
        nextStatus = STATUS.CONFIG()
        (x, y) = opeForm.MOUSE()
        (clickX, clickY) = opeForm.leftClickMoveMouse()
        (ok_x, ok_y, ok_width, ok_height) = configForm.get_ok_button()
        (back_x, back_y, back_width, back_height) = configForm.get_back_button()
        if ok_x != -1 and ok_y != -1:  # OKボタンは設定が変更されたタイミングしか表示されない
            if cmn.Judge.click(ok_x, ok_y, ok_width, ok_height, x, y, clickX, clickY, opeForm.isLeftClick()):
                cmn.SaveMethod().save(convert.Convert.createInput(configForm), SAVE.CONF_HEAD(), SAVE.CONF_TAIL())
                nextStatus = configForm.pre_status
        if cmn.Judge.click(back_x, back_y, back_width, back_height, x, y, clickX, clickY, opeForm.isLeftClick()):
            configForm.buckKeyType()
            nextStatus = configForm.pre_status
        statusForm.updateStatus(nextStatus)

    def config_form_get_status(configForm, status):
        configForm.pre_status = status

    def loadConfig(configForm):
        saveMethod = cmn.SaveMethod()
        convert.Convert.convertOutput(configForm, saveMethod.load(SAVE.CONF_HEAD(), SAVE.CONF_TAIL()))
