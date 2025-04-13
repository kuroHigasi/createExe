import common.common as cmn
import common.config.service.action as sub_action
import common.layer.request.request as request


class Action:
    @staticmethod
    def execute(config_form, ope_form):
        # INIT
        left_click = ope_form.is_left_click()
        x, y = ope_form.get_mouse()
        click_x, click_y = ope_form.left_click_move_mouse()
        data_list = Action.create_request_data(config_form, left_click, x, y, click_x, click_y)
        service = sub_action.Action(request.Request(data_list))
        # タブ設定
        res_tab = service.select_tab()
        if res_tab.is_ok():
            config_form.tab = res_tab.data
        # 方向キー設定
        res_way = service.select_way_key_type()
        if res_way.is_ok():
            config_form.set_way_key_type(res_way.data)
        # 直進キー設定
        res_go = service.select_go_key_type()
        if res_go.is_ok():
            config_form.set_go_key_type(res_go.data)
        # 足踏みキー設定
        res_step = service.select_step_key_type()
        if res_step.is_ok():
            config_form.set_go_key_type(res_step.data)
        # 音量設定
        res_volume = service.select_volume()
        if res_volume.is_ok():
            config_form.set_volume(res_volume.data)

    @staticmethod
    def create_request_data(config_form, left_click, x, y, click_x, click_y):
        data_list = []
        way1_x, way1_y, way1_width, way1_height = config_form.get_way_button(0)
        way2_x, way2_y, way2_width, way2_height = config_form.get_way_button(1)
        go1_x, go1_y, go1_width, go1_height = config_form.get_go_button(0)
        go2_x, go2_y, go2_width, go2_height = config_form.get_go_button(1)
        step1_x, step1_y, step1_width, step1_height = config_form.get_step_button(0)
        step2_x, step2_y, step2_width, step2_height = config_form.get_step_button(1)
        tab1_x, tab1_y, tab1_width, tab1_height = config_form.get_tab_button(0)
        tab2_x, tab2_y, tab2_width, tab2_height = config_form.get_tab_button(1)
        way1_click = cmn.Judge.click(way1_x, way1_y, way1_width, way1_height, x, y, click_x, click_y, left_click)
        way2_click = cmn.Judge.click(way2_x, way2_y, way2_width, way2_height, x, y, click_x, click_y, left_click)
        go1_click = cmn.Judge.click(go1_x, go1_y, go1_width, go1_height, x, y, click_x, click_y, left_click)
        go2_click = cmn.Judge.click(go2_x, go2_y, go2_width, go2_height, x, y, click_x, click_y, left_click)
        step1_click = cmn.Judge.click(step1_x, step1_y, step1_width, step1_height, x, y, click_x, click_y, left_click)
        step2_click = cmn.Judge.click(step2_x, step2_y, step2_width, step2_height, x, y, click_x, click_y, left_click)
        tab1_click = cmn.Judge.click(tab1_x, tab1_y, tab1_width, tab1_height, x, y, click_x, click_y, left_click)
        tab2_click = cmn.Judge.click(tab2_x, tab2_y, tab2_width, tab2_height, x, y, click_x, click_y, left_click)
        data_list.insert(0, x)  # マウス位置 X
        data_list.insert(1, click_x)  # クリック マウス位置 X
        data_list.insert(2, click_y)  # クリック マウス位置 Y
        data_list.insert(3, way1_click)  # 方向キー設定0 選択状態
        data_list.insert(4, way2_click)  # 方向キー設定1 選択状態
        data_list.insert(5, go1_click)  # 直進キー設定0 選択状態
        data_list.insert(6, go2_click)  # 直進キー設定1 選択状態
        data_list.insert(7, step1_click)  # 足踏みキー設定0 選択状態
        data_list.insert(8, step2_click)  # 足踏みキー設定1 選択状態
        data_list.insert(9, tab1_click)  # タブ選択0 選択状態
        data_list.insert(10, tab2_click)  # タブ選択1 選択状態
        data_list.insert(11, config_form.get_way_key_type())  # 方向キー設定 現在状態
        data_list.insert(12, config_form.get_go_key_type())  # 直進キー設定 現在状態
        data_list.insert(13, config_form.tab)  # タブ選択 現在状態
        return data_list
