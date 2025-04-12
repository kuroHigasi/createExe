import dataclasses

import common.download as config_img
import pyd.status as status
import pyd.createPass as cPass
import common.common as cmn
import common.debug.debug as dbg
import common.config.buttons.form as buttons_form
import pygame


@dataclasses.dataclass
class Form:
    _img_list: list
    _volume: int
    _pre_volume: int
    _way_key_type: int
    _pre_way_key_type: int
    _go_key_type: int
    _pre_go_key_type: int
    _tab: int
    _buttons_form: buttons_form
    _pre_status: int

    def __init__(self):
        self._img_list = config_img.Download.configImag()
        self._volume = 30
        self._pre_volume = 30
        self._way_key_type = 0
        self._pre_way_key_type = 0
        self._go_key_type = 0
        self._pre_go_key_type = 0
        self._tab = 0
        self._buttons_form = buttons_form.Form()
        self._pre_status = status.HOME()

    @property
    def img_list(self):
        return self._img_list

    @staticmethod
    def font():
        return pygame.font.Font(str(cmn.resource_path(cPass.getFontPass("DotGothic16-Regular.ttf"))), 34)

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        if 0 <= volume <= 100:
            self._volume = volume

    def update_pre_volume(self):
        self._pre_volume = self._volume

    @property
    def tab(self):
        return self._tab

    @tab.setter
    def tab(self, tab):
        if 0 <= tab < 2:
            self._tab = tab
        else:
            dbg.ERROR_LOG("[configForm.tab] 引数不備")

    def reset_config(self):
        self._way_key_type = self._pre_way_key_type
        self._go_key_type = self._pre_go_key_type
        self._volume = self._pre_volume

    @property
    def go_key_type(self):
        return self._go_key_type

    @go_key_type.setter
    def go_key_type(self, go_key_type):
        if 0 <= go_key_type < 2:
            self._go_key_type = go_key_type

    def update_pre_go_key_type(self):
        self._pre_go_key_type = self._go_key_type

    @property
    def way_key_type(self):
        return self._way_key_type

    @way_key_type.setter
    def way_key_type(self, way_key_type):
        if 0 <= way_key_type < 2:
            self._way_key_type = way_key_type

    def update_pre_way_key_type(self):
        self._pre_way_key_type = self._way_key_type

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

    def set_tab_button(self, index, x, y):
        if 0 <= index < 2:
            self._buttons_form.set_tab_button_pos(index, x, y)
        else:
            dbg.ERROR_LOG("[configForm.set_step_button] 引数不備")

    def hidden_tab_button(self, index):
        if 0 <= index < 2:
            self._buttons_form.hidden_tab_button(index)
        else:
            dbg.ERROR_LOG("[configForm.hidden_step_button] 引数不備")

    def get_tab_button(self, index):
        if 0 <= index < 2:
            return self._buttons_form.get_tab_button(index)
        else:
            dbg.ERROR_LOG("[configForm.get_step_button] 引数不備")

    @property
    def pre_status(self):
        return self._pre_status

    @pre_status.setter
    def pre_status(self, pre_status):
        if status.existStatus(pre_status):
            self._pre_status = pre_status

    def is_config_different(self):
        return \
            self._pre_way_key_type != self._way_key_type or \
            self._pre_go_key_type != self._go_key_type or \
            self._pre_volume != self._volume

    def create_input_data(self):
        return str(self._way_key_type) + "," + str(self._go_key_type) + "," + str(self._volume)
