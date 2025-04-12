import common.common as cmn
import common.config.convert as convert
import pyd.status as status
import pyd.save as save


class Status:
    @staticmethod
    def next_status(status_form, ope_form, config_form):
        next_status = status.CONFIG()
        (x, y) = ope_form.MOUSE()
        (click_x, click_y) = ope_form.leftClickMoveMouse()
        (ok_x, ok_y, ok_width, ok_height) = config_form.get_ok_button()
        (back_x, back_y, back_width, back_height) = config_form.get_back_button()
        if cmn.Judge.click(ok_x, ok_y, ok_width, ok_height, x, y, click_x, click_y, ope_form.isLeftClick()):
            cmn.SaveMethod().save(convert.Convert.create_input(config_form), save.CONF_HEAD(), save.CONF_TAIL())
            next_status = config_form.pre_status
        if cmn.Judge.click(back_x, back_y, back_width, back_height, x, y, click_x, click_y, ope_form.isLeftClick()):
            config_form.reset_config()
            next_status = config_form.pre_status
        status_form.updateStatus(next_status)

    @staticmethod
    def config_form_get_status(config_form, status):
        config_form.pre_status = status

    @staticmethod
    def load_config(config_form):
        convert.Convert.convert_output(config_form, cmn.SaveMethod().load(save.CONF_HEAD(), save.CONF_TAIL()))
