import dungeon.display as dungeonDisp
import common.home.display as homeDisp
import common.config.display as configDisp
import common.end.display as endDisp
import common.save.display as saveDisp
import pyd.status as STATUS
import common.debug.debug as dbg
import dungeon.convert as ConvertDungeon


class Display:
    @staticmethod
    def execute(screen, status_form, system_form, ope_form):
        now_status = status_form.NOW_STATUS()
        pre_status = status_form.PRE_STATUS()
        dungeon_form = system_form.DUNGEON_FORM()
        end_form = system_form.END_FORM()
        save_form = system_form.SAVE_FORM()
        config_form = system_form.CONFIG_FORM()
        if now_status == STATUS.EXIT():
            dbg.LOG("[main.DISP]終了ステータスのため何もしない")
        elif now_status == STATUS.END():
            if pre_status == STATUS.DUNGEON():
                end_form.updateActionCount(dungeon_form)
            endDisp.Display.endDisplay(screen, end_form, ope_form, 0, 0)
        elif now_status == STATUS.HOME():
            Display.__homeDisp(screen, system_form.HOME_FORM(), ope_form)
        elif now_status == STATUS.CONFIG():
            configDisp.Display.execute(
                config_form,
                configDisp.Display.create_request_data(screen, config_form, ope_form))
        elif now_status == STATUS.SAVE():
            saveDisp.Display.execute(save_form, saveDisp.Display.create_request_data(screen, save_form, ope_form))
        elif now_status == STATUS.DUNGEON():
            if pre_status == STATUS.HOME():
                dungeon_form.offEndFlag()
                floor = dungeon_form.FLOOR()
                dungeon_form.reset(floor)
            if pre_status == STATUS.SAVE() and save_form.OUTPUT_DATA() != "":
                dungeon_form.offEndFlag()
                floor = ConvertDungeon.Convert.getFloor(save_form.OUTPUT_DATA())
                dungeon_form.reset(floor)
            Display.__dungeonInfo(screen, system_form.DUNGEON_FORM(), system_form, ope_form)
        else:
            dbg.ERROR_LOG("[Main.DISP]存在しないステータス:"+str(status_form.NOW_STATUS()))

    def __dungeonInfo(screen, dungeon_form, system_form, ope_form):
        flash = system_form.FLASH
        dungeonDisp.Display.dispRader(screen, dungeon_form, flash, 800, 0)
        dungeonDisp.Display.dispConversationText(screen, dungeon_form, 0, 600)
        dungeonDisp.Display.dispInfo(screen, dungeon_form, flash, 800, 200)
        dungeonDisp.Display.dispActionButton(screen, dungeon_form, ope_form, flash, 800, 400)
        dungeonDisp.Display.dispSystemButton(screen, dungeon_form, ope_form, flash, 800, 600)
        dungeonDisp.Display.dispView(screen, dungeon_form, ope_form, 0, 0)

    def __homeDisp(screen, home_form, ope_form):
        homeDisp.Display.dispHome(screen, home_form, ope_form, 0, 0)
