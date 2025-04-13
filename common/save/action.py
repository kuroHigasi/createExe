import common.common as cmn
import pyd.save as SAVE
# ゲーム毎
import dungeon.convert as ConvertDungeon
# ゲーム毎


class Action:
    def save(saveForm, opeForm):
        Action.__save(saveForm, opeForm, 0)
        Action.__save(saveForm, opeForm, 1)
        Action.__save(saveForm, opeForm, 2)
        Action.__load(saveForm, opeForm, 0)
        Action.__load(saveForm, opeForm, 1)
        Action.__load(saveForm, opeForm, 2)
        Action.__delete(saveForm, opeForm, 0)
        Action.__delete(saveForm, opeForm, 1)
        Action.__delete(saveForm, opeForm, 2)

    def __save(saveForm, opeForm, index):
        (x, y) = opeForm.get_mouse()
        (clickX, clickY) = opeForm.left_click_move_mouse()
        (saveX, saveY, saveW, saveH) = saveForm.SAVE_LIST(index)
        if not (saveX == -1 and saveY == -1):
            if cmn.Judge.click(saveX, saveY, saveW, saveH, x, y, clickX, clickY, opeForm.is_left_click()):
                saveMesthod = cmn.SaveMethod()
                saveMesthod.save(saveForm.INPUT_DATA(), SAVE.SAVE_HEAD(index), SAVE.SAVE_TAIL(index))
                Action.__updateDispSaveList(saveForm)

    def __load(saveForm, opeForm, index):
        (x, y) = opeForm.get_mouse()
        (clickX, clickY) = opeForm.left_click_move_mouse()
        (loadX, loadY, loadW, loadH) = saveForm.LOAD_LIST(index)
        if not (loadX == -1 and loadY == -1):
            if cmn.Judge.click(loadX, loadY, loadW, loadH, x, y, clickX, clickY, opeForm.is_left_click()):
                saveMesthod = cmn.SaveMethod()
                saveForm.updateOutputData(saveMesthod.load(SAVE.SAVE_HEAD(index), SAVE.SAVE_TAIL(index)))

    def __delete(saveForm, opeForm, index):
        (x, y) = opeForm.get_mouse()
        (clickX, clickY) = opeForm.left_click_move_mouse()
        (deleteX, deleteY, deleteW, deleteH) = saveForm.DELETE_LIST(index)
        if not (deleteX == -1 and deleteY == -1):
            if cmn.Judge.click(deleteX, deleteY, deleteW, deleteH, x, y, clickX, clickY, opeForm.is_left_click()):
                saveMesthod = cmn.SaveMethod()
                saveMesthod.delete(SAVE.SAVE_HEAD(index), SAVE.SAVE_TAIL(index))
                Action.__updateDispSaveList(saveForm)

    def updateInputData(saveForm, data):
        saveForm.updateInputData(data)

    def resetOutputData(saveForm):
        saveForm.updateOutputData("")

    def receiveOutputData(saveForm):
        saveForm.OUTPUT_DATA()

    def updateDispSaveList(saveForm):
        Action.__updateDispSaveList(saveForm)

    def __updateDispSaveList(saveForm):
        for i in (0, 2, 1):
            head = SAVE.SAVE_HEAD(i)
            tail = SAVE.SAVE_TAIL(i)
            saveMethod = cmn.SaveMethod()
            dispData = ConvertDungeon.Convert.getDispData(saveMethod.load(head, tail))
            saveForm.updateSaveDispList(i, dispData)
