import common.save.pyd.index as INDEX
import lib.status as STATUS
import lib.hitJudge as judge
import common.common as cmn


class Display:
    def dispSave(screen, saveForm, opeForm, posX: int, posY: int):
        imgList = saveForm.IMG_LIST()
        screen.blit(imgList[INDEX.SAVE()][0], (posX, posY))
        # BUCK
        Display.__dispBuckButton(screen, imgList, opeForm, saveForm, posX+750, posY+670)
        # HOME
        Display.__dispHomeButton(screen, imgList, opeForm, saveForm, posX+540, posY+670)
        # LIST
        Display.__dispList(screen, imgList, saveForm, opeForm, 0, posX+150, posY+150)
        Display.__dispList(screen, imgList, saveForm, opeForm, 1, posX+150, posY+310)
        Display.__dispList(screen, imgList, saveForm, opeForm, 2, posX+150, posY+470)

    def __dispBuckButton(screen, imgList, opeForm, saveForm, posX, posY):
        Display.__dispButton(screen, imgList, opeForm, 14, posX, posY)
        saveForm.updatebuckButton(posX, posY)

    def __dispHomeButton(screen, imgList, opeForm, saveForm, posX, posY):
        if not (saveForm.PRE_STATUS() == STATUS.HOME()):
            Display.__dispButton(screen, imgList, opeForm, 4, posX, posY)
            saveForm.updateHomeButton(posX, posY)
        else:
            saveForm.updateHomeButton(-1, -1)

    def __dispList(screen, imgList, saveForm, opeForm, index, listX, listY):
        font = saveForm.FONT()
        (saveX, saveY) = (listX+590, listY+12)
        (loadX, loadY) = (listX+590, listY+55)
        (deleteX, deleteY) = (listX+590, listY+98)
        (textX, textY) = (listX+40, listY+75)
        (flag, text) = saveForm.DISP_SAVE_LIST(index)
        screen.blit(imgList[INDEX.LIST()][0], (listX, listY))
        if not (saveForm.INPUT_DATA() == ""):  # SAVE BUTTON
            Display.__dispSaveButton1(screen, imgList, opeForm, 0, saveX, saveY)
            saveForm.updateSaveList(index, saveX, saveY)
        else:
            Display.__dispSaveButtonNone(screen, imgList, 2, saveX, saveY)
            saveForm.updateSaveList(index, -1, -1)
        if flag:  # LOAD BUTTON
            Display.__dispSaveButton1(screen, imgList, opeForm, 3, loadX, loadY)
            saveForm.updateLoadList(index, loadX, loadY)
        else:
            Display.__dispSaveButtonNone(screen, imgList, 5, loadX, loadY)
            saveForm.updateLoadList(index, -1, -1)
        if flag:  # DELETE BUTTON
            Display.__dispSaveButton1(screen, imgList, opeForm, 6, deleteX, deleteY)
            saveForm.updateDeleteList(index, deleteX, deleteY)
        else:
            Display.__dispSaveButtonNone(screen, imgList, 8, deleteX, deleteY)
            saveForm.updateDeleteList(index, -1, -1)
        Display.__dispText(screen, font, cmn.Colors.black, str(index), 160, textY)
        if flag:
            Display.__dispText(screen, font, cmn.Colors.black, text, textX, textY)
        else:
            Display.__dispText(screen, font, cmn.Colors.black, "セーブなし", textX, textY)

    def __dispButton(screen, imgList, opeForm, buttonIndex: int, posX: int, posY: int):
        (x, y) = opeForm.MOUSE()
        if judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[INDEX.BUTTON()][buttonIndex+1], (posX, posY))
        else:
            screen.blit(imgList[INDEX.BUTTON()][buttonIndex], (posX, posY))

    def __dispSaveButton1(screen, imgList, opeForm, buttonIndex: int, posX: int, posY: int):
        (x, y) = opeForm.MOUSE()
        if judge.hitJudgeSquare(posX, posY, 100, 40, int(x), int(y)):
            screen.blit(imgList[INDEX.SAVE_BUTTON()][buttonIndex+1], (posX, posY))
        else:
            screen.blit(imgList[INDEX.SAVE_BUTTON()][buttonIndex], (posX, posY))

    def __dispSaveButtonNone(screen, imgList, buttonIndex: int, posX: int, posY: int):
        screen.blit(imgList[INDEX.SAVE_BUTTON()][buttonIndex], (posX, posY))

    def __dispText(screen, font, color, text: str, x: int, y: int):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x+text_surface.get_width()/2, y))
        screen.blit(text_surface, text_rect)
