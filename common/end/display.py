import common.abstract.end.abstractDisplay as abstractDisplay
import common.layer.request.end.endDisplayRequest as endDisplayRequest
import common.end.service.display as sub_display
import pyd.hitJudge as hitJudge


class Display(abstractDisplay.AbstractDisplay):
    @staticmethod
    def execute(end_form, request: endDisplayRequest.EndDisplayRequest):
        service = sub_display.Display(request)
        service.disp_result()
        res_home = service.disp_home_button()
        if res_home.is_ok():
            x, y = res_home.data
            end_form.set_home_button(x, y)

    @staticmethod
    def create_request_data(screen, end_form, ope_form):
        (x, y) = ope_form.get_mouse()
        (home_x, home_y, home_width, home_height) = end_form.get_home_button()
        return endDisplayRequest.EndDisplayRequest(
            screen,
            hitJudge.hitJudgeSquare(home_x, home_y, home_width, home_height, x, y),
            end_form.get_count(),
            end_form.get_font(),
            end_form.get_img_list()
        )
