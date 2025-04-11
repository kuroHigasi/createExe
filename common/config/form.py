import common.download as ConfigImg
import pyd.status as STATUS
import pyd.createPass as cPass
import common.common as cmn
import common.debug.debug as dbg
import common.config.buttons.form as buttons_form
import pygame


class Form:
    def __init__(self):
        self._img_list = ConfigImg.Download.configImag()
        self._volume = 1
        self.__nowWayKeyType = 1
        self.__preWayKeyType = 1
        self.__nowGoKeyType = 1
        self.__preGoKeyType = 1
        self._buttons_form = buttons_form.Form()
        self.__pre_status = STATUS.HOME()

    @property
    def img_list(self):
        return self._img_list

    @staticmethod
    def font():
        return pygame.font.Font(cmn.resource_path(cPass.getFontPass("DotGothic16-Regular.ttf")), 34)

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        if 0 <= volume <= 1:
            self._volume = volume

    def buckKeyType(self):
        self.__nowWayKeyType = self.__preWayKeyType
        self.__nowGoKeyType = self.__preGoKeyType

    def updateNowGoKeyType(self, type: int):
        self.__nowGoKeyType = type

    def updatePreGoKeyType(self):
        self.__preGoKeyType = self.__nowGoKeyType

    def GO_KEY_TYPE(self):
        return self.__nowGoKeyType

    def updateNowWayKeyType(self, type: int):
        self.__nowWayKeyType = type

    def updatePreWayKeyType(self):
        self.__preWayKeyType = self.__nowWayKeyType

    def WAY_KEY_TYPE(self):
        return self.__nowWayKeyType

    def set_ok_button(self, x, y):
        self._buttons_form.set_ok_button_pos(x, y)

    def hidden_ok_button(self):
        self._buttons_form.hidden_ok_button()

    def get_ok_button(self):
        return self._buttons_form.get_ok_button()

    def set_back_button(self, x, y):
        self._buttons_form.set_back_button_pos(x, y)

    def hidden_back_button(self):
        self._buttons_form.hidden_back_button()

    def get_back_button(self):
        return self._buttons_form.get_back_button()

    def set_way_button(self, index, x, y):
        if 0 <= index < 2:
            self._buttons_form.set_way_button_pos(index, x, y)
        else:
            dbg.ERROR_LOG("[configForm.set_way_button] 引数不備")

    def hidden_way_button(self, index):
        if 0 <= index < 2:
            self._buttons_form.hidden_way_button(index)
        else:
            dbg.ERROR_LOG("[configForm.hidden_way_button] 引数不備")

    def get_way_button(self, index):
        if 0 <= index < 2:
            return self._buttons_form.get_way_button(index)
        else:
            dbg.ERROR_LOG("[configForm.get_way_button] 引数不備")

    def set_go_button(self, index, x, y):
        if 0 <= index < 2:
            self._buttons_form.set_go_button_pos(index, x, y)
        else:
            dbg.ERROR_LOG("[configForm.set_go_button] 引数不備")

    def hidden_go_button(self, index):
        if 0 <= index < 2:
            self._buttons_form.hidden_go_button(index)
        else:
            dbg.ERROR_LOG("[configForm.hidden_go_button] 引数不備")

    def get_go_button(self, index):
        if 0 <= index < 2:
            return self._buttons_form.get_go_button(index)
        else:
            dbg.ERROR_LOG("[configForm.get_way_button] 引数不備")

    def set_step_button(self, index, x, y):
        if 0 <= index < 2:
            self._buttons_form.set_step_button_pos(index, x, y)
        else:
            dbg.ERROR_LOG("[configForm.set_step_button] 引数不備")

    def hidden_step_button(self, index):
        if 0 <= index < 2:
            self._buttons_form.hidden_step_button(index)
        else:
            dbg.ERROR_LOG("[configForm.hidden_step_button] 引数不備")

    def get_step_button(self, index):
        if 0 <= index < 2:
            return self._buttons_form.get_step_button(index)
        else:
            dbg.ERROR_LOG("[configForm.get_step_button] 引数不備")

    @property
    def pre_status(self):
        return self.__pre_status

    @pre_status.setter
    def pre_status(self, status):
        self.__pre_status = status

    def IS_DIFFERENT(self):
        return not (self.__preWayKeyType == self.__nowWayKeyType) or not (self.__preGoKeyType == self.__nowGoKeyType)

    def CREATE_INPUTDATA(self):
        return str(self.__nowWayKeyType) + "," + str(self.__nowGoKeyType)
