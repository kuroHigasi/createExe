import pyd.status as STATUS
import common.config.action as ConfigAction
import dungeon.action as DungeonAction
import common.save.action as SaveAction


class Action:
    @staticmethod
    def execute(status_form, system_form, ope_form):
        now_status = status_form.now_status
        dungeon_form = system_form.DUNGEON_FORM()
        config_form = system_form.CONFIG_FORM()
        save_form = system_form.SAVE_FORM()
        # ステータスごとのACTION分岐
        if now_status == STATUS.CONFIG():
            ConfigAction.Action.execute(config_form, ConfigAction.Action.create_request_data(config_form, ope_form))
        elif now_status == STATUS.DUNGEON():
            request_dungeon = DungeonAction.Action.create_request_data(dungeon_form, ope_form, config_form)
            DungeonAction.Action.execute(dungeon_form, ope_form, request_dungeon)
        elif now_status == STATUS.SAVE():
            SaveAction.Action.execute(save_form, SaveAction.Action.create_request_data(save_form, ope_form))
