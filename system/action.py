import pyd.status as STATUS
import common.config.action as ConfigAction
import dungeon.action as DungeonAction
import common.save.action as SaveAction


class Action:
    def execute(statusForm, systemForm, ope_form):
        nowStatus = statusForm.NOW_STATUS()
        dungeonForm = systemForm.DUNGEON_FORM()
        configForm = systemForm.CONFIG_FORM()
        save_form = systemForm.SAVE_FORM()
        # ステータスごとのACTION分岐
        if nowStatus == STATUS.CONFIG():
            ConfigAction.Action.execute(configForm, ConfigAction.Action.create_request_data(configForm, ope_form))
        elif nowStatus == STATUS.DUNGEON():
            DungeonAction.Action.go(dungeonForm, ope_form, configForm)
            DungeonAction.Action.updateFlag(dungeonForm)
            DungeonAction.Action.useItemBox(dungeonForm, ope_form)
            DungeonAction.Action.enemyAction(dungeonForm)
            DungeonAction.Action.actionButton(dungeonForm, ope_form)
            DungeonAction.Action.retryButton(dungeonForm, ope_form)
        elif nowStatus == STATUS.SAVE():
            SaveAction.Action.execute(save_form, SaveAction.Action.create_request_data(save_form, ope_form))
