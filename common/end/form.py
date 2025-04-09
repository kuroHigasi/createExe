import common.download as EndImg
import common.end.button.form as ButtonForm
import pyd.createPass as cPass
import common.common as cmn
import pygame


class Form:
    def __init__(self):
        self.__imgList = EndImg.Download.endImag()
        self.__buttonForm = ButtonForm.Form()
        self.__font = pygame.font.Font(cmn.resource_path(cPass.getFontPass("DotGothic16-Regular.ttf")), 34)
        self.__actionCount = 0

    def IMG_LIST(self):
        return self.__imgList

    def updateActionCount(self, dungeonForm):
        self.__actionCount = dungeonForm.TOTAL_COUNT()

    def COUNT(self):
        return self.__actionCount

    def FONT(self):
        return self.__font

    def updateHomeButton(self, x, y):
        return self.__buttonForm.updateHomeButton(x, y, 200, 80)

    def HOME_BUTTON(self):
        return self.__buttonForm.HOME_BUTTON()
