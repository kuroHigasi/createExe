import pyd.indexSave as INDEX
import pyd.status as STATUS
import pyd.hitJudge as judge
import common.common as cmn


class Display:
    @staticmethod
    def execute(screen, save_form, ope_form):
        img_list = save_form.img_list()
        screen.blit(img_list[INDEX.SAVE()][0], (0, 0))
        # BUCK
        Display.__dispBuckButton(screen, img_list, ope_form, save_form, 750, 670)
        # HOME
        Display.__dispHomeButton(screen, img_list, ope_form, save_form, 540, 670)
        # LIST
        Display.__dispList(screen, img_list, save_form, ope_form, 0, 150, 150)
        Display.__dispList(screen, img_list, save_form, ope_form, 1, 150, 310)
        Display.__dispList(screen, img_list, save_form, ope_form, 2, 150, 470)

    def __dispBuckButton(screen, imgList, opeForm, saveForm, posX, posY):
        Display.__dispButton(screen, imgList, opeForm, 14, posX, posY)
        saveForm.set_back_button(posX, posY)

    def __dispHomeButton(screen, imgList, opeForm, saveForm, posX, posY):
        if not (saveForm.get_pre_status() == STATUS.HOME()):
            Display.__dispButton(screen, imgList, opeForm, 4, posX, posY)
            saveForm.set_home_button(posX, posY)
        else:
            saveForm.hidden_home_button()

    def __dispList(screen, imgList, saveForm, opeForm, index, listX, listY):
        font = saveForm.font()
        (saveX, saveY) = (listX+590, listY+12)
        (loadX, loadY) = (listX+590, listY+55)
        (deleteX, deleteY) = (listX+590, listY+98)
        (textX, textY) = (listX+40, listY+75)
        (flag, text) = saveForm.DISP_SAVE_LIST(index)
        screen.blit(imgList[INDEX.LIST()][0], (listX, listY))
        if not (saveForm.get_input_data() == ""):  # SAVE BUTTON
            Display.__dispSaveButton1(screen, imgList, opeForm, 0, saveX, saveY)
            saveForm.set_save_list(index, saveX, saveY)
        else:
            Display.__dispSaveButtonNone(screen, imgList, 2, saveX, saveY)
            saveForm.hidden_save_list(index)
        if flag:  # LOAD BUTTON
            Display.__dispSaveButton1(screen, imgList, opeForm, 3, loadX, loadY)
            saveForm.set_load_list(index, loadX, loadY)
        else:
            Display.__dispSaveButtonNone(screen, imgList, 5, loadX, loadY)
            saveForm.hidden_load_list(index)
        if flag:  # DELETE BUTTON
            Display.__dispSaveButton1(screen, imgList, opeForm, 6, deleteX, deleteY)
            saveForm.set_delete_list(index, deleteX, deleteY)
        else:
            Display.__dispSaveButtonNone(screen, imgList, 8, deleteX, deleteY)
            saveForm.hidden_delete_list(index)
        Display.__dispText(screen, font, cmn.Colors.black, str(index), 160, textY)
        if flag:
            Display.__dispText(screen, font, cmn.Colors.black, text, textX, textY)
        else:
            Display.__dispText(screen, font, cmn.Colors.black, "セーブなし", textX, textY)

    def __dispButton(screen, imgList, opeForm, buttonIndex: int, posX: int, posY: int):
        (x, y) = opeForm.get_mouse()
        if judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[INDEX.BUTTON()][buttonIndex+1], (posX, posY))
        else:
            screen.blit(imgList[INDEX.BUTTON()][buttonIndex], (posX, posY))

    def __dispSaveButton1(screen, imgList, opeForm, buttonIndex: int, posX: int, posY: int):
        (x, y) = opeForm.get_mouse()
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
