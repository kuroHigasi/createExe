import lib.createPass as cPass
import lib.indexHome as HOME_INDEX
import lib.indexConfig as CONFIG_INDEX
import lib.indexEnd as END_INDEX
import common.save.pyd.index as SAVE_INDEX
import lib.imgNum as IMG_NUM
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
    def homeImag(case='home'):
        # return
        imgList = []
        # init list load
        HOME_load = []
        BUTTON_load = []
        # download
        for file_name in range(0, IMG_NUM.HOME(), 1):
            HOME_load.insert(int(file_name), Download.__loadImg(case, "HOME", file_name))
        for file_name in range(0, IMG_NUM.BUTTON(), 1):
            BUTTON_load.insert(int(file_name), Download.__loadImg("common", "BUTTON", file_name))
        # init list img
        HOME_img = []
        BUTTON_img = []
        # img set
        for i in range(0, len(HOME_load), 1):
            HOME_img.insert(i, pygame.transform.scale(HOME_load[i], home_size))
        for i in range(0, len(BUTTON_load), 1):
            BUTTON_img.insert(i, pygame.transform.scale(BUTTON_load[i], button_size))
        imgList.insert(HOME_INDEX.HOME(), HOME_img)
        imgList.insert(HOME_INDEX.BUTTON(), BUTTON_img)
        return imgList

    def configImag(case='config'):
        # return
        imgList = []
        # init list load
        CONFIG_load = []
        CONFIG_BUTTON_load = []
        BUTTON_load = []
        SET_BUTTON_load = []
        # download
        for file_name in range(0, IMG_NUM.CONFIG(), 1):
            CONFIG_load.insert(int(file_name), Download.__loadImg(case, "CONFIG", file_name))
        for file_name in range(0, IMG_NUM.CONFIG_BUTTON(), 1):
            CONFIG_BUTTON_load.insert(int(file_name), Download.__loadImg(case, "CONFIG_BUTTON", file_name))
        for file_name in range(0, IMG_NUM.BUTTON(), 1):
            BUTTON_load.insert(int(file_name), Download.__loadImg("common", "BUTTON", file_name))
        for file_name in range(0, IMG_NUM.CONFIG_SET_BUTTON(), 1):
            SET_BUTTON_load.insert(int(file_name), Download.__loadImg(case, "SET_BUTTON", file_name))
        # init list img
        CONFIG_img = []
        CONFIG_BUTTON_img = []
        BUTTON_img = []
        SET_BUTTON_img = []
        # img set
        for i in range(0, len(CONFIG_load), 1):
            CONFIG_img.insert(i, pygame.transform.scale(CONFIG_load[i], config_size))
        for i in range(0, len(CONFIG_BUTTON_load), 1):
            CONFIG_BUTTON_img.insert(i, pygame.transform.scale(CONFIG_BUTTON_load[i], config_button_size))
        for i in range(0, len(BUTTON_load), 1):
            BUTTON_img.insert(i, pygame.transform.scale(BUTTON_load[i], button_size))
        for i in range(0, len(SET_BUTTON_load), 1):
            SET_BUTTON_img.insert(i, pygame.transform.scale(SET_BUTTON_load[i], button_size))
        imgList.insert(CONFIG_INDEX.CONFIG(),   CONFIG_img)
        imgList.insert(CONFIG_INDEX.CONFIG_BUTTON(), CONFIG_BUTTON_img)
        imgList.insert(CONFIG_INDEX.BUTTON(), BUTTON_img)
        imgList.insert(CONFIG_INDEX.SET_BUTTON(), SET_BUTTON_img)
        return imgList

    def endImag(case='end'):
        # return
        imgList = []
        # init list load
        END_load = []
        BUTTON_load = []
        # download
        for file_name in range(0, IMG_NUM.END(), 1):
            END_load.insert(int(file_name), Download.__loadImg(case, "END", file_name))
        for file_name in range(0, IMG_NUM.BUTTON(), 1):
            BUTTON_load.insert(int(file_name), Download.__loadImg("common", "BUTTON", file_name))
        # init list img
        END_img = []
        BUTTON_img = []
        # img set
        for i in range(0, len(END_load), 1):
            END_img.insert(i, pygame.transform.scale(END_load[i], home_size))
        for i in range(0, len(BUTTON_load), 1):
            BUTTON_img.insert(i, pygame.transform.scale(BUTTON_load[i], button_size))
        imgList.insert(END_INDEX.END(), END_img)
        imgList.insert(END_INDEX.BUTTON(), BUTTON_img)
        return imgList

    def saveImag(case='save'):
        # return
        imgList = []
        # init list load
        SAVE_load = []
        BUTTON_load = []
        LIST_load = []
        SAVE_BUTTON_load = []
        # download
        for file_name in range(0, IMG_NUM.SAVE(), 1):
            SAVE_load.insert(int(file_name), Download.__loadImg(case, "SAVE", file_name))
        for file_name in range(0, IMG_NUM.BUTTON(), 1):
            BUTTON_load.insert(int(file_name), Download.__loadImg("common", "BUTTON", file_name))
        for file_name in range(0, IMG_NUM.SAVE_LIST(), 1):
            LIST_load.insert(int(file_name), Download.__loadImg(case, "LIST", file_name))
        for file_name in range(0, IMG_NUM.SAVE_BUTTON(), 1):
            SAVE_BUTTON_load.insert(int(file_name), Download.__loadImg(case, "SAVE_BUTTON", file_name))
        # init list img
        SAVE_img = []
        BUTTON_img = []
        LIST_img = []
        SAVE_BUTTON_img = []
        # img set
        for i in range(0, len(SAVE_load), 1):
            SAVE_img.insert(i, pygame.transform.scale(SAVE_load[i], save_size))
        for i in range(0, len(BUTTON_load), 1):
            BUTTON_img.insert(i, pygame.transform.scale(BUTTON_load[i], button_size))
        for i in range(0, len(LIST_load), 1):
            LIST_img.insert(i, pygame.transform.scale(LIST_load[i], list_size))
        for i in range(0, len(SAVE_BUTTON_load), 1):
            SAVE_BUTTON_img.insert(i, pygame.transform.scale(SAVE_BUTTON_load[i], save_button_size))
        imgList.insert(SAVE_INDEX.SAVE(), SAVE_img)
        imgList.insert(SAVE_INDEX.BUTTON(), BUTTON_img)
        imgList.insert(SAVE_INDEX.LIST(), LIST_img)
        imgList.insert(SAVE_INDEX.SAVE_BUTTON(), SAVE_BUTTON_img)
        return imgList

    def __loadImg(case, name, number):
        return pygame.image.load(cmn.resource_path(cPass.getImgPass(case, name, number)))
