import lib.status as STATUS
import common.config.action as ConfigAction
import dungeon.action as DungeonAction
import common.save.action as SaveAction


class Action:
    def execute(statusForm, systemForm, operationForm):
        nowStatus = statusForm.NOW_STATUS()
        dungeonForm = systemForm.DUNGEON_FORM()
        configForm = systemForm.CONFIG_FORM()
        saveForm = systemForm.SAVE_FORM()
        # ステータスごとのACTION分岐
        if (nowStatus == STATUS.CONFIG()):
            ConfigAction.Action.update(configForm, operationForm)
        elif (nowStatus == STATUS.DUNGEON()):
            DungeonAction.Action.go(dungeonForm, operationForm, configForm)
            DungeonAction.Action.updateFlag(dungeonForm)
            DungeonAction.Action.useItemBox(dungeonForm, operationForm)
            DungeonAction.Action.enemyAction(dungeonForm)
            DungeonAction.Action.actionButton(dungeonForm, operationForm)
            DungeonAction.Action.retryButton(dungeonForm, operationForm)
        elif (nowStatus == STATUS.SAVE()):
            SaveAction.Action.save(saveForm, operationForm)
