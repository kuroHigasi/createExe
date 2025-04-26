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
        now_status = status_form.NOW_STATUS()
        config_form = system_form.CONFIG_FORM()
        save_form = system_form.SAVE_FORM()
        dungeon_form = system_form.DUNGEON_FORM()
        home_form = system_form.HOME_FORM()
        # ステータス毎 処理分岐
        if now_status == STATUS.EXIT():
            dbg.LOG("[main.STATUS]終了ステータスのため何もしない")
        elif now_status == STATUS.END():
            EndStatus.Status.nextStatus(status_form, ope_form, system_form.END_FORM())
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
            DungeonStatus.Status.updateLog(system_form.DUNGEON_FORM())
        else:
            dbg.ERROR_LOG("[Main.STATUS]存在しないステータス: "+str(now_status))
            status_form.updateStatus(STATUS.HOME())

    def init(statusForm, systemForm, operationForm):
        now_status = statusForm.NOW_STATUS()
        pre_status = statusForm.PRE_STATUS()
        configForm = systemForm.CONFIG_FORM()
        saveForm = systemForm.SAVE_FORM()
        dungeonForm = systemForm.DUNGEON_FORM()
        # ステータス遷移タイミング 初期化 共通処理
        Status.__change_init(pre_status, now_status, operationForm, configForm)
        # ステータス毎 処理分岐
        if now_status == STATUS.EXIT():
            if pre_status != STATUS.EXIT():
                dbg.LOG("[main.EXIT]終了ステータスのため何もしない")
        elif now_status == STATUS.END():
            if pre_status != STATUS.END():
                dbg.LOG("[main.END]初期化処理なし")
        elif now_status == STATUS.HOME():
            if pre_status != STATUS.HOME():
                ConfigStatus.Status.load_config(configForm)
        elif now_status == STATUS.CONFIG():
            if pre_status != STATUS.CONFIG():
                ConfigStatus.Status.config_form_get_status(configForm, pre_status)
                ConfigStatus.Status.load_config(configForm)
        elif now_status == STATUS.SAVE():
            if pre_status != STATUS.SAVE():
                save_status.Status.initialize(saveForm, pre_status)
                if pre_status == STATUS.DUNGEON():
                    save_status.Status.update_input_data(saveForm, dungeonForm)
                else:
                    save_status.Status.reset_input_data(saveForm)
        elif now_status == STATUS.DUNGEON():
            if pre_status == STATUS.HOME():
                DungeonStatus.Status.fromHomeReset(dungeonForm)
            if pre_status == STATUS.SAVE():
                DungeonStatus.Status.fromSaveConvert(dungeonForm, saveForm.OUTPUT_DATA())
        else:
            dbg.ERROR_LOG("[Main.STATUS]存在しないステータス: "+str(now_status))
            statusForm.updateStatus(STATUS.HOME())

    @staticmethod
    def __change_init(preStatus, now_status, operationForm, configForm):
        if preStatus != now_status:
            operationForm.reset_mouse_click_l()
            operationForm.reset_mouse_click_r()
            configForm.update_pre_way_key_type()
            configForm.update_pre_go_key_type()
