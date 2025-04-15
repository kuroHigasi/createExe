import common.common as cmn
import dungeon.convert as convert
import pyd.status as STATUS
import pyd.save as SAVE


class Status:
    def nextStatus(statusForm, opeForm, saveForm):
        nextStatus = STATUS.SAVE()
        (x, y) = opeForm.get_mouse()
        (clickX, clickY) = opeForm.left_click_move_mouse()
        (buckX, buckY, sizeX, sizeY) = saveForm.get_back_button()
        (homeX, homeY, homeSizeX, homeSizeY) = saveForm.get_home_button()
        if (cmn.Judge.click(buckX, buckY, sizeX, sizeY, x, y, clickX, clickY, opeForm.is_left_click())):
            nextStatus = saveForm.get_pre_status()
        if not (homeX == -1 and homeY == -1):
            if (cmn.Judge.click(homeX, homeY, homeSizeX, homeSizeY, x, y, clickX, clickY, opeForm.is_left_click())):
                nextStatus = STATUS.HOME()
        if (saveForm.OUTPUT_DATA() != ""):
            nextStatus = STATUS.DUNGEON()
        statusForm.updateStatus(nextStatus)

    def updatePreStatus(saveForm, status):
        saveForm.set_pre_status(status)

    def updateInputData(saveForm, data):
        saveForm.updateInputData(data)

    def resetInputData(saveForm):
        saveForm.updateInputData("")

    def resetOutputData(saveForm):
        saveForm.updateOutputData("")

    def updateDispSaveList(saveForm):
        for i in (0, 2, 1):
            head = SAVE.SAVE_HEAD(i)
            tail = SAVE.SAVE_TAIL(i)
            saveMethod = cmn.SaveMethod()
            dispData = convert.Convert.getDispData(saveMethod.load(head, tail))
            saveForm.updateSaveDispList(i, dispData)
