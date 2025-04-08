import dungeon.display as dungeonDisp
import common.home.display as homeDisp
import common.config.display as configDisp
import common.end.display as endDisp
import common.save.display as saveDisp
import pyd.status as STATUS
import common.debug.debug as dbg
import dungeon.convert as ConvertDungeon


class Display:
    def execute(screen, statusForm, systemForm, operationForm):
        nowStatus = statusForm.NOW_STATUS()
        preStatus = statusForm.PRE_STATUS()
        dungeonForm = systemForm.DUNGEON_FORM()
        endForm = systemForm.END_FORM()
        saveForm = systemForm.SAVE_FORM()
        if (nowStatus == STATUS.EXIT()):
            dbg.LOG("[main.DISP]終了ステータスのため何もしない")
        elif (statusForm.NOW_STATUS() == STATUS.END()):
            if preStatus == STATUS.DUNGEON():
                endForm.updateActionCount(dungeonForm)
            endDisp.Display.endDisplay(screen, endForm, operationForm, 0, 0)
        elif (nowStatus == STATUS.HOME()):
            Display.__homeDisp(screen, systemForm.HOME_FORM(), operationForm)
        elif (nowStatus == STATUS.CONFIG()):
            Display.__configDisp(screen, systemForm.CONFIG_FORM(), operationForm)
        elif (nowStatus == STATUS.SAVE()):
            Display.__saveDisp(screen, systemForm.SAVE_FORM(), operationForm)
        elif (nowStatus == STATUS.DUNGEON()):
            if preStatus == STATUS.HOME():
                dungeonForm.offEndFlag()
                floor = dungeonForm.FLOOR()
                dungeonForm.reset(floor)
            if preStatus == STATUS.SAVE() and saveForm.OUTPUT_DATA() != "":
                dungeonForm.offEndFlag()
                floor = ConvertDungeon.Convert.getFloor(saveForm.OUTPUT_DATA())
                dungeonForm.reset(floor)
            Display.__dungeonInfo(screen, systemForm.DUNGEON_FORM(), systemForm, operationForm)
        else:
            dbg.ERROR_LOG("[Main.DISP]存在しないステータス:"+str(statusForm.NOW_STATUS()))

    def __dungeonInfo(screen, dungeonForm, dispSystemForm, opeForm):
        flash = dispSystemForm.FLASH
        dunDisp = dungeonDisp.Display()
        dunDisp.dispRader(screen, dungeonForm, flash, 800, 0)
        dunDisp.dispConversationText(screen, dungeonForm, 0, 600)
        dunDisp.dispInfo(screen, dungeonForm, flash, 800, 200)
        dunDisp.dispActionButton(screen, dungeonForm, opeForm, flash, 800, 400)
        dunDisp.dispSystemButton(screen, dungeonForm, opeForm, flash, 800, 600)
        dunDisp.dispView(screen, dungeonForm, opeForm, 0, 0)

    def __homeDisp(screen, homeForm, opeForm):
        homeDisp.Display.dispHome(screen, homeForm, opeForm, 0, 0)

    def __configDisp(screen, configForm, opeForm):
        configDisp.Display.dispConfig(screen, configForm, opeForm, 0, 0)

    def __saveDisp(screen, saveForm, opeForm):
        saveDisp.Display.dispSave(screen, saveForm, opeForm, 0, 0)
