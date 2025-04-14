import common.save.form.buttons.form as buttons_form
import common.download as IMG_LIST
import pyd.status as STATUS
import pyd.createPass as cPass
import common.common as cmn
import pygame


class Form:
    def __init__(self):
        self.__img_list = IMG_LIST.Download.saveImag()
        self.__buttons_form = buttons_form.Form()
        self.__preStatus = STATUS.HOME()
        self.__dispList = [[False, "データなし"], [False, "データなし"], [False, "データなし"]]
        self.__inputData = ""
        self.__outputData = ""

    def img_list(self):
        return self.__img_list

    def font(self):
        return pygame.font.Font(str(cmn.resource_path(cPass.getFontPass("DotGothic16-Regular.ttf"))), 34)

    def updatebuckButton(self, x, y):
        return self.__buttons_form.set_back_button_pos(x, y)

    def BUCK_BUTTON(self):
        return self.__buttons_form.get_back_button_pos() + self.__buttons_form.get_back_button_size()

    def updateHomeButton(self, x, y):
        return self.__buttons_form.set_home_button_pos(x, y)

    def HOME_BUTTON(self):
        return self.__buttons_form.get_home_button_pos() + self.__buttons_form.get_home_button_size()

    def updateSaveList(self, index, x, y):
        return self.__buttons_form.set_save_list_pos(index, x, y)

    def SAVE_LIST(self, index):
        return self.__buttons_form.get_save_list_pos(index) + self.__buttons_form.get_save_list_size(index)

    def updateLoadList(self, index, x, y):
        return self.__buttons_form.set_load_list_pos(index, x, y)

    def LOAD_LIST(self, index):
        return self.__buttons_form.get_load_list_pos(index) + self.__buttons_form.get_load_list_size(index)

    def updateDeleteList(self, index, x, y):
        return self.__buttons_form.set_delete_list_pos(index, x, y)

    def DELETE_LIST(self, index):
        return self.__buttons_form.get_delete_list_pos(index) + self.__buttons_form.get_delete_list_size(index)

    def updatePreStatus(self, status):
        self.__preStatus = status

    def PRE_STATUS(self):
        return self.__preStatus

    def updateInputData(self, data):
        self.__inputData = data

    def INPUT_DATA(self):
        return self.__inputData

    def updateOutputData(self, data):
        self.__outputData = data

    def OUTPUT_DATA(self):
        return self.__outputData

    def updateSaveDispList(self, index, data: str):
        if data == "":
            self.__dispList[index][0] = False
            self.__dispList[index][1] = "データなし"
        else:
            self.__dispList[index][0] = True
            self.__dispList[index][1] = data

    def DISP_SAVE_LIST(self, index):
        return (self.__dispList[index][0],
                self.__dispList[index][1])
