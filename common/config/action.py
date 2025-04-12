import common.debug.debug as dbg
import common.common as cmn


class Action:
    def execute(config_form, ope_form):
        left_click = ope_form.isLeftClick()
        x, y = ope_form.MOUSE()
        click_x, click_y = ope_form.leftClickMoveMouse()
        way_key_type = config_form.way_key_type
        go_key_type = config_form.go_key_type
        way1_x, way1_y, way1_width, way1_height = config_form.get_way_button(0)
        way2_x, way2_y, way2_width, way2_height = config_form.get_way_button(1)
        go1_x, go1_y, go1_width, go1_height = config_form.get_go_button(0)
        go2_x, go2_y, go2_width, go2_height = config_form.get_go_button(1)
        step1_x, step1_y, step1_width, step1_height = config_form.get_step_button(0)
        step2_x, step2_y, step2_width, step2_height = config_form.get_step_button(1)
        tab1_x, tab1_y, tab1_width, tab1_height = config_form.get_tab_button(0)
        tab2_x, tab2_y, tab2_width, tab2_height = config_form.get_tab_button(1)
        way_key_type1_click = \
            cmn.Judge.click(way1_x, way1_y, way1_width, way1_height, x, y, click_x, click_y, left_click)
        way_key_type2_click = \
            cmn.Judge.click(way2_x, way2_y, way2_width, way2_height, x, y, click_x, click_y, left_click)
        go_key_type1_click = \
            cmn.Judge.click(go1_x, go1_y, go1_width, go1_height, x, y, click_x, click_y, left_click)
        go_key_type2_click = \
            cmn.Judge.click(go2_x, go2_y, go2_width, go2_height, x, y, click_x, click_y, left_click)
        step_key_type1_click = \
            cmn.Judge.click(step1_x, step1_y, step1_width, step1_height, x, y, click_x, click_y, left_click)
        step_key_type2_click = \
            cmn.Judge.click(step2_x, step2_y, step2_width, step2_height, x, y, click_x, click_y, left_click)
        tab1_click = \
            cmn.Judge.click(tab1_x, tab1_y, tab1_width, tab1_height, x, y, click_x, click_y, left_click)
        tab2_click = \
            cmn.Judge.click(tab2_x, tab2_y, tab2_width, tab2_height, x, y, click_x, click_y, left_click)
        # タブ_設定
        Action._set_tab(config_form, config_form.tab, tab1_click, tab2_click)
        # キータイプ1_設定
        Action._set_way_key_type(config_form, way_key_type, way_key_type1_click, way_key_type2_click)
        # キータイプ2_設定
        Action._set_go_key_type(config_form, go_key_type, go_key_type1_click, go_key_type2_click)
        # キータイプ3_設定
        Action._set_step_key_type(config_form, go_key_type, step_key_type1_click, step_key_type2_click)
        # ボリューム_設定
        Action._set_volume(config_form, x, y, click_x, click_y)

    def _set_way_key_type(config_form, wayKeyType, click1, click2):
        if wayKeyType != 0 and click1:
            config_form.way_key_type = 0
        elif wayKeyType != 1 and click2:
            config_form.way_key_type = 1
        elif click1 or click2:
            dbg.LOG("[ConfigAction._set_way_key_type]" + str(wayKeyType) + "再設定")
            if wayKeyType < 0 or 1 < wayKeyType:
                dbg.ERROR_LOG("[ConfigAction._set_way_key_type]存在しないKeyType")

    def _set_go_key_type(config_form, goKeyType, click1, click2):
        if (goKeyType != 0 and click1):
            config_form.go_key_type = 0
        elif (goKeyType != 1 and click2):
            config_form.go_key_type = 1
        elif (click1 or click2):
            dbg.LOG("[ConfigAction._set_go_key_type]" + str(goKeyType) + "再設定")
            if goKeyType < 0 or 2 < goKeyType:
                dbg.ERROR_LOG("[ConfigAction._set_go_key_type]存在しないKeyType")

    def _set_step_key_type(config_form, goKeyType, click1, click2):
        if (goKeyType != 1 and click1):
            config_form.go_key_type = 1
        elif (goKeyType != 0 and click2):
            config_form.go_key_type = 0
        elif (click1 or click2):
            dbg.LOG("[ConfigAction._set_step_key_type]" + str(goKeyType) + "再設定")
            if goKeyType < 0 or 2 < goKeyType:
                dbg.ERROR_LOG("[ConfigAction._set_step_key_type]存在しないKeyType")

    def _set_tab(config_form, tab, click1, click2):
        if tab != 0 and click1:
            config_form.tab = 0
        elif tab != 1 and click2:
            config_form.tab = 1
        elif click1 or click2:
            dbg.LOG("[ConfigAction._set_tab]" + str(tab) + "再設定")
            if tab < 0 or 2 < tab:
                dbg.ERROR_LOG("[ConfigAction._set_tab]存在しないKeyType")

    def _set_volume(config_form, x, y, click_x, click_y):
        if 180 <= click_y <= 210 and 50 <= click_x <= 450:
            if 50 <= x <= 450:
                config_form.volume = int((x - 50) / 4)
            elif x < 50:
                config_form.volume = 0
            elif 450 < x:
                config_form.volume = 100
