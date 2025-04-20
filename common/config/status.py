import common.common as cmn
import common.abstract.config.abstractStatus as abstractStatus
import common.layer.request.config.configStatusRequest as configStatusRequest
import common.config.service.status as sub_status
import common.config.convert as convert
import pyd.save as save


class Status(abstractStatus.AbstractStatus):
    @staticmethod
    def execute(status_form, config_form, request):
        service = sub_status.Status(request)

        res_status = service.get_next_status()
        if res_status.is_ok():
            reset_flag, next_status = res_status.data
            if reset_flag:
                config_form.reset_config()
            status_form.updateStatus(next_status)
        elif res_status.is_do_nothing():
            reset_flag, next_status = res_status.data
            status_form.updateStatus(next_status)

    @staticmethod
    def create_request_data(config_form, ope_form):
        left_click = ope_form.is_left_click()
        (x, y) = ope_form.get_mouse()
        (click_x, click_y) = ope_form.left_click_move_mouse()
        (ok_x, ok_y, ok_width, ok_height) = config_form.get_ok_button()
        (back_x, back_y, back_width, back_height) = config_form.get_back_button()
        return configStatusRequest.ConfigDisplayRequest(
            cmn.Judge.click(ok_x, ok_y, ok_width, ok_height, x, y, click_x, click_y, left_click),
            cmn.Judge.click(back_x, back_y, back_width, back_height, x, y, click_x, click_y, left_click),
            convert.Convert.create_input(config_form),
            config_form.pre_status
        )

    @staticmethod
    def config_form_get_status(config_form, status):
        config_form.pre_status = status

    @staticmethod
    def load_config(config_form):
        convert.Convert.convert_output(config_form, cmn.SaveMethod().load(save.CONF_HEAD(), save.CONF_TAIL()))
