import dataclasses
import pyd.calc as calc
import common.debug.debug as dbg


@dataclasses.dataclass
class OperationForm:
    __directionKey: int
    __space: int
    __enter: int
    __click: int
    __mouseX: int
    __mouseY: int
    __mouseXclickR: int
    __mouseYclickR: int
    __mouseXclickL: int
    __mouseYclickL: int

    def __init__(self):
        self.__directionKey = 0b0000
        self.__space = 0
        self.__enter = 0
        self.__click = 0b0000
        self.__mouseX = 0
        self.__mouseY = 0
        self.__mouseXclickR = -1
        self.__mouseYclickR = -1
        self.__mouseXclickL = -1
        self.__mouseYclickL = -1

    def reset(self):
        self.__directionKey = 0b0000

    def up_on(self):
        self.__directionKey = calc.bitmask(self.__directionKey, 0b0001)

    def up_off(self):
        self.__directionKey = calc.maskAndRight(self.__directionKey, 0b1110, 0)

    def get_up(self):
        return calc.maskAndRight(self.__directionKey, 0b0001, 0) == 0b0001

    def left_on(self):
        self.__directionKey = calc.bitmask(self.__directionKey, 0b0010)

    def left_off(self):
        self.__directionKey = calc.maskAndRight(self.__directionKey, 0b1101, 0)

    def get_left(self):
        return calc.maskAndRight(self.__directionKey, 0b0010, 1) == 0b0001

    def right_on(self):
        self.__directionKey = calc.bitmask(self.__directionKey, 0b0100)

    def right_off(self):
        self.__directionKey = calc.maskAndRight(self.__directionKey, 0b1011, 0)

    def get_right(self):
        return calc.maskAndRight(self.__directionKey, 0b0100, 2) == 0b0001

    def down_on(self):
        self.__directionKey = calc.bitmask(self.__directionKey, 0b1000)

    def down_off(self):
        self.__directionKey = calc.maskAndRight(self.__directionKey, 0b0111, 0)

    def get_down(self):
        return calc.maskAndRight(self.__directionKey, 0b1000, 3) == 0b0001

    def space_pn(self):
        self.__space = 1

    def space_off(self):
        self.__space = 0

    def get_space(self):
        return self.__space == 1

    def enter_on(self):
        self.__enter = 1

    def enter_off(self):
        self.__enter = 0

    def get_enter(self):
        return self.__enter == 1

    def right_click_on(self):
        if calc.maskAndRight(self.__click, 0b0001, 0) == 0:
            self.__mouseXclickR = self.__mouseX
            self.__mouseYclickR = self.__mouseY
            dbg.LOG("RIGHT CLICK ONESHOT")
        self.__click = calc.bitmask(self.__click, 0b0001)

    def right_click_off(self):
        if calc.maskAndRight(self.__click, 0b0001, 0) == 1:
            self.__mouseXclickR = -1
            self.__mouseYclickR = -1
        self.__click = calc.maskAndRight(self.__click, 0b1110, 0)

    def is_right_click(self):
        return calc.maskAndRight(self.__click, 0b0001, 0) == 1

    def right_click_move_mouse(self):
        return self.__mouseXclickR, self.__mouseYclickR

    def left_click_on(self):
        if calc.maskAndRight(self.__click, 0b0010, 1) == 0:
            self.__mouseXclickL = self.__mouseX
            self.__mouseYclickL = self.__mouseY
            dbg.LOG("LEFT CLICK ONESHOT")
        self.__click = calc.bitmask(self.__click, 0b0010)

    def left_click_off(self):
        if calc.maskAndRight(self.__click, 0b0010, 1) == 1:
            self.__mouseXclickL = -1
            self.__mouseYclickL = -1
        self.__click = calc.maskAndRight(self.__click, 0b1101, 0)

    def is_left_click(self):
        return calc.maskAndRight(self.__click, 0b0010, 1) == 1

    def left_click_move_mouse(self):
        return self.__mouseXclickL, self.__mouseYclickL

    def reset_click(self):
        self.__click = 0b0000
        self.__mouseXclickR = 0
        self.__mouseYclickR = 0
        self.__mouseXclickL = 0
        self.__mouseYclickL = 0

    def set_mouse(self, x, y):
        self.__mouseX = x
        self.__mouseY = y

    def resetMouseClickR(self):
        self.__mouseXclickR = -1
        self.__mouseYclickR = -1

    def resetMouseClickL(self):
        self.__mouseXclickL = -1
        self.__mouseYclickL = -1

    def get_mouse(self):
        return self.__mouseX, self.__mouseY
