import common.config.sub.action as sub_action


class Action:
    @staticmethod
    def execute(config_form, ope_form):
        service = sub_action.Action(config_form, ope_form)
        # 設定
        service.set_tab(config_form)
        service.set_way_key_type(config_form)
        service.set_go_key_type(config_form)
        service.set_step_key_type(config_form)
        service.set_volume(config_form)
