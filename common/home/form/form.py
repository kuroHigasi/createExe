import dataclasses

import common.download as download
import common.home.form.buttons.form as buttons_form


@dataclasses.dataclass
class Form:
    _img_list: list
    _buttons_form: buttons_form.Form

    def __init__(self):
        self.__img_list = download.Download.homeImag()
        self._buttons_form = buttons_form.Form()

    def get_img_list(self):
        return self.__img_list

    def set_config_button(self, x, y):
        self._buttons_form.set_config_button_pos(x, y)

    def get_config_button(self):
        return self._buttons_form.get_config_button_pos() + self._buttons_form.get_config_button_size()

    def set_start_button(self, x, y):
        self._buttons_form.set_start_button_pos(x, y)

    def get_start_button(self):
        return self._buttons_form.get_start_button_pos() + self._buttons_form.get_start_button_size()

    def set_exit_button(self, x, y):
        self._buttons_form.set_exit_button_pos(x, y)

    def get_exit_button(self):
        return self._buttons_form.get_exit_button_pos() + self._buttons_form.get_exit_button_size()

    def set_load_button(self, x, y):
        self._buttons_form.set_load_button_pos(x, y)

    def get_load_button(self):
        return self._buttons_form.get_load_button_pos() + self._buttons_form.get_load_button_size()
