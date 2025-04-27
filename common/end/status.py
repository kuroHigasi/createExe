import common.common as cmn
import common.abstract.end.abstractStatus as abstractStatus
import common.layer.request.end.endStatusRequest as endStatusRequest
import common.end.service.status as sub_status


class Status(abstractStatus.AbstractStatus):
    @staticmethod
    def execute(status_form, request):
        service = sub_status.Status(request)
        res_status = service.get_next_status()
        if res_status.is_ok() or res_status.is_do_nothing():
            status_form.update_status(res_status.data)

    @staticmethod
    def create_request_data(end_form, ope_form):
        left_click = ope_form.is_left_click()
        (x, y) = ope_form.get_mouse()
        (click_x, click_y) = ope_form.left_click_move_mouse()
        (home_x, home_y, home_width, home_height) = end_form.get_home_button()
        return endStatusRequest.EndStatusRequest(
            cmn.Judge.click(home_x, home_y, home_width, home_height, x, y, click_x, click_y, left_click)
        )
