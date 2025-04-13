import pyd.status as STATUS
import common.common as cmn
import dungeon.convert as convert


class Status:
    def nextStatus(statusForm, opeForm, dungeonForm):
        nextStatus = STATUS.DUNGEON()
        (x, y) = opeForm.get_mouse()
        (clickX, clickY) = opeForm.left_click_move_mouse()
        (configX, configY, configSizeW, configSizeH) = dungeonForm.CONFIG_BUTTON()
        (saveX, saveY, saveSizeW, saveSizeH) = dungeonForm.SAVE_BUTTON()
        if dungeonForm.END_FLAG():
            nextStatus = STATUS.END()
        elif (cmn.Judge.click(configX, configY, configSizeW, configSizeH, x, y, clickX, clickY, opeForm.is_left_click())):
            nextStatus = STATUS.CONFIG()
        elif (cmn.Judge.click(saveX, saveY, saveSizeW, saveSizeH, x, y, clickX, clickY, opeForm.is_left_click())):
            nextStatus = STATUS.SAVE()
        statusForm.updateStatus(nextStatus)

    def updateLog(dungeonForm):
        if dungeonForm.UPDATE_LOG_FLAG():
            dungeonForm.updateLog()
            dungeonForm.logFlagOff()

    def fromHomeReset(dungeonForm):
        dungeonForm.reset(1)
        dungeonForm.updateTotalCount(0)
        dungeonForm.resetLog()
        dungeonForm.itemBoxClear()

    def fromSaveConvert(dungeonForm, data: str):
        if (data != ""):
            convert.Convert.convertOutput(dungeonForm, data)
