import dungeon.display as dungeon_display
import common.home.display as home_display
import common.config.display as config_display
import common.end.display as end_display
import common.save.display as save_display
import pyd.status as STATUS
import common.debug.debug as dbg
import dungeon.convert as convert_dungeon


class Display:
    @staticmethod
    def execute(screen, status_form, system_form, ope_form):
        now_status = status_form.now_status
        pre_status = status_form.pre_status
        # FORM
        dungeon_form = system_form.dungeon_form
        end_form = system_form.end_form
        save_form = system_form.save_form
        config_form = system_form.config_form
        home_form = system_form.home_form
        if now_status == STATUS.EXIT():
            dbg.LOG("[main.DISP]終了ステータスのため何もしない")
        elif now_status == STATUS.END():
            if pre_status == STATUS.DUNGEON():
                end_form.set_action_count(dungeon_form)
            request_end = \
                end_display.Display.create_request_data(screen, end_form, ope_form)
            end_display.Display.execute(end_form, request_end)
        elif now_status == STATUS.HOME():
            request_home = \
                home_display.Display.create_request_data(screen, home_form, ope_form)
            home_display.Display.execute(home_form, request_home)
        elif now_status == STATUS.CONFIG():
            request_config = \
                config_display.Display.create_request_data(screen, config_form, ope_form)
            config_display.Display.execute(config_form, request_config)
        elif now_status == STATUS.SAVE():
            request_save = \
                save_display.Display.create_request_data(screen, save_form, ope_form)
            save_display.Display.execute(save_form, request_save)
        elif now_status == STATUS.DUNGEON():
            if pre_status == STATUS.HOME():
                dungeon_form.end_flag = False
                dungeon_form.reset(dungeon_form.get_floor())
            if pre_status == STATUS.SAVE() and save_form.OUTPUT_DATA() != "":
                dungeon_form.end_flag = False
                dungeon_form.reset(convert_dungeon.Convert.getFloor(save_form.OUTPUT_DATA()))
            request_dungeon = \
                dungeon_display.Display.create_request_data(screen, dungeon_form, ope_form, system_form)
            dungeon_display.Display.execute(dungeon_form, request_dungeon)
        else:
            dbg.ERROR_LOG("[Main.DISP]存在しないステータス:"+str(now_status))
