import common.debug.debug as dbg
import pyd.status as STATUS
import dungeon.status as DungeonStatus
import common.home.status as HomeStatus
import common.config.status as ConfigStatus
import common.end.status as EndStatus
import common.save.status as SaveStatus
import dungeon.convert as convert


class Status:
    def execute(statusForm, systemForm, operationForm):
        now_status = statusForm.NOW_STATUS()
        # ステータス毎 処理分岐
        if now_status == STATUS.EXIT():
            dbg.LOG("[main.STATUS]終了ステータスのため何もしない")
        elif now_status == STATUS.END():
            EndStatus.Status.nextStatus(statusForm, operationForm, systemForm.END_FORM())
        elif now_status == STATUS.HOME():
            HomeStatus.Status.nextStatus(statusForm, operationForm, systemForm.HOME_FORM())
        elif now_status == STATUS.CONFIG():
            ConfigStatus.Status.next_status(statusForm, operationForm, systemForm.CONFIG_FORM())
        elif now_status == STATUS.SAVE():
            SaveStatus.Status.nextStatus(statusForm, operationForm, systemForm.SAVE_FORM())
        elif now_status == STATUS.DUNGEON():
            DungeonStatus.Status.nextStatus(statusForm, operationForm, systemForm.DUNGEON_FORM())
            DungeonStatus.Status.updateLog(systemForm.DUNGEON_FORM())
        else:
            dbg.ERROR_LOG("[Main.STATUS]存在しないステータス: "+str(now_status))
            statusForm.updateStatus(STATUS.HOME())

    def init(statusForm, systemForm, operationForm):
        now_status = statusForm.NOW_STATUS()
        pre_status = statusForm.PRE_STATUS()
        configForm = systemForm.CONFIG_FORM()
        saveForm = systemForm.SAVE_FORM()
        dungeonForm = systemForm.DUNGEON_FORM()
        # ステータス遷移タイミング 初期化 共通処理
        Status.__changeInit(pre_status, now_status, operationForm, configForm)
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
                SaveStatus.Status.updatePreStatus(saveForm, pre_status)
                SaveStatus.Status.resetOutputData(saveForm)
                SaveStatus.Status.updateDispSaveList(saveForm)
                if pre_status == STATUS.DUNGEON():
                    inputData = convert.Convert.createInput(dungeonForm)
                    dbg.LOG("INPUT_DATA SET[" + inputData + "]")
                    SaveStatus.Status.updateInputData(saveForm, inputData)
                else:
                    dbg.LOG("INPUT_DATA RESET")
                    SaveStatus.Status.resetInputData(saveForm)
        elif now_status == STATUS.DUNGEON():
            if pre_status == STATUS.HOME():
                DungeonStatus.Status.fromHomeReset(dungeonForm)
            if pre_status == STATUS.SAVE():
                DungeonStatus.Status.fromSaveConvert(dungeonForm, saveForm.OUTPUT_DATA())
        else:
            dbg.ERROR_LOG("[Main.STATUS]存在しないステータス: "+str(now_status))
            statusForm.updateStatus(STATUS.HOME())

    def __changeInit(preStatus, now_status, operationForm, configForm):
        if preStatus != now_status:
            operationForm.reset_mouse_click_l()
            operationForm.reset_mouse_click_r()
            configForm.update_pre_way_key_type()
            configForm.update_pre_go_key_type()
