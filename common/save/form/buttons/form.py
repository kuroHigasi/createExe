import dataclasses

import common.button.form as button_form
import common.debug.debug as dbg


@dataclasses.dataclass
class Form:
    __back_button: button_form
    __home_button: button_form
    __save_list: list
    __load_list: list
    __delete_list: list

    def __init__(self):
        self.__back_button = button_form.Form(-1, -1, 200, 80)
        self.__home_button = button_form.Form(-1, -1, 200, 80)
        self.__save_list = \
            [button_form.Form(-1, -1, 100, 40),
			 button_form.Form(-1, -1, 100, 40),
             button_form.Form(-1, -1, 100, 40)]
        self.__load_list = \
            [button_form.Form(-1, -1, 100, 40),
             button_form.Form(-1, -1, 100, 40),
             button_form.Form(-1, -1, 100, 40)]
        self.__delete_list = \
            [button_form.Form(-1, -1, 100, 40),
             button_form.Form(-1, -1, 100, 40),
             button_form.Form(-1, -1, 100, 40)]

    def set_back_button_pos(self, x, y):
        self.__back_button.x = x
        self.__back_button.y = y

    def get_back_button_pos(self):
        return \
            self.__back_button.x,\
            self.__back_button.y

    def get_back_button_size(self):
        return \
            self.__back_button.width, \
            self.__back_button.height

    def set_home_button_pos(self, x, y):
        self.__home_button.x = x
        self.__home_button.y = y

    def get_home_button_pos(self):
        return \
            self.__home_button.x, \
            self.__home_button.y

    def get_home_button_size(self):
        return \
            self.__home_button.width, \
            self.__home_button.height

    def set_save_list_pos(self, index, x, y):
        if 0 <= index < len(self.__save_list):
            self.__save_list[index].x = x
            self.__save_list[index].y = y
        else:
            dbg.ERROR_LOG("[SaveForm.updateSaveList]存在しないindex")

    def get_save_list_pos(self, index):
        if 0 <= index < len(self.__save_list):
            return (self.__save_list[index].x,
                    self.__save_list[index].y)
        else:
            dbg.ERROR_LOG("[SaveForm.SAVE_LIST]存在しないindex")
            return -1, -1

    def get_save_list_size(self, index):
        if 0 <= index < len(self.__save_list):
            return (self.__save_list[index].width,
                    self.__save_list[index].height)
        else:
            dbg.ERROR_LOG("[SaveForm.SAVE_LIST]存在しないindex")
            return 0, 0

    def set_load_list_pos(self, index, x, y):
        if 0 <= index < len(self.__load_list):
            self.__load_list[index].x = x
            self.__load_list[index].y = y
        else:
            dbg.ERROR_LOG("[SaveForm.updateSaveList]存在しないindex")
            return -1, -1

    def get_load_list_pos(self, index):
        if 0 <= index < len(self.__load_list):
            return (self.__load_list[index].x,
                    self.__load_list[index].y)
        else:
            dbg.ERROR_LOG("[SaveForm.SAVE_LIST]存在しないindex")
            return -1, -1

    def get_load_list_size(self, index):
        if 0 <= index < len(self.__load_list):
            return (self.__load_list[index].width,
                    self.__load_list[index].height)
        else:
            dbg.ERROR_LOG("[SaveForm.SAVE_LIST]存在しないindex")
            return 0, 0

    def set_delete_list_pos(self, index, x, y):
        if 0 <= index < len(self.__delete_list):
            self.__delete_list[index].x = x
            self.__delete_list[index].y = y
        else:
            dbg.ERROR_LOG("[SaveForm.updateSaveList]存在しないindex")

    def get_delete_list_pos(self, index):
        if 0 <= index < len(self.__delete_list):
            return (self.__delete_list[index].x,
                    self.__delete_list[index].y)
        else:
            dbg.ERROR_LOG("[SaveForm.SAVE_LIST]存在しないindex")
            return -1, -1

    def get_delete_list_size(self, index):
        if 0 <= index < len(self.__delete_list):
            return (self.__delete_list[index].width,
                    self.__delete_list[index].height)
        else:
            dbg.ERROR_LOG("[SaveForm.SAVE_LIST]存在しないindex")
            return 0, 0
