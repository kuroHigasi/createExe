import dataclasses
import common.button.form as button_form
import pyd.typeItem as typeItem


@dataclasses.dataclass
class Form:
    __pre_box: list
    __pre_box_num: list
    __pre_num: int
    __box: list
    __box_num: list
    _box_button: list
    _box_use_flag: list
    __box_use_turn: list
    __flag: bool
    __max: int
    __num: int

    def __init__(self):
        self.__pre_box = [typeItem.RADER(), -1, -1]
        self.__pre_box_num = [1, 0, 0]
        self.__pre_num = 1
        self.__box = [typeItem.RADER(), -1, -1]
        self.__box_num = [1, 0, 0]
        self._box_button = \
            [button_form.Form(-1, -1, 60, 60),
             button_form.Form(-1, -1, 60, 60),
             button_form.Form(-1, -1, 60, 60)]
        self._box_use_flag = [True, False, False]
        self.__box_use_turn = [-2, -1, -1]
        self.__flag = False
        self.__max = 3
        self.__num = 1

    def reset(self):
        self.__box = [self.__pre_box[0], self.__pre_box[1], self.__pre_box[2]]
        self.__box_num = [self.__pre_box_num[0], self.__pre_box_num[1], self.__pre_box_num[2]]
        self.__num = self.__pre_num
        for index in range(0, 3, 1):
            self._box_button[index].x = -1
            self._box_button[index].y = -1
        self._box_use_flag = [True, False, False]
        self.__box_use_turn = [-2, -1, -1]

    def clear(self):
        self.__pre_box = [typeItem.RADER(), -1, -1]
        self.__pre_box_num = [1, 0, 0]
        self.__pre_num = 1
        self.__box = [typeItem.RADER(), -1, -1]
        self.__box_num = [1, 0, 0]
        self.__num = 1
        for index in range(0, 3, 1):
            self._box_button[index].x = -1
            self._box_button[index].y = -1
        self._box_use_flag = [True, False, False]
        self.__box_use_turn = [-2, -1, -1]

    def item_set(self, item):
        flag = False
        item_index = -1
        if self.__num < self.__max:
            # 同じアイテム存在チェック
            for index in range(0, self.__num+1, 1):
                if self.__box[index] == item:
                    item_index = index
                    flag = True
            # アイテム被りなし
            if not flag:
                for index in range(0, self.__num+1, 1):
                    if self.__box[index] == -1:
                        self.__box[index] = item
                        self.__box_num[index] += 1
                        self.__num += 1
                        break
            else:
                self.__box_num[item_index] += 1
            return True
        else:
            return False

    def watch(self, num):
        return self.__box[num], self.__box_num[num]

    def pre_watch(self, num):
        return self.__pre_box[num], self.__pre_box_num[num]

    def update_pre(self):
        self.__pre_box = [self.__box[0], self.__box[1], self.__box[2]]
        self.__pre_box_num = [self.__box_num[0], self.__box_num[1], self.__box_num[2]]
        self.__pre_num = self.__num

    def set_box_button_pos(self, index, x, y):
        if index < self.__max and 0 < self.__num:
            if self.__box[index] != -1:
                self._box_button[index].x = x
                self._box_button[index].y = y
            else:
                self._box_button[index].x = -1
                self._box_button[index].y = -1

    def get_box_button_pos(self, index):
        if index < self.__max and 0 < self.__num:
            return (self._box_button[index].x,
                    self._box_button[index].y)
        else:
            return -1, -1

    def get_box_button_size(self, index):
        if index < self.__max and 0 < self.__num:
            return (self._box_button[index].width,
                    self._box_button[index].height)
        else:
            return 60, 60

    def use_item(self, index):
        if index < self.__max and 0 < self.__num:
            if self.__box[index] != -1 and not (self._box_use_flag[index]):
                self._box_use_flag[index] = True
                self.__box_use_turn[index] = 10

    def get_use_flag(self, index):
        if index < self.__max and 0 < self.__num:
            return self._box_use_flag[index]
        else:
            return False

    def flag_on(self):
        self.__flag = True

    def get_flag(self):
        return self.__flag

    def use_turn_count_up(self):
        if self.__flag:
            self.__flag = False
        if self._box_use_flag[0]:
            if -1 < self.__box_use_turn[0]:
                self.__box_use_turn[0] -= 1
            if self.__box_use_turn[0] == 0:
                self._box_use_flag[0] = False
                self.__box_num[0] -= 1
                if self.__box_num[0] == 0:
                    self.__num -= 1
                    self.__box[0] = -1
        if self._box_use_flag[1]:
            if -1 < self.__box_use_turn[1]:
                self.__box_use_turn[1] -= 1
            if self.__box_use_turn[1] == 0:
                self._box_use_flag[1] = False
                self.__box_num[1] -= 1
                if self.__box_num[1] == 0:
                    self.__num -= 1
                    self.__box[1] = -1
        if self._box_use_flag[2]:
            if -1 < self.__box_use_turn[2]:
                self.__box_use_turn[2] -= 1
            if self.__box_use_turn[2] == 0:
                self._box_use_flag[2] = False
                self.__box_num[2] -= 1
                if self.__box_num[2] == 0:
                    self.__num -= 1
                    self.__box[2] = -1

    def get_pre_num(self):
        return self.__pre_num
