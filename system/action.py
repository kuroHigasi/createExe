import common.pyd.status as STATUS
import common.config.action as ConfigAction
import common.save.action as SaveAction


class Action:
    def execute(statusForm, systemForm, operationForm):
        nowStatus = statusForm.NOW_STATUS()
        dungeonForm = systemForm.DUNGEON_FORM()
        configForm = systemForm.CONFIG_FORM()
        saveForm = systemForm.SAVE_FORM()
        # ステータスごとのACTION分岐
        if nowStatus == STATUS.CONFIG():
            ConfigAction.Action.update(configForm, operationForm)
        elif nowStatus == STATUS.DUNGEON():
            """
                MAIN処理を実装
            """
        elif nowStatus == STATUS.SAVE():
            SaveAction.Action.save(saveForm, operationForm)
