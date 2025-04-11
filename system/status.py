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
        nowStatus = statusForm.NOW_STATUS()
        dungeonForm = systemForm.DUNGEON_FORM()
        # ステータス毎 処理分岐
        if (statusForm.NOW_STATUS() == STATUS.EXIT()):
            dbg.LOG("[main.STATUS]終了ステータスのため何もしない")
        elif (statusForm.NOW_STATUS() == STATUS.END()):
            EndStatus.Status.nextStatus(statusForm, operationForm, systemForm.END_FORM())
        elif (statusForm.NOW_STATUS() == STATUS.HOME()):
            HomeStatus.Status.nextStatus(statusForm, operationForm, systemForm.HOME_FORM())
        elif (statusForm.NOW_STATUS() == STATUS.CONFIG()):
            ConfigStatus.Status.nextStatus(statusForm, operationForm, systemForm.CONFIG_FORM())
        elif (statusForm.NOW_STATUS() == STATUS.SAVE()):
            SaveStatus.Status.nextStatus(statusForm, operationForm, systemForm.SAVE_FORM())
        elif (nowStatus == STATUS.DUNGEON()):
            DungeonStatus.Status.nextStatus(statusForm, operationForm, dungeonForm)
            DungeonStatus.Status.updateLog(dungeonForm)
        else:
            dbg.ERROR_LOG("[Main.STATUS]存在しないステータス: "+str(nowStatus))
            statusForm.updateStatus(STATUS.HOME())

    def init(statusForm, systemForm, operationForm):
        nowStatus = statusForm.NOW_STATUS()
        preStatus = statusForm.PRE_STATUS()
        configForm = systemForm.CONFIG_FORM()
        saveForm = systemForm.SAVE_FORM()
        dungeonForm = systemForm.DUNGEON_FORM()
        # ステータス遷移タイミング 初期化 共通処理
        Status.__changeInit(preStatus, nowStatus, operationForm, configForm)
        # ステータス毎 処理分岐
        if (statusForm.NOW_STATUS() == STATUS.EXIT()):
            if (preStatus != STATUS.EXIT()):
                dbg.LOG("[main.EXIT]終了ステータスのため何もしない")
        elif (statusForm.NOW_STATUS() == STATUS.END()):
            if (preStatus != STATUS.END()):
                dbg.LOG("[main.END]初期化処理なし")
        elif (statusForm.NOW_STATUS() == STATUS.HOME()):
            if (preStatus != STATUS.HOME()):
                dbg.LOG("[main.HOME]初期化処理なし")
        elif (statusForm.NOW_STATUS() == STATUS.CONFIG()):
            if (preStatus != STATUS.CONFIG()):
                ConfigStatus.Status.config_form_get_status(configForm, preStatus)
                ConfigStatus.Status.loadConfig(configForm)
        elif (statusForm.NOW_STATUS() == STATUS.SAVE()):
            if (preStatus != STATUS.SAVE()):
                SaveStatus.Status.updatePreStatus(saveForm, preStatus)
                SaveStatus.Status.resetOutputData(saveForm)
                SaveStatus.Status.updateDispSaveList(saveForm)
                if preStatus == STATUS.DUNGEON():
                    inputData = convert.Convert.createInput(dungeonForm)
                    dbg.LOG("INPUT_DATA SET[" + inputData + "]")
                    SaveStatus.Status.updateInputData(saveForm, inputData)
                else:
                    dbg.LOG("INPUT_DATA RESET")
                    SaveStatus.Status.resetInputData(saveForm)
        elif (nowStatus == STATUS.DUNGEON()):
            if preStatus == STATUS.HOME():
                DungeonStatus.Status.fromHomeReset(dungeonForm)
            if preStatus == STATUS.SAVE():
                DungeonStatus.Status.fromSaveConvert(dungeonForm, saveForm.OUTPUT_DATA())
        else:
            dbg.ERROR_LOG("[Main.STATUS]存在しないステータス: "+str(nowStatus))
            statusForm.updateStatus(STATUS.HOME())

    def __changeInit(preStatus, nowStatus, operationForm, configForm):
        if preStatus != nowStatus:
            operationForm.resetMouseClickL()
            operationForm.resetMouseClickR()
            configForm.updatePreWayKeyType()
            configForm.updatePreGoKeyType()
