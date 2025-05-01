import copy

import pyd.typeEvent as EVENT_TYPE
import dungeon.data.text.infoText as infoText


class Form:
    def __init__(self):
        self.__eventCount = 0
        self.__event_list = []

    def registry(self, event_list):
        self.__eventCount = len(event_list)
        self.__event_list = copy.deepcopy(event_list)

    def get_text(self, pos, way):
        for event in self.__event_list:
            if event.pos[0] == pos[0] and event.pos[1] == pos[1]:
                if event.way == way:
                    if event.flag is True:
                        if event.type == EVENT_TYPE.FLAVOR():
                            event.flag = False
                        return event.text, EVENT_TYPE.getText(event.type)
                    else:
                        if event.type == EVENT_TYPE.ITEM():
                            return infoText.ITEM_TEXT2, EVENT_TYPE.getText(EVENT_TYPE.ITEM())
        return "", ""

    def flag_off(self, pos):
        for event in self.__event_list:
            if event.pos[0] == pos[0] and event.pos[1] == pos[1]:
                if event.type == EVENT_TYPE.ITEM():
                    if event.flag is True:
                        event.flag = False
