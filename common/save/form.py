import common.save.button.form as ButtonForm
import common.download as IMG_LIST
import pyd.status as STATUS
import pyd.createPass as cPass
import common.common as cmn
import pygame


class Form:
    def __init__(self):
        self.__imgList = IMG_LIST.Download.saveImag()
        self.__buttonForm = ButtonForm.Form()
        self.__preStatus = STATUS.HOME()
        self.__dispList = [[False, "データなし"], [False, "データなし"], [False, "データなし"]]
        self.__font = pygame.font.Font(cmn.resource_path(cPass.getFontPass("DotGothic16-Regular.ttf")), 34)
        self.__inputData = ""
        self.__outputData = ""

    def IMG_LIST(self):
        return self.__imgList

    def FONT(self):
        return self.__font

    def updatebuckButton(self, x, y):
        return self.__buttonForm.updatebuckButton(x, y, 200, 80)

    def BUCK_BUTTON(self):
        return self.__buttonForm.BUCK_BUTTON()

    def updateHomeButton(self, x, y):
        return self.__buttonForm.updateHomeButton(x, y, 200, 80)

    def HOME_BUTTON(self):
        return self.__buttonForm.HOME_BUTTON()

    def updateSaveList(self, index, x, y):
        return self.__buttonForm.updateSaveList(index, x, y, 100, 40)

    def SAVE_LIST(self, index):
        return self.__buttonForm.SAVE_LIST(index)

    def updateLoadList(self, index, x, y):
        return self.__buttonForm.updateLoadList(index, x, y, 100, 40)

    def LOAD_LIST(self, index):
        return self.__buttonForm.LOAD_LIST(index)

    def updateDeleteList(self, index, x, y):
        return self.__buttonForm.updateDeleteList(index, x, y, 100, 40)

    def DELETE_LIST(self, index):
        return self.__buttonForm.DELETE_LIST(index)

    def updatePreStatus(self, status):
        self.__preStatus = status

    def PRE_STATUS(self):
        return self.__preStatus

    def updateInputData(self, data):
        self.__inputData = data

    def INPUT_DATA(self):
        return self.__inputData

    def updateOutputData(self, data):
        self.__outputData = data

    def OUTPUT_DATA(self):
        return self.__outputData

    def updateSaveDispList(self, index, data: str):
        if data == "":
            self.__dispList[index][0] = False
            self.__dispList[index][1] = "データなし"
        else:
            self.__dispList[index][0] = True
            self.__dispList[index][1] = data

    def DISP_SAVE_LIST(self, index):
        return (self.__dispList[index][0],
                self.__dispList[index][1])
