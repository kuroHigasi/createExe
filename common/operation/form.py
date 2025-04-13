import dataclasses
import pyd.calc as calc
import common.operation.key.form as key_form
import common.operation.mouse.form as mouse_form
import common.debug.debug as dbg


@dataclasses.dataclass
class OperationForm:
    __key: key_form
    __mouse: mouse_form

    def __init__(self):
        self.__key = key_form.Form()
        self.__mouse = mouse_form.Form()

    def reset(self):
        self.__key.direction_key = 0b0000

    def up_on(self):
        self.__key.direction_key = calc.bitmask(self.__key.direction_key, 0b0001)

    def up_off(self):
        self.__key.direction_key = calc.maskAndRight(self.__key.direction_key, 0b1110, 0)

    def get_up(self):
        return calc.maskAndRight(self.__key.direction_key, 0b0001, 0) == 0b0001

    def left_on(self):
        self.__key.direction_key = calc.bitmask(self.__key.direction_key, 0b0010)

    def left_off(self):
        self.__key.direction_key = calc.maskAndRight(self.__key.direction_key, 0b1101, 0)

    def get_left(self):
        return calc.maskAndRight(self.__key.direction_key, 0b0010, 1) == 0b0001

    def right_on(self):
        self.__key.direction_key = calc.bitmask(self.__key.direction_key, 0b0100)

    def right_off(self):
        self.__key.direction_key = calc.maskAndRight(self.__key.direction_key, 0b1011, 0)

    def get_right(self):
        return calc.maskAndRight(self.__key.direction_key, 0b0100, 2) == 0b0001

    def down_on(self):
        self.__key.direction_key = calc.bitmask(self.__key.direction_key, 0b1000)

    def down_off(self):
        self.__key.direction_key = calc.maskAndRight(self.__key.direction_key, 0b0111, 0)

    def get_down(self):
        return calc.maskAndRight(self.__key.direction_key, 0b1000, 3) == 0b0001

    def space_pn(self):
        self.__key.space = True

    def space_off(self):
        self.__key.space = False

    def get_space(self):
        return self.__key.space

    def enter_on(self):
        self.__key.enter = True

    def enter_off(self):
        self.__key.enter = False

    def get_enter(self):
        return self.__key.enter

    def right_click_on(self):
        if not self.__mouse.click_r:
            self.__mouse.click_r_pos_x = self.__mouse.mouse_pointer_x
            self.__mouse.click_r_pos_y = self.__mouse.mouse_pointer_y
            dbg.LOG("RIGHT CLICK ONESHOT")
        self.__mouse.click_r = True

    def right_click_off(self):
        if self.__mouse.click_r:
            self.__mouse.click_r_pos_x = -1
            self.__mouse.click_r_pos_y = -1
        self.__mouse.click_r = False

    def is_right_click(self):
        return self.__mouse.click_r

    def right_click_move_mouse(self):
        return self.__mouse.get_click_r_pos()

    def left_click_on(self):
        if not self.__mouse.click_l:
            self.__mouse.click_l_pos_x = self.__mouse.mouse_pointer_x
            self.__mouse.click_l_pos_y = self.__mouse.mouse_pointer_y
            self.__mouse.click_l = True
            dbg.LOG("LEFT CLICK ONESHOT")

    def left_click_off(self):
        if self.__mouse.click_l:
            self.__mouse.click_l_pos_x = -1
            self.__mouse.click_l_pos_y = -1
            self.__mouse.click_l = False

    def is_left_click(self):
        return self.__mouse.click_l

    def left_click_move_mouse(self):
        return self.__mouse.get_click_l_pos()

    def reset_click(self):
        self.__mouse.reset()

    def set_mouse(self, x, y):
        self.__mouse.mouse_pointer_x = x
        self.__mouse.mouse_pointer_y = y

    def reset_mouse_click_r(self):
        self.__mouse.click_r_pos_x = -1
        self.__mouse.click_r_pos_y = -1

    def reset_mouse_click_l(self):
        self.__mouse.click_l_pos_x = -1
        self.__mouse.click_l_pos_y = -1

    def get_mouse(self):
        return self.__mouse.get_mouse_pointer()
