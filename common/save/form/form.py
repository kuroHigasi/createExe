import common.save.form.buttons.form as buttons_form
import common.download as IMG_LIST
import pyd.status as STATUS
import pyd.createPass as cPass
import common.common as cmn
import pygame


class Form:
    def __init__(self):
        self.__img_list = IMG_LIST.Download.save_img_list()
        self.__buttons_form = buttons_form.Form()
        self.__pre_status = STATUS.HOME()
        self.__dispList = [[False, "データなし"], [False, "データなし"], [False, "データなし"]]
        self.__inputData = ""
        self.__outputData = ""

    def img_list(self):
        return self.__img_list

    @staticmethod
    def font():
        return pygame.font.Font(str(cmn.resource_path(cPass.getFontPass("DotGothic16-Regular.ttf"))), 34)

    def set_back_button(self, x, y):
        return self.__buttons_form.set_back_button_pos(x, y)

    def get_back_button(self):
        return self.__buttons_form.get_back_button_pos() + self.__buttons_form.get_back_button_size()

    def get_back_button_width(self):
        width, height = self.__buttons_form.get_back_button_size()
        return width

    def get_back_button_height(self):
        width, height = self.__buttons_form.get_back_button_size()
        return height

    def set_home_button(self, x, y):
        return self.__buttons_form.set_home_button_pos(x, y)

    def hidden_home_button(self):
        return self.__buttons_form.set_home_button_pos(-1, -1)

    def get_home_button(self):
        return self.__buttons_form.get_home_button_pos() + self.__buttons_form.get_home_button_size()

    def get_home_button_width(self):
        width, height = self.__buttons_form.get_home_button_size()
        return width

    def get_home_button_height(self):
        width, height = self.__buttons_form.get_home_button_size()
        return height

    def set_save_list(self, index, x, y):
        return self.__buttons_form.set_save_list_pos(index, x, y)

    def hidden_save_list(self, index):
        return self.__buttons_form.set_save_list_pos(index, -1, -1)

    def get_save_list(self, index):
        return self.__buttons_form.get_save_list_pos(index) + self.__buttons_form.get_save_list_size(index)

    def get_save_list_width(self, index):
        width, height = self.__buttons_form.get_save_list_size(index)
        return width

    def get_save_list_height(self, index):
        width, height = self.__buttons_form.get_save_list_size(index)
        return height

    def set_load_list(self, index, x, y):
        return self.__buttons_form.set_load_list_pos(index, x, y)

    def hidden_load_list(self, index):
        return self.__buttons_form.set_load_list_pos(index, -1, -1)

    def get_load_list(self, index):
        return self.__buttons_form.get_load_list_pos(index) + self.__buttons_form.get_load_list_size(index)

    def set_delete_list(self, index, x, y):
        return self.__buttons_form.set_delete_list_pos(index, x, y)

    def hidden_delete_list(self, index):
        return self.__buttons_form.set_delete_list_pos(index, -1, -1)

    def get_delete_list(self, index):
        return self.__buttons_form.get_delete_list_pos(index) + self.__buttons_form.get_delete_list_size(index)

    def set_pre_status(self, status):
        self.__pre_status = status

    def get_pre_status(self):
        return self.__pre_status

    def set_input_data(self, data):
        self.__inputData = data

    def get_input_data(self):
        return self.__inputData

    def set_output_data(self, data):
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
