import pyd.status as STATUS
import common.config.action as config_action
import dungeon.action as dungeon_action
import common.save.action as save_action


class Action:
    @staticmethod
    def execute(status_form, system_form, ope_form):
        now_status = status_form.now_status
        dungeon_form = system_form.dungeon_form
        config_form = system_form.config_form
        save_form = system_form.save_form
        # ステータスごとのACTION分岐
        if now_status == STATUS.CONFIG():
            request_config = config_action.Action.create_request_data(config_form, ope_form)
            config_action.Action.execute(config_form, request_config)
        elif now_status == STATUS.DUNGEON():
            request_dungeon = dungeon_action.Action.create_request_data(dungeon_form, ope_form, config_form)
            dungeon_action.Action.execute(dungeon_form, ope_form, request_dungeon)
        elif now_status == STATUS.SAVE():
            request_save = save_action.Action.create_request_data(save_form, ope_form)
            save_action.Action.execute(save_form, request_save)
