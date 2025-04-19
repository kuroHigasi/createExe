import pyd.indexConfig as Index
import pyd.hitJudge as Judge
from pygame_widgets.slider import Slider
import common.common as cmn


class Display:
    @staticmethod
    def execute(screen, config_form, ope_form, pos_x: int, pos_y: int):
        img_list = config_form.img_list
        font = config_form.font()
        way_type_text_list = ["WASD操作", "方向キー操作"]
        go_type_text_list = ["スペース押下", "エンター押下"]
        step_type_text_list = ["エンター押下", "スペース押下"]
        way_key_type = config_form.get_way_key_type()
        go_key_type = config_form.get_go_key_type()
        screen.blit(img_list[Index.CONFIG()][0], (pos_x, pos_y))
        # Config項目 選択
        Display.__disp_tab_button(screen, img_list, ope_form, config_form, 0, 50, 100)
        Display.__disp_tab_button(screen, img_list, ope_form, config_form, 1, 300, 100)
        if config_form.tab == 0:
            # WAY SET BUTTON
            Display.__disp_text(screen, font, "方向キー入力タイプ…" + way_type_text_list[way_key_type], 50, 150)
            Display.__disp_way_key_type_button(screen, img_list, ope_form, config_form, 0, 50, 180)
            Display.__disp_way_key_type_button(screen, img_list, ope_form, config_form, 1, 260, 180)
            # GO SET BUTTON
            Display.__disp_text(screen, font, "前進入力タイプ…" + go_type_text_list[go_key_type], 50, 285)
            Display.__disp_go_key_type_button(screen, img_list, ope_form, config_form, 0, 50, 320)
            Display.__disp_go_key_type_button(screen, img_list, ope_form, config_form, 1, 260, 320)
            # STEP SET BUTTON
            Display.__disp_text(screen, font, "足踏み入力タイプ…" + step_type_text_list[go_key_type], 50, 420)
            Display.__disp_step_key_type_button(screen, img_list, ope_form, config_form, 1, 50, 460)
            Display.__disp_step_key_type_button(screen, img_list, ope_form, config_form, 0, 260, 460)
            # VOLUME SET SLIDER
            config_form.hidden_volume_slider()
        else:
            config_form.hidden_way_button(0)
            config_form.hidden_way_button(1)
            config_form.hidden_go_button(0)
            config_form.hidden_go_button(1)
            config_form.hidden_step_button(0)
            config_form.hidden_step_button(1)
            # VOLUME SET SLIDER
            Display.__disp_volume_set_slider(screen, config_form, font, 50, 150)
        # OK
        if config_form.is_config_different():
            Display.__disp_ok_button(screen, img_list, ope_form, 6, 750, 670)
            config_form.set_ok_button(750, 670)
        else:
            screen.blit(img_list[Index.SET_BUTTON()][5], (750, 670))
            config_form.hidden_ok_button()
        # BACK
        Display.__disp_back_button(screen, img_list, ope_form, 14, 540, 670)
        config_form.set_back_button(540, 670)

    def __disp_ok_button(screen, imgList, opeForm, buttonIndex: int, posX: int, posY: int):
        (x, y) = opeForm.get_mouse()
        if Judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[Index.SET_BUTTON()][buttonIndex+1], (posX, posY))
        else:
            screen.blit(imgList[Index.SET_BUTTON()][buttonIndex], (posX, posY))

    def __disp_back_button(screen, imgList, opeForm, buttonIndex: int, posX: int, posY: int):
        (x, y) = opeForm.get_mouse()
        if Judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[Index.BUTTON()][buttonIndex+1], (posX, posY))
        else:
            screen.blit(imgList[Index.BUTTON()][buttonIndex], (posX, posY))

    def __disp_way_key_type_button(screen, imgList, opeForm, configForm, type: int, posX: int, posY: int):
        typeList = [1, 3]
        way_key_type = configForm.get_way_key_type()
        (x, y) = opeForm.get_mouse()
        # ボタン設定
        configForm.set_way_button(type, posX, posY)
        if Judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[Index.SET_BUTTON()][typeList[type]+1], (posX, posY))
        else:
            screen.blit(imgList[Index.SET_BUTTON()][typeList[type]], (posX, posY))
        if way_key_type == type:
            screen.blit(imgList[Index.SET_BUTTON()][0], (posX, posY))
            configForm.hidden_way_button(type)

    def __disp_go_key_type_button(screen, imgList, opeForm, configForm, type: int, posX: int, posY: int):
        typeList = [1, 3]
        goKeyType = configForm.get_go_key_type()
        (x, y) = opeForm.get_mouse()
        # ボタン設定
        configForm.set_go_button(type, posX, posY)
        if Judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[Index.SET_BUTTON()][typeList[type]+1], (posX, posY))
        else:
            screen.blit(imgList[Index.SET_BUTTON()][typeList[type]], (posX, posY))
        if goKeyType == type:
            screen.blit(imgList[Index.SET_BUTTON()][0], (posX, posY))
            configForm.hidden_go_button(type)

    def __disp_step_key_type_button(screen, imgList, opeForm, configForm, type: int, posX: int, posY: int):
        typeList = [3, 1]
        stepKeyType = configForm.get_go_key_type()
        (x, y) = opeForm.get_mouse()
        # ボタン設定
        if type == 1:
            configForm.set_step_button(0, posX, posY)
        else:
            configForm.set_step_button(1, posX, posY)
        if Judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[Index.SET_BUTTON()][typeList[type]+1], (posX, posY))
        else:
            screen.blit(imgList[Index.SET_BUTTON()][typeList[type]], (posX, posY))
        if stepKeyType == type:
            screen.blit(imgList[Index.SET_BUTTON()][0], (posX, posY))
            if type == 1:
                configForm.hidden_step_button(0)
            else:
                configForm.hidden_step_button(1)

    def __disp_tab_button(screen, img_list, ope_form, config_form, tab_index: int, pos_x: int, pos_y: int):
        (x, y) = ope_form.get_mouse()
        config_form.set_tab_button(tab_index, pos_x, pos_y)
        if Judge.hitJudgeSquare(pos_x, pos_y, 250, 25, int(x), int(y)):
            screen.blit(img_list[Index.CONFIG_BUTTON()][1], (pos_x, pos_y))
        else:
            if tab_index == config_form.tab:
                screen.blit(img_list[Index.CONFIG_BUTTON()][0], (pos_x, pos_y))
            else:
                screen.blit(img_list[Index.CONFIG_BUTTON()][2], (pos_x, pos_y))

    def __disp_volume_set_slider(screen, config_form, font, pos_x, pos_y):
        Display.__disp_text(screen, font, "SE VOLUME", pos_x, pos_y)
        slider = Slider(screen, pos_x, pos_y + 45, 400, 10, min=0, max=99, step=1)
        slider.setValue(config_form.get_volume())
        slider.draw()
        Display.__disp_text(screen, font, str(config_form.get_volume()), pos_x + 425, pos_y + 40)
        config_form.set_volume_slider(50, 180)

    def __disp_text(screen, font, text: str, x: int, y: int):
        text_surface = font.render(text, True, cmn.Colors.black)
        text_rect = text_surface.get_rect(center=(x+text_surface.get_width()/2, y))
        screen.blit(text_surface, text_rect)
