import pyd.createPass as cPass
import pyd.indexHome as HOME_INDEX
import pyd.indexConfig as CONFIG_INDEX
import pyd.indexEnd as END_INDEX
import pyd.indexSave as SAVE_INDEX
import pyd.imgNum as IMG_NUM
import common.common as cmn
import pygame
import pygame.locals


home_size = (1000, 800)
save_size = (1000, 800)
button_size = (200, 80)
save_button_size = (100, 40)
list_size = (700, 150)
config_size = (1000, 800)
config_button_size = (250, 25)


class Download:
    @staticmethod
    def home_img_list(case='home'):
        # return
        img_list = []
        # init list load
        home_load = []
        button_load = []
        # download
        for file_name in range(0, IMG_NUM.HOME(), 1):
            home_load.insert(int(file_name), Download.__load_img(case, "HOME", file_name))
        for file_name in range(0, IMG_NUM.BUTTON(), 1):
            button_load.insert(int(file_name), Download.__load_img("common", "BUTTON", file_name))
        # init list img
        home_img = []
        button_img = []
        # img set
        for i in range(0, len(home_load), 1):
            home_img.insert(i, pygame.transform.scale(home_load[i], home_size))
        for i in range(0, len(button_load), 1):
            button_img.insert(i, pygame.transform.scale(button_load[i], button_size))
        img_list.insert(HOME_INDEX.HOME(), home_img)
        img_list.insert(HOME_INDEX.BUTTON(), button_img)
        return img_list

    @staticmethod
    def config_img_list(case='config'):
        # return
        img_list = []
        # init list load
        config_load = []
        config_button_load = []
        button_load = []
        set_button_load = []
        # download
        for file_name in range(0, IMG_NUM.CONFIG(), 1):
            config_load.insert(int(file_name), Download.__load_img(case, "CONFIG", file_name))
        for file_name in range(0, IMG_NUM.CONFIG_BUTTON(), 1):
            config_button_load.insert(int(file_name), Download.__load_img(case, "CONFIG_BUTTON", file_name))
        for file_name in range(0, IMG_NUM.BUTTON(), 1):
            button_load.insert(int(file_name), Download.__load_img("common", "BUTTON", file_name))
        for file_name in range(0, IMG_NUM.CONFIG_SET_BUTTON(), 1):
            set_button_load.insert(int(file_name), Download.__load_img(case, "SET_BUTTON", file_name))
        # init list img
        config_img = []
        config_button_img = []
        button_img = []
        set_button_img = []
        # img set
        for i in range(0, len(config_load), 1):
            config_img.insert(i, pygame.transform.scale(config_load[i], config_size))
        for i in range(0, len(config_button_load), 1):
            config_button_img.insert(i, pygame.transform.scale(config_button_load[i], config_button_size))
        for i in range(0, len(button_load), 1):
            button_img.insert(i, pygame.transform.scale(button_load[i], button_size))
        for i in range(0, len(set_button_load), 1):
            set_button_img.insert(i, pygame.transform.scale(set_button_load[i], button_size))
        img_list.insert(CONFIG_INDEX.CONFIG(),   config_img)
        img_list.insert(CONFIG_INDEX.CONFIG_BUTTON(), config_button_img)
        img_list.insert(CONFIG_INDEX.BUTTON(), button_img)
        img_list.insert(CONFIG_INDEX.SET_BUTTON(), set_button_img)
        return img_list

    @staticmethod
    def end_img_list(case='end'):
        # return
        img_list = []
        # init list load
        end_load = []
        button_load = []
        # download
        for file_name in range(0, IMG_NUM.END(), 1):
            end_load.insert(int(file_name), Download.__load_img(case, "END", file_name))
        for file_name in range(0, IMG_NUM.BUTTON(), 1):
            button_load.insert(int(file_name), Download.__load_img("common", "BUTTON", file_name))
        # init list img
        end_img = []
        button_img = []
        # img set
        for i in range(0, len(end_load), 1):
            end_img.insert(i, pygame.transform.scale(end_load[i], home_size))
        for i in range(0, len(button_load), 1):
            button_img.insert(i, pygame.transform.scale(button_load[i], button_size))
        img_list.insert(END_INDEX.END(), end_img)
        img_list.insert(END_INDEX.BUTTON(), button_img)
        return img_list

    @staticmethod
    def save_img_list(case='save'):
        # return
        img_list = []
        # init list load
        save_load = []
        button_load = []
        list_load = []
        save_button_load = []
        # download
        for file_name in range(0, IMG_NUM.SAVE(), 1):
            save_load.insert(int(file_name), Download.__load_img(case, "SAVE", file_name))
        for file_name in range(0, IMG_NUM.BUTTON(), 1):
            button_load.insert(int(file_name), Download.__load_img("common", "BUTTON", file_name))
        for file_name in range(0, IMG_NUM.SAVE_LIST(), 1):
            list_load.insert(int(file_name), Download.__load_img(case, "LIST", file_name))
        for file_name in range(0, IMG_NUM.SAVE_BUTTON(), 1):
            save_button_load.insert(int(file_name), Download.__load_img(case, "SAVE_BUTTON", file_name))
        # init list img
        save_img = []
        button_img = []
        list_img = []
        save_button_img = []
        # img set
        for i in range(0, len(save_load), 1):
            save_img.insert(i, pygame.transform.scale(save_load[i], save_size))
        for i in range(0, len(button_load), 1):
            button_img.insert(i, pygame.transform.scale(button_load[i], button_size))
        for i in range(0, len(list_load), 1):
            list_img.insert(i, pygame.transform.scale(list_load[i], list_size))
        for i in range(0, len(save_button_load), 1):
            save_button_img.insert(i, pygame.transform.scale(save_button_load[i], save_button_size))
        img_list.insert(SAVE_INDEX.SAVE(), save_img)
        img_list.insert(SAVE_INDEX.BUTTON(), button_img)
        img_list.insert(SAVE_INDEX.LIST(), list_img)
        img_list.insert(SAVE_INDEX.SAVE_BUTTON(), save_button_img)
        return img_list

    @staticmethod
    def sound() -> list:
        """

        :rtype: list
        """
        sound_list: list = []
        sound_list.insert(0, Download.__load_mp3("common", "CLICK", 0))
        sound_list.insert(1, Download.__load_mp3("common", "TEST", 0))
        return sound_list

    @staticmethod
    def __load_img(case, name, number):
        return pygame.image.load(str(cmn.resource_path(cPass.getImgPass(case, name, number))))

    @staticmethod
    def __load_mp3(case, name, number):
        return cmn.resource_path(cPass.getMp3Pass(case, name, number))
