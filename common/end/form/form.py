import common.download as end_img
import common.end.form.buttons.form as buttons_form
import pyd.createPass as cPass
import common.common as cmn
import pygame


class Form:
    def __init__(self):
        self.__img_list = end_img.Download.end_img_list()
        self.__buttons_form = buttons_form.Form()
        self.__action_count = 0

    def get_img_list(self):
        return self.__img_list

    def set_action_count(self, dungeon_form):
        self.__action_count = dungeon_form.get_total_count()

    def get_count(self):
        return self.__action_count

    @staticmethod
    def get_font():
        return pygame.font.Font(str(cmn.resource_path(cPass.getFontPass("DotGothic16-Regular.ttf"))), 34)

    def set_home_button(self, x, y):
        return self.__buttons_form.set_home_button_pos(x, y)

    def get_home_button(self):
        return self.__buttons_form.get_home_button_pos() + self.__buttons_form.get_home_button_size()
