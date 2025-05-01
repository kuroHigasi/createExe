import dataclasses
import common.debug.debug as dbg


@dataclasses.dataclass
class Form:
    _item_count: int
    _item_pos: list
    _item_type: list
    _item_flag: list
    _get_flag: bool
    _get_index: int

    def __init__(self):
        self._item_count = 0
        self._item_pos = []
        self._item_type = []
        self._item_flag = []
        self._get_flag = False
        self._get_index = 0

    def register(self, item_list):
        self._item_pos = []
        self._item_type = []
        self._item_flag = []
        index: int = 0
        for item in item_list:
            self._item_pos.insert(index, [item.pos[0], item.pos[1]])
            self._item_type.insert(index, item.type)
            self._item_flag.insert(index, True)
            index += 1
        self._item_count = index

    def getItem(self, pos):
        index = 0
        for itemPos in self._item_pos:
            if itemPos[0] == pos[0] and itemPos[1] == pos[1]:
                if self._item_flag[index] is True:
                    self._get_flag = True
                    self._get_index = index
                    return self._item_type[index]
            else:
                self._get_flag = False
            index += 1
        return -1

    def ITEM_GET_FLAG(self):
        return self._get_flag

    def flagOff(self):
        if self._get_flag is True:
            self._get_flag = False
            self._item_flag[self._get_index] = False
        else:
            dbg.ERROR_LOG("ITEM_FLAG False ERROR!")
