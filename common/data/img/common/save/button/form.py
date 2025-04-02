
import common.debug.debug as dbg


class Form:
    def __init__(self):
        self.__buckButton = [-1, -1, 0, 0]
        self.__homeButton = [-1, -1, 0, 0]
        self.__savelist = [[-1, -1, 0, 0], [-1, -1, 0, 0], [-1, -1, 0, 0]]
        self.__loadlist = [[-1, -1, 0, 0], [-1, -1, 0, 0], [-1, -1, 0, 0]]
        self.__deletelist = [[-1, -1, 0, 0], [-1, -1, 0, 0], [-1, -1, 0, 0]]

    def updatebuckButton(self, x, y, sizeW, sizeH):
        self.__buckButton[0] = x
        self.__buckButton[1] = y
        self.__buckButton[2] = sizeW
        self.__buckButton[3] = sizeH

    def BUCK_BUTTON(self):
        return (self.__buckButton[0],
                self.__buckButton[1],
                self.__buckButton[2],
                self.__buckButton[3])

    def updateHomeButton(self, x, y, sizeW, sizeH):
        self.__homeButton[0] = x
        self.__homeButton[1] = y
        self.__homeButton[2] = sizeW
        self.__homeButton[3] = sizeH

    def HOME_BUTTON(self):
        return (self.__homeButton[0],
                self.__homeButton[1],
                self.__homeButton[2],
                self.__homeButton[3])

    def updateSaveList(self, index, x, y, sizeW, sizeH):
        if 0 <= index and index < len(self.__savelist):
            self.__savelist[index][0] = x
            self.__savelist[index][1] = y
            self.__savelist[index][2] = sizeW
            self.__savelist[index][3] = sizeH
        else:
            dbg.ERROR_LOG("[SaveForm.updateSaveList]存在しないindex")

    def SAVE_LIST(self, index):
        if 0 <= index and index < len(self.__savelist):
            return (self.__savelist[index][0],
                    self.__savelist[index][1],
                    self.__savelist[index][2],
                    self.__savelist[index][3])
        else:
            dbg.ERROR_LOG("[SaveForm.SAVE_LIST]存在しないindex")
            return (-1, -1, 0, 0)

    def updateLoadList(self, index, x, y, sizeW, sizeH):
        if 0 <= index and index < len(self.__savelist):
            self.__loadlist[index][0] = x
            self.__loadlist[index][1] = y
            self.__loadlist[index][2] = sizeW
            self.__loadlist[index][3] = sizeH
        else:
            dbg.ERROR_LOG("[SaveForm.updateSaveList]存在しないindex")

    def LOAD_LIST(self, index):
        if 0 <= index and index < len(self.__savelist):
            return (self.__loadlist[index][0],
                    self.__loadlist[index][1],
                    self.__loadlist[index][2],
                    self.__loadlist[index][3])
        else:
            dbg.ERROR_LOG("[SaveForm.SAVE_LIST]存在しないindex")
            return (-1, -1, 0, 0)

    def updateDeleteList(self, index, x, y, sizeW, sizeH):
        if 0 <= index and index < len(self.__savelist):
            self.__deletelist[index][0] = x
            self.__deletelist[index][1] = y
            self.__deletelist[index][2] = sizeW
            self.__deletelist[index][3] = sizeH
        else:
            dbg.ERROR_LOG("[SaveForm.updateSaveList]存在しないindex")

    def DELETE_LIST(self, index):
        if 0 <= index and index < len(self.__savelist):
            return (self.__deletelist[index][0],
                    self.__deletelist[index][1],
                    self.__deletelist[index][2],
                    self.__deletelist[index][3])
        else:
            dbg.ERROR_LOG("[SaveForm.SAVE_LIST]存在しないindex")
            return (-1, -1, 0, 0)
