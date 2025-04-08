import pyd.indexConfig as index
import pyd.hitJudge as judge
import common.common as cmn


class Display:
    def dispConfig(screen, configForm, opeForm, posX: int, posY: int):
        imgList = configForm.IMG_LIST()
        font = configForm.FONT()
        textList1 = ["WASD操作", "方向キー操作"]
        textList2 = ["スペース押下", "エンター押下"]
        textList3 = ["エンター押下", "スペース押下"]
        wayKeyType = configForm.WAY_KEY_TYPE()
        goKeyType = configForm.GO_KEY_TYPE()
        screen.blit(imgList[index.CONFIG()][0], (posX, posY))
        # Config項目 選択
        Display.__dispConfigButton(screen, imgList, opeForm, 0, 50, 100)
        # SET BUTTON
        Display.__dispText(screen, font, "方向キー入力タイプ…" + textList1[wayKeyType-1], 50, 150)
        Display.__dispWayKeyTypeButton(screen, imgList, opeForm, configForm, 1, 50, 180)
        Display.__dispWayKeyTypeButton(screen, imgList, opeForm, configForm, 2, 260, 180)
        # SET BUTTON
        Display.__dispText(screen, font, "前進入力タイプ…" + textList2[goKeyType-1], 50, 285)
        Display.__dispGoKeyTypeButton(screen, imgList, opeForm, configForm, 1, 50, 320)
        Display.__dispGoKeyTypeButton(screen, imgList, opeForm, configForm, 2, 260, 320)
        # SET BUTTON
        Display.__dispText(screen, font, "足踏み入力タイプ…" + textList3[goKeyType-1], 50, 420)
        Display.__dispStepKeyTypeButton(screen, imgList, opeForm, configForm, 2, 50, 460)
        Display.__dispStepKeyTypeButton(screen, imgList, opeForm, configForm, 1, 260, 460)
        # OK
        if configForm.IS_DIFFERENT():
            Display.__dispSetButton(screen, imgList, opeForm, 6, 750, 670)
            configForm.updateOkButton(750, 670)
        else:
            screen.blit(imgList[index.SET_BUTTON()][5], (750, 670))
            configForm.updateOkButton(-1, -1)
        # BUCK
        Display.__dispButton(screen, imgList, opeForm, 14, 540, 670)
        configForm.updateBuckButton(540, 670)

    def __dispSetButton(screen, imgList, opeForm, buttonIndex: int, posX: int, posY: int):
        (x, y) = opeForm.MOUSE()
        if judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[index.SET_BUTTON()][buttonIndex+1], (posX, posY))
        else:
            screen.blit(imgList[index.SET_BUTTON()][buttonIndex], (posX, posY))

    def __dispButton(screen, imgList, opeForm, buttonIndex: int, posX: int, posY: int):
        (x, y) = opeForm.MOUSE()
        if judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[index.BUTTON()][buttonIndex+1], (posX, posY))
        else:
            screen.blit(imgList[index.BUTTON()][buttonIndex], (posX, posY))

    def __dispWayKeyTypeButton(screen, imgList, opeForm, configForm, type: int, posX: int, posY: int):
        typeList = [1, 3]
        nowKeyType = configForm.WAY_KEY_TYPE()
        (x, y) = opeForm.MOUSE()
        if judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[index.SET_BUTTON()][typeList[type-1]+1], (posX, posY))
        else:
            screen.blit(imgList[index.SET_BUTTON()][typeList[type-1]], (posX, posY))
        if nowKeyType == type:
            screen.blit(imgList[index.SET_BUTTON()][0], (posX, posY))

    def __dispGoKeyTypeButton(screen, imgList, opeForm, configForm, type: int, posX: int, posY: int):
        typeList = [1, 3]
        goKeyType = configForm.GO_KEY_TYPE()
        (x, y) = opeForm.MOUSE()
        if judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[index.SET_BUTTON()][typeList[type-1]+1], (posX, posY))
        else:
            screen.blit(imgList[index.SET_BUTTON()][typeList[type-1]], (posX, posY))
        if goKeyType == type:
            screen.blit(imgList[index.SET_BUTTON()][0], (posX, posY))

    def __dispStepKeyTypeButton(screen, imgList, opeForm, configForm, type: int, posX: int, posY: int):
        typeList = [3, 1]
        stepKeyType = configForm.GO_KEY_TYPE()
        (x, y) = opeForm.MOUSE()
        if judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[index.SET_BUTTON()][typeList[type-1]+1], (posX, posY))
        else:
            screen.blit(imgList[index.SET_BUTTON()][typeList[type-1]], (posX, posY))
        if stepKeyType == type:
            screen.blit(imgList[index.SET_BUTTON()][0], (posX, posY))

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
