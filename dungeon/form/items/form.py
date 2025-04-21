import common.debug as dbg


class Form:
    def __init__(self):
        self.__itemCount = 0
        self.__itemPos = []
        self.__itemType = []
        self.__itemFlag = []
        self.__getFlag = False
        self.__getIndex = 0

    def regist(self, itemList):
        self.__itemPos = []
        self.__itemType = []
        self.__itemFlag = []
        index: int = 0
        for item in itemList:
            self.__itemPos.insert(index, [item.pos[0], item.pos[1]])
            self.__itemType.insert(index, item.type)
            self.__itemFlag.insert(index, True)
            index += 1
        self.__itemCount = index

    def ITEM_COUNT(self):
        return self.__itemCount

    def getItem(self, pos):
        index = 0
        for itemPos in self.__itemPos:
            if itemPos[0] == pos[0] and itemPos[1] == pos[1]:
                if self.__itemFlag[index] is True:
                    self.__getFlag = True
                    self.__getIndex = index
                    return self.__itemType[index]
            else:
                self.__getFlag = False
            index += 1
        return -1

    def ITEM_GET_FLAG(self):
        return self.__getFlag

    def flagOff(self):
        if self.__getFlag is True:
            self.__getFlag = False
            self.__itemFlag[self.__getIndex] = False
        else:
            dbg.ERROR_LOG("ITEM_FLAG False ERROR!")
