import common.common as cmn
import common.abstract.home.abstractStatus as abstractStatus
import common.layer.request.home.homeStatusRequest as homeStatusRequest
import common.home.service.status as sub_status


class Status(abstractStatus.AbstractStatus):
    @staticmethod
    def execute(status_form, request:homeStatusRequest.HomeStatusRequest):
        service = sub_status.Status(request)
        res_status = service.get_next_status()
        if res_status.is_ok() or res_status.is_do_nothing():
            status_form.updateStatus(res_status.data)

    @staticmethod
    def create_request_data(home_form, ope_form):
        left_click = ope_form.is_left_click()
        (x, y) = ope_form.get_mouse()
        (click_x, click_y) = ope_form.left_click_move_mouse()
        (start_x, start_y, start_width, start_height) = home_form.get_start_button()
        (config_x, config_y, config_width, config_height) = home_form.get_config_button()
        (exit_x, exit_y, exit_width, exit_height) = home_form.get_exit_button()
        (load_x, load_y, load_width, load_height) = home_form.get_load_button()
        return homeStatusRequest.HomeStatusRequest(
            cmn.Judge.click(start_x, start_y, start_width, start_height, x, y, click_x, click_y, left_click),
            cmn.Judge.click(config_x, config_y, config_width, config_height, x, y, click_x, click_y, left_click),
            cmn.Judge.click(exit_x, exit_y, exit_width, exit_height, x, y, click_x, click_y, left_click),
            cmn.Judge.click(load_x, load_y, load_width, load_height, x, y, click_x, click_y, left_click)
        )
