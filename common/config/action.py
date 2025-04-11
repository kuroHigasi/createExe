import common.debug.debug as dbg
import common.common as cmn


class Action:
    def update(configForm, opeForm):
        left_click = opeForm.isLeftClick()
        x, y = opeForm.MOUSE()
        clickX, clickY = opeForm.leftClickMoveMouse()
        way_key_type = configForm.WAY_KEY_TYPE()
        go_key_type = configForm.GO_KEY_TYPE()
        way1_x, way1_y, way1_width, way1_height = configForm.get_way_button(0)
        way2_x, way2_y, way2_width, way2_height = configForm.get_way_button(1)
        go1_x, go1_y, go1_width, go1_height = configForm.get_go_button(0)
        go2_x, go2_y, go2_width, go2_height = configForm.get_go_button(1)
        step1_x, step1_y, step1_width, step1_height = configForm.get_step_button(0)
        step2_x, step2_y, step2_width, step2_height = configForm.get_step_button(1)
        wayKeyType1Click = \
            cmn.Judge.click(way1_x, way1_y, way1_width, way1_height, x, y, clickX, clickY, left_click)
        wayKeyType2Click = \
            cmn.Judge.click(way2_x, way2_y, way2_width, way2_height, x, y, clickX, clickY, left_click)
        GoKeyType1Click = \
            cmn.Judge.click(go1_x, go1_y, go1_width, go1_height, x, y, clickX, clickY, left_click)
        GoKeyType2Click = \
            cmn.Judge.click(go2_x, go2_y, go2_width, go2_height, x, y, clickX, clickY, left_click)
        StepKeyType1Click = \
            cmn.Judge.click(step1_x, step1_y, step1_width, step1_height, x, y, clickX, clickY, left_click)
        StepKeyType2Click = \
            cmn.Judge.click(step2_x, step2_y, step2_width, step2_height, x, y, clickX, clickY, left_click)
        # キータイプ1_設定
        Action._set_way_key_type(configForm, way_key_type, wayKeyType1Click, wayKeyType2Click)
        # キータイプ2_設定
        Action._set_go_key_type(configForm, go_key_type, GoKeyType1Click, GoKeyType2Click)
        # キータイプ3_設定
        Action._set_step_key_type(configForm, go_key_type, StepKeyType1Click, StepKeyType2Click)

    def _set_way_key_type(configForm, wayKeyType, click1, click2):
        if wayKeyType != 1 and click1:
            configForm.updateNowWayKeyType(1)
        elif wayKeyType != 2 and click2:
            configForm.updateNowWayKeyType(2)
        elif click1 or click2:
            dbg.LOG("[ConfigAction.update]" + str(wayKeyType) + "再設定")
            if wayKeyType < 0 or 2 < wayKeyType:
                dbg.ERROR_LOG("[ConfigAction.update]存在しないKeyType")

    def _set_go_key_type(configForm, goKeyType, click1, click2):
        if (goKeyType != 1 and click1):
            configForm.updateNowGoKeyType(1)
        elif (goKeyType != 2 and click2):
            configForm.updateNowGoKeyType(2)
        elif (click1 or click2):
            dbg.LOG("[ConfigAction.update]" + str(goKeyType) + "再設定")
            if goKeyType < 0 or 2 < goKeyType:
                dbg.ERROR_LOG("[ConfigAction.update]存在しないKeyType")

    def _set_step_key_type(configForm, goKeyType, click1, click2):
        if (goKeyType != 2 and click1):
            configForm.updateNowGoKeyType(2)
        elif (goKeyType != 1 and click2):
            configForm.updateNowGoKeyType(1)
        elif (click1 or click2):
            dbg.LOG("[ConfigAction.update]" + str(goKeyType) + "再設定")
            if goKeyType < 0 or 2 < goKeyType:
                dbg.ERROR_LOG("[ConfigAction.update]存在しないKeyType")
