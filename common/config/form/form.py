import dataclasses

import common.download as config_img
import pyd.status as status
import pyd.createPass as cPass
import common.common as cmn
import common.debug.debug as dbg
import common.config.form.buttons.form as buttons_form
import common.config.form.set.form as set_form
import pygame


@dataclasses.dataclass
class Form:
    _img_list: list
    _tab: int
    _set_form: set_form
    _buttons_form: buttons_form
    _pre_status: int
    _test_playing_flag: bool
    _test_busy_flag: bool

    def __init__(self):
        self._img_list = config_img.Download.configImag()
        self._tab = 0
        self._set_form = set_form.Form()
        self._buttons_form = buttons_form.Form()
        self._pre_status = status.HOME()
        self._test_playing_flag = False
        self._test_busy_flag = False

    @property
    def img_list(self):
        return self._img_list

    @staticmethod
    def font():
        return pygame.font.Font(str(cmn.resource_path(cPass.getFontPass("DotGothic16-Regular.ttf"))), 34)

    def get_volume(self):
        return self._set_form.volume

    def set_volume(self, volume):
        if 0 <= volume <= 100:
            self._set_form.volume = volume

    def update_pre_volume(self):
        self._set_form.volume_pre = self._set_form.volume

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
        self._set_form.way_key_type = self._set_form.way_key_type_pre
        self._set_form.go_key_type = self._set_form.go_key_type_pre
        self._set_form.volume_pre = self._set_form.volume

    def get_go_key_type(self):
        return self._set_form.go_key_type

    def set_go_key_type(self, go_key_type):
        if 0 <= go_key_type < 2:
            self._set_form.go_key_type = go_key_type

    def update_pre_go_key_type(self):
        self._set_form.go_key_type_pre = self._set_form.go_key_type

    def get_way_key_type(self):
        return self._set_form.way_key_type

    def set_way_key_type(self, way_key_type):
        if type(way_key_type) is int:
            if 0 <= way_key_type < 2:
                self._set_form.way_key_type = way_key_type
        else:
            raise ValueError

    def update_pre_way_key_type(self):
        self._set_form.way_key_type_pre = self._set_form.way_key_type

    def set_ok_button(self, x, y):
        self._buttons_form.set_ok_button_pos(x, y)

    def get_ok_button(self):
        return self._buttons_form.get_ok_button_pos() + self._buttons_form.get_ok_button_size()

    def set_back_button(self, x, y):
        self._buttons_form.set_back_button_pos(x, y)

    def get_back_button(self):
        return self._buttons_form.get_back_button_pos() + self._buttons_form.get_back_button_size()

    def set_way_button(self, index, x, y):
        if 0 <= index < 2:
            self._buttons_form.set_way_button_pos(index, x, y)
        else:
            dbg.ERROR_LOG("[configForm.set_way_button] 引数不備")

    def get_way_button(self, index):
        if 0 <= index < 2:
            return self._buttons_form.get_way_button_pos(index) + self._buttons_form.get_way_button_size(index)
        else:
            dbg.ERROR_LOG("[configForm.get_way_button] 引数不備")

    def set_go_button(self, index, x, y):
        if 0 <= index < 2:
            self._buttons_form.set_go_button_pos(index, x, y)
        else:
            dbg.ERROR_LOG("[configForm.set_go_button] 引数不備")

    def get_go_button(self, index):
        if 0 <= index < 2:
            return self._buttons_form.get_go_button_pos(index) + self._buttons_form.get_go_button_size(index)
        else:
            dbg.ERROR_LOG("[configForm.get_way_button] 引数不備")

    def set_step_button(self, index, x, y):
        if 0 <= index < 2:
            self._buttons_form.set_step_button_pos(index, x, y)
        else:
            dbg.ERROR_LOG("[configForm.set_step_button] 引数不備")

    def get_step_button(self, index):
        if 0 <= index < 2:
            return self._buttons_form.get_step_button_pos(index) + self._buttons_form.get_step_button_size(index)
        else:
            dbg.ERROR_LOG("[configForm.get_step_button] 引数不備")

    def set_tab_button(self, index, x, y):
        if 0 <= index < 2:
            self._buttons_form.set_tab_button_pos(index, x, y)
        else:
            dbg.ERROR_LOG("[configForm.set_step_button] 引数不備")

    def get_tab_button(self, index):
        if 0 <= index < 2:
            return self._buttons_form.get_tab_button_pos(index) + self._buttons_form.get_tab_button_size(index)
        else:
            dbg.ERROR_LOG("[configForm.get_step_button] 引数不備")

    def set_volume_slider(self, x, y):
        self._buttons_form.set_volume_slider_pos(x, y)

    def get_volume_slider(self):
        return self._buttons_form.get_volume_slider_pos() + self._buttons_form.get_volume_slider_size()

    def set_test_button(self, x, y):
        self._buttons_form.set_test_button_pos(x, y)

    def get_test_button(self):
        return self._buttons_form.get_test_button_pos() + self._buttons_form.get_test_button_size()

    @property
    def pre_status(self):
        return self._pre_status

    @pre_status.setter
    def pre_status(self, pre_status):
        if status.existStatus(pre_status):
            self._pre_status = pre_status

    def is_config_different(self):
        return \
            self._set_form.way_key_type_pre != self._set_form.way_key_type or \
            self._set_form.go_key_type_pre != self._set_form.go_key_type or \
            self._set_form.volume_pre != self._set_form.volume

    def create_input_data(self):
        return \
            str(self._set_form.way_key_type) + "," + \
            str(self._set_form.go_key_type) + "," + \
            str(self._set_form.volume)

    def test_playing_flag_off(self):
        self._test_playing_flag = False

    def test_playing_flag_on(self):
        self._test_playing_flag = True

    def get_test_playing_flag(self):
        return self._test_playing_flag

    def test_busy_flag_off(self):
        self._test_busy_flag = False

    def test_busy_flag_on(self):
        self._test_busy_flag = True

    def get_test_busy_flag(self):
        return self._test_busy_flag
