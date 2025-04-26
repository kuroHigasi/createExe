import common.abstract.home.abstractDisplay as abstractDisplay
import common.layer.request.home.homeDisplayRequest as homeDisplayRequest
import common.home.service.display as sub_display
import pyd.hitJudge as hitJudge


class Display(abstractDisplay.AbstractDisplay):
    @staticmethod
    def execute(home_form, request: homeDisplayRequest.HomeSoundRequest):
        service = sub_display.Display(request)

        res_start = service.disp_start_button()
        if res_start.is_ok():
            (x, y) = res_start.data
            home_form.set_start_button(x, y)

        res_config = service.disp_config_button()
        if res_config.is_ok():
            (x, y) = res_config.data
            home_form.set_config_button(x, y)

        res_load = service.disp_load_button()
        if res_load.is_ok():
            (x, y) = res_load.data
            home_form.set_load_button(x, y)

        res_exit = service.disp_exit_button()
        if res_exit.is_ok():
            (x, y) = res_exit.data
            home_form.set_exit_button(x, y)

    @staticmethod
    def create_request_data(screen, home_form, ope_form):
        (x, y) = ope_form.get_mouse()
        (start_x, start_y, start_width, start_height) = home_form.get_start_button()
        (config_x, config_y, config_width, config_height) = home_form.get_config_button()
        (exit_x, exit_y, exit_width, exit_height) = home_form.get_exit_button()
        (load_x, load_y, load_width, load_height) = home_form.get_load_button()
        return homeDisplayRequest.HomeSoundRequest(
            hitJudge.hitJudgeSquare(start_x, start_y, start_width, start_height, x, y),
            hitJudge.hitJudgeSquare(config_x, config_y, config_width, config_height, x, y),
            hitJudge.hitJudgeSquare(exit_x, exit_y, exit_width, exit_height, x, y),
            hitJudge.hitJudgeSquare(load_x, load_y, load_width, load_height, x, y),
            home_form.get_img_list(),
            screen
        )
