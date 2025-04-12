import common.common as cmn
import common.config.convert as convert
import pyd.status as STATUS
import pyd.save as SAVE


class Status:
    def next_status(status_form, ope_form, config_form):
        next_status = STATUS.CONFIG()
        (x, y) = ope_form.MOUSE()
        (clickX, clickY) = ope_form.leftClickMoveMouse()
        (ok_x, ok_y, ok_width, ok_height) = config_form.get_ok_button()
        (back_x, back_y, back_width, back_height) = config_form.get_back_button()
        if cmn.Judge.click(ok_x, ok_y, ok_width, ok_height, x, y, clickX, clickY, ope_form.isLeftClick()):
            cmn.SaveMethod().save(convert.Convert.createInput(config_form), SAVE.CONF_HEAD(), SAVE.CONF_TAIL())
            next_status = config_form.pre_status
        if cmn.Judge.click(back_x, back_y, back_width, back_height, x, y, clickX, clickY, ope_form.isLeftClick()):
            config_form.reset_config()
            next_status = config_form.pre_status
        status_form.updateStatus(next_status)

    def config_form_get_status(config_form, status):
        config_form.pre_status = status

    def loadConfig(config_form):
        convert.Convert.convertOutput(config_form, cmn.SaveMethod().load(SAVE.CONF_HEAD(), SAVE.CONF_TAIL()))
