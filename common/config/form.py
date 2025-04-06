import common.img as ConfigImg
import common.pyd.status as STATUS
import common.pyd.createPass as cPass
import common.common as cmn
import pygame


class Form:
    def __init__(self):
        self.__imgList = ConfigImg.Download.configImag()
        self.__volume = 1
        self.__nowWayKeyType = 1
        self.__preWayKeyType = 1
        self.__nowGoKeyType = 1
        self.__preGoKeyType = 1
        self.__okButton = (-1, -1)
        self.__buckButton = (-1, -1)
        self.__preStatus = STATUS.HOME()
        self.__font = pygame.font.Font(cmn.resource_path(cPass.getFontPass("DotGothic16-Regular.ttf")), 34)

    def IMG_LIST(self):
        return self.__imgList

    def FONT(self):
        return self.__font

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

    def updateOkButton(self, x, y):
        self.__okButton = (x, y)

    def OK_BUTTON(self):
        return self.__okButton

    def updateBuckButton(self, x, y):
        self.__buckButton = (x, y)

    def BUCK_BUTTON(self):
        return self.__buckButton

    def updatePreStatus(self, status):
        self.__preStatus = status

    def PRE_STATUS(self):
        return self.__preStatus

    def IS_DIFFERENT(self):
        return not (self.__preWayKeyType == self.__nowWayKeyType) or not (self.__preGoKeyType == self.__nowGoKeyType)

    def CREATE_INPUTDATA(self):
        return str(self.__nowWayKeyType) + "," + str(self.__nowGoKeyType)
