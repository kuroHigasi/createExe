import pyd.hitJudge as Judge
import common.abstract.config.abstractDisplay as abstractDisplay
import common.layer.request.config.configDisplayRequest as configDisplayRequest
import common.config.form.form as form
import common.config.service.display as sub_display


class Display(abstractDisplay.AbstractDisplay):
    @staticmethod
    def execute(config_form, request: configDisplayRequest.ConfigDisplayRequest):
        service = sub_display.Display(request)

        res_back = service.disp_back_button()
        if res_back.is_ok():
            x, y = res_back.data
            config_form.set_back_button(x, y)

        res_ok = service.disp_ok_button()
        if res_ok.is_ok():
            x, y = res_ok.data
            config_form.set_ok_button(x, y)

        for index in (0, 1, 1):
            res_tab = service.disp_tab(index)
            if res_tab.is_ok():
                x, y = res_tab.data
                config_form.set_tab_button(index, x, y)
            res_way = service.disp_way_button(index)
            if res_way.is_ok():
                x, y = res_way.data
                config_form.set_way_button(index, x, y)
            res_go = service.disp_go_button(index)
            if res_go.is_ok():
                x, y = res_go.data
                config_form.set_go_button(index, x, y)
            res_step = service.disp_step_button(index)
            if res_step.is_ok():
                x, y = res_step.data
                config_form.set_step_button(index, x, y)

        res_volume = service.disp_volume_slider()
        if res_volume.is_ok():
            x, y = res_volume.data
            config_form.set_volume_slider(x, y)

        res_test = service.disp_test_button()
        if res_test.is_ok():
            x, y = res_test.data
            config_form.set_test_button(x, y)

    @staticmethod
    def create_request_data(screen, config_form: form, ope_form):
        (x, y) = ope_form.get_mouse()
        way1_x, way1_y, way1_width, way1_height = config_form.get_way_button(0)
        way2_x, way2_y, way2_width, way2_height = config_form.get_way_button(1)
        go1_x, go1_y, go1_width, go1_height = config_form.get_go_button(0)
        go2_x, go2_y, go2_width, go2_height = config_form.get_go_button(1)
        step1_x, step1_y, step1_width, step1_height = config_form.get_step_button(0)
        step2_x, step2_y, step2_width, step2_height = config_form.get_step_button(1)
        tab1_x, tab1_y, tab1_width, tab1_height = config_form.get_tab_button(0)
        tab2_x, tab2_y, tab2_width, tab2_height = config_form.get_tab_button(1)
        ok_x, ok_y, ok_width, ok_height = config_form.get_ok_button()
        back_x, back_y, back_width, back_height = config_form.get_back_button()
        test_x, test_y, test_width, test_height = config_form.get_test_button()
        return configDisplayRequest.ConfigDisplayRequest(
            screen,
            config_form.font(),
            config_form.img_list,
            Judge.hitJudgeSquare(way1_x, way1_y, way1_width, way1_height, x, y),
            Judge.hitJudgeSquare(way2_x, way2_y, way2_width, way2_height, x, y),
            Judge.hitJudgeSquare(go1_x, go1_y, go1_width, go1_height, x, y),
            Judge.hitJudgeSquare(go2_x, go2_y, go2_width, go2_height, x, y),
            Judge.hitJudgeSquare(step1_x, step1_y, step1_width, step1_height, x, y),
            Judge.hitJudgeSquare(step2_x, step2_y, step2_width, step2_height, x, y),
            Judge.hitJudgeSquare(tab1_x, tab1_y, tab1_width, tab1_height, x, y),
            Judge.hitJudgeSquare(tab2_x, tab2_y, tab2_width, tab2_height, x, y),
            Judge.hitJudgeSquare(ok_x, ok_y, ok_width, ok_height, x, y),
            Judge.hitJudgeSquare(back_x, back_y, back_width, back_height, x, y),
            config_form.get_way_key_type(),
            config_form.get_go_key_type(),
            config_form.tab,
            config_form.get_volume(),
            config_form.is_config_different(),
            Judge.hitJudgeSquare(test_x, test_y, test_width, test_height, x, y)
        )
