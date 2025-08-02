import common.debug.debug as dbg
import pyd.status as STATUS
import dungeon.status as DungeonStatus
import common.home.status as HomeStatus
import common.config.status as ConfigStatus
import common.end.status as EndStatus
import common.save.status as save_status


class Status:
    @staticmethod
    def execute(status_form, system_form, ope_form):
        now_status = status_form.now_status
        config_form = system_form.config_form
        save_form = system_form.save_form
        dungeon_form = system_form.dungeon_form
        home_form = system_form.home_form
        end_form = system_form.end_form
        # ステータス毎 処理分岐
        if now_status == STATUS.EXIT():
            dbg.LOG("[main.STATUS]終了ステータスのため何もしない")
        elif now_status == STATUS.END():
            end_request = EndStatus.Status.create_request_data(end_form, ope_form)
            EndStatus.Status.execute(status_form, end_request)
        elif now_status == STATUS.HOME():
            home_request = HomeStatus.Status.create_request_data(home_form, ope_form)
            HomeStatus.Status.execute(status_form, home_request)
        elif now_status == STATUS.CONFIG():
            config_request = ConfigStatus.Status.create_request_data(config_form, ope_form)
            ConfigStatus.Status.execute(status_form, config_form, config_request)
        elif now_status == STATUS.SAVE():
            save_request = save_status.Status.create_request_data(save_form, ope_form)
            save_status.Status.execute(status_form, save_request)
        elif now_status == STATUS.DUNGEON():
            dungeon_request = DungeonStatus.Status.create_request_data(dungeon_form, ope_form)
            DungeonStatus.Status.execute(status_form, dungeon_request)
            DungeonStatus.Status.updateLog(dungeon_form)
        else:
            dbg.ERROR_LOG("[Main.STATUS]存在しないステータス: "+str(now_status))
            status_form.update_status(STATUS.HOME())

    @staticmethod
    def init(status_form, system_form, operation_form):
        now_status = status_form.now_status
        pre_status = status_form.pre_status
        config_form = system_form.config_form
        save_form = system_form.save_form
        dungeon_form = system_form.dungeon_form
        # ステータス遷移タイミング 初期化 共通処理
        Status.__change_init(pre_status, now_status, operation_form, config_form)
        # ステータス毎 処理分岐
        if now_status == STATUS.EXIT():
            if pre_status != STATUS.EXIT():
                dbg.LOG("[main.EXIT]終了ステータスのため何もしない")
        elif now_status == STATUS.END():
            if pre_status != STATUS.END():
                dbg.LOG("[main.END]初期化処理なし")
        elif now_status == STATUS.HOME():
            if pre_status != STATUS.HOME():
                ConfigStatus.Status.load_config(config_form)
        elif now_status == STATUS.CONFIG():
            if pre_status != STATUS.CONFIG():
                ConfigStatus.Status.config_form_get_status(config_form, pre_status)
                ConfigStatus.Status.load_config(config_form)
        elif now_status == STATUS.SAVE():
            if pre_status != STATUS.SAVE():
                save_status.Status.initialize(save_form, pre_status)
                if pre_status == STATUS.DUNGEON():
                    save_status.Status.update_input_data(save_form, dungeon_form)
                else:
                    save_status.Status.reset_input_data(save_form)
        elif now_status == STATUS.DUNGEON():
            if pre_status == STATUS.HOME():
                DungeonStatus.Status.fromHomeReset(dungeon_form)
            if pre_status == STATUS.SAVE():
                DungeonStatus.Status.fromSaveConvert(dungeon_form, save_form.OUTPUT_DATA())
        else:
            dbg.ERROR_LOG("[Main.STATUS]存在しないステータス: "+str(now_status))
            status_form.update_status(STATUS.HOME())

    @staticmethod
    def __change_init(pre_status, now_status, operation_form, config_form):
        if pre_status != now_status:
            operation_form.reset_mouse_click_l()
            operation_form.reset_mouse_click_r()
            config_form.update_pre_way_key_type()
            config_form.update_pre_go_key_type()
