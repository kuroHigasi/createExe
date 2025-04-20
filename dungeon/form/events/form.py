import pyd.typeEvent as EVENT_TYPE
import dungeon.data.text.infoText as infoText


class Form:
    def __init__(self):
        self.__eventCount = 0
        self.__eventPos = []
        self.__eventWay = []
        self.__eventText = []
        self.__eventType = []
        self.__eventFlag = []

    def regist(self, eventList):
        self.__eventPos = []
        self.__eventWay = []
        self.__eventText = []
        self.__eventType = []
        self.__eventFlag = []
        index: int = 0
        for event in eventList:
            self.__eventPos.insert(index, [event.POS()[0], event.POS()[1]])
            self.__eventWay.insert(index, event.WAY())
            self.__eventText.insert(index, event.TEXT())
            self.__eventType.insert(index, event.TYPE())
            self.__eventFlag.insert(index, True)
            index += 1
        self.__eventCount = index

    def EVENT_COUNT(self):
        return self.__eventCount

    def getEventText(self, pos, way):
        index = 0
        for eventPos in self.__eventPos:
            if eventPos[0] == pos[0] and eventPos[1] == pos[1]:
                if self.__eventWay[index] == way:
                    if self.__eventFlag[index] is True:
                        if self.__eventType[index] == EVENT_TYPE.FLAVOR():
                            self.__eventFlag[index] = False
                        return (self.__eventText[index], EVENT_TYPE.getText(self.__eventType[index]))
                    else:
                        if self.__eventType[index] == EVENT_TYPE.ITEM():
                            return (infoText.ITEM_TEXT2, EVENT_TYPE.getText(EVENT_TYPE.ITEM()))
            index += 1
        return ("", "")

    def eventFlagOff(self, pos):
        index = 0
        for eventPos in self.__eventPos:
            if eventPos[0] == pos[0] and eventPos[1] == pos[1]:
                if self.__eventType[index] == EVENT_TYPE.ITEM():
                    if self.__eventFlag[index] is True:
                        self.__eventFlag[index] = False
            index += 1
