import pyd.indexConfig as index
import pyd.hitJudge as judge
import common.common as cmn


class Display:
    def dispConfig(screen, configForm, opeForm, posX: int, posY: int):
        img_list = configForm.img_list
        font = configForm.font()
        textList1 = ["WASD操作", "方向キー操作"]
        textList2 = ["スペース押下", "エンター押下"]
        textList3 = ["エンター押下", "スペース押下"]
        wayKeyType = configForm.WAY_KEY_TYPE()
        goKeyType = configForm.GO_KEY_TYPE()
        screen.blit(img_list[index.CONFIG()][0], (posX, posY))
        # Config項目 選択
        Display.__dispConfigButton(screen, img_list, opeForm, 0, 50, 100)
        # SET BUTTON
        Display.__dispText(screen, font, "方向キー入力タイプ…" + textList1[wayKeyType-1], 50, 150)
        Display.__disp_way_key_type_button(screen, img_list, opeForm, configForm, 1, 50, 180)
        Display.__disp_way_key_type_button(screen, img_list, opeForm, configForm, 2, 260, 180)
        # SET BUTTON
        Display.__dispText(screen, font, "前進入力タイプ…" + textList2[goKeyType-1], 50, 285)
        Display.__disp_go_key_type_button(screen, img_list, opeForm, configForm, 1, 50, 320)
        Display.__disp_go_key_type_button(screen, img_list, opeForm, configForm, 2, 260, 320)
        # SET BUTTON
        Display.__dispText(screen, font, "足踏み入力タイプ…" + textList3[goKeyType-1], 50, 420)
        Display.__disp_step_key_type_button(screen, img_list, opeForm, configForm, 2, 50, 460)
        Display.__disp_step_key_type_button(screen, img_list, opeForm, configForm, 1, 260, 460)
        # OK
        if configForm.IS_DIFFERENT():
            Display.__disp_ok_button(screen, img_list, opeForm, 6, 750, 670)
            configForm.set_back_button(750, 670)
        else:
            screen.blit(img_list[index.SET_BUTTON()][5], (750, 670))
            configForm.hidden_back_button()
        # BACK
        Display.__disp_back_button(screen, img_list, opeForm, 14, 540, 670)
        configForm.set_back_button(540, 670)

    def __disp_ok_button(screen, imgList, opeForm, buttonIndex: int, posX: int, posY: int):
        (x, y) = opeForm.MOUSE()
        if judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[index.SET_BUTTON()][buttonIndex+1], (posX, posY))
        else:
            screen.blit(imgList[index.SET_BUTTON()][buttonIndex], (posX, posY))

    def __disp_back_button(screen, imgList, opeForm, buttonIndex: int, posX: int, posY: int):
        (x, y) = opeForm.MOUSE()
        if judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[index.BUTTON()][buttonIndex+1], (posX, posY))
        else:
            screen.blit(imgList[index.BUTTON()][buttonIndex], (posX, posY))

    def __disp_way_key_type_button(screen, imgList, opeForm, configForm, type: int, posX: int, posY: int):
        typeList = [1, 3]
        nowKeyType = configForm.WAY_KEY_TYPE()
        (x, y) = opeForm.MOUSE()
        # ボタン設定
        configForm.set_way_button(type-1, posX, posY)
        if judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[index.SET_BUTTON()][typeList[type-1]+1], (posX, posY))
        else:
            screen.blit(imgList[index.SET_BUTTON()][typeList[type-1]], (posX, posY))
        if nowKeyType == type:
            screen.blit(imgList[index.SET_BUTTON()][0], (posX, posY))
            configForm.hidden_way_button(type-1)

    def __disp_go_key_type_button(screen, imgList, opeForm, configForm, type: int, posX: int, posY: int):
        typeList = [1, 3]
        goKeyType = configForm.GO_KEY_TYPE()
        (x, y) = opeForm.MOUSE()
        # ボタン設定
        configForm.set_go_button(type-1, posX, posY)
        if judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[index.SET_BUTTON()][typeList[type-1]+1], (posX, posY))
        else:
            screen.blit(imgList[index.SET_BUTTON()][typeList[type-1]], (posX, posY))
        if goKeyType == type:
            screen.blit(imgList[index.SET_BUTTON()][0], (posX, posY))
            configForm.hidden_go_button(type-1)

    def __disp_step_key_type_button(screen, imgList, opeForm, configForm, type: int, posX: int, posY: int):
        typeList = [3, 1]
        stepKeyType = configForm.GO_KEY_TYPE()
        (x, y) = opeForm.MOUSE()
        # ボタン設定
        if type == 2:
            configForm.set_step_button(0, posX, posY)
        else:
            configForm.set_step_button(1, posX, posY)
        if judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[index.SET_BUTTON()][typeList[type-1]+1], (posX, posY))
        else:
            screen.blit(imgList[index.SET_BUTTON()][typeList[type-1]], (posX, posY))
        if stepKeyType == type:
            screen.blit(imgList[index.SET_BUTTON()][0], (posX, posY))
            if type == 2:
                configForm.hidden_step_button(0)
            else:
                configForm.hidden_step_button(1)

    def __dispConfigButton(screen, imgList, opeForm, buttonIndex: int, posX: int, posY: int):
        (x, y) = opeForm.MOUSE()
        if judge.hitJudgeSquare(posX, posY, 250, 25, int(x), int(y)):
            screen.blit(imgList[index.CONFIG_BUTTON()][buttonIndex+1], (posX, posY))
        else:
            screen.blit(imgList[index.CONFIG_BUTTON()][buttonIndex], (posX, posY))

    def __dispText(screen, font, text: str, x: int, y: int):
        text_surface = font.render(text, True, cmn.Colors.black)
        text_rect = text_surface.get_rect(center=(x+text_surface.get_width()/2, y))
        screen.blit(text_surface, text_rect)
