import dataclasses
import dungeon.form.position.form as pos_form
import dungeon.img as dungeon_img
# Form
import dungeon.form.map.form as map_form
import dungeon.form.button.form as button_form
import dungeon.form.action.form as action_form
import dungeon.form.abnormal.form as abnormal_form
import dungeon.form.log.form as log_form
import dungeon.form.box.form as box_form
# method
import pyd.createPass as cPass
import pyd.way as WAY
import dungeon.common as cmn_dungeon
import common.debug.debug as dbg
import common.common as cmn
import pygame
import math
import random


@dataclasses.dataclass
class Form:
    __map_form: map_form.Form
    __button_form: button_form.Form
    __action_form: action_form.Form
    __abnormal_form: abnormal_form.Form
    __log_form: log_form.Form
    __box_form: box_form.Form
    __img_list: list
    __end_flag: bool

    def __init__(self, floor: int):
        self.__map_form = map_form.Form(floor)
        self.__button_form = button_form.Form()
        self.__action_form = action_form.Form()
        self.__abnormal_form = abnormal_form.Form()
        self.__log_form = log_form.Form()
        self.__box_form = box_form.Form()
        self.__img_list = dungeon_img.Download.dungeonImag()
        self.__end_flag = False

    def reset(self, floor: int):
        if floor > len(map_form.dungeon):
            self.__action_form.total_count_up()
            self.__action_form.count_reset()
            self.__abnormal_form.recover()
            self.__log_form.reset()
            if self.__action_form.get_flag() is True:
                self.__action_form.flag_off()
            dbg.LOG("最上階へ到達しました")
            return True
        else:
            self.__map_form.reset(floor)
            self.__action_form.total_count_up()
            self.__action_form.count_reset()
            self.__abnormal_form.recover()
            self.__log_form.reset()
            if self.__action_form.get_flag() is True:
                self.__action_form.flag_off()
            return False

    def update_way(self, ope_form):
        now_way = self.__map_form.now_way
        next_way = now_way
        if now_way == WAY.UP():
            if ope_form.get_up():
                next_way = WAY.UP()
            elif ope_form.get_left():
                next_way = WAY.LEFT()
            elif ope_form.get_right():
                next_way = WAY.RIGHT()
            elif ope_form.get_down():
                next_way = WAY.DOWN()
        if now_way == WAY.RIGHT():
            if ope_form.get_up():
                next_way = WAY.RIGHT()
            elif ope_form.get_left():
                next_way = WAY.UP()
            elif ope_form.get_right():
                next_way = WAY.DOWN()
            elif ope_form.get_down():
                next_way = WAY.LEFT()
        if now_way == WAY.LEFT():
            if ope_form.get_up():
                next_way = WAY.LEFT()
            elif ope_form.get_left():
                next_way = WAY.DOWN()
            elif ope_form.get_right():
                next_way = WAY.UP()
            elif ope_form.get_down():
                next_way = WAY.RIGHT()
        if now_way == WAY.DOWN():
            if ope_form.get_up():
                next_way = WAY.DOWN()
            elif ope_form.get_left():
                next_way = WAY.RIGHT()
            elif ope_form.get_right():
                next_way = WAY.LEFT()
            elif ope_form.get_down():
                next_way = WAY.UP()
        self.__map_form.update_way(next_way)

    def update_pos(self, pos):
        self.__map_form.update_pos(pos)

    def update_view(self):
        self.__map_form.update_view()

    def update_situation(self):
        self.__map_form.update_situation()

    def enemy_move(self):
        if self.__action_form.get_flag():
            self.__map_form.enemy_move()

    def get_floor(self):
        return self.__map_form.floor

    def get_now_way(self):
        return self.__map_form.now_way

    def debug_now_way(self):
        return self.__map_form.now_way

    def get_now_pos(self):
        return [self.__map_form.now_pos.x, self.__map_form.now_pos.y]

    def debug_now_pos(self):
        return [self.__map_form.now_pos.x, self.__map_form.now_pos.y]

    def get_now_view(self):
        return self.__map_form.now_view

    def debug_now_view(self):
        return self.__map_form.now_view

    def debug_pre_way(self):
        return self.__map_form.pre_way

    def get_pre_pos(self):
        return [self.__map_form.pre_pos.x, self.__map_form.pre_pos.y]

    def debug_pre_pos(self):
        return [self.__map_form.pre_pos.x, self.__map_form.pre_pos.y]

    def debug_pre_view(self):
        return self.__map_form.pre_view

    def get_situation(self):
        return self.__map_form.situation

    def get_dungeon_map(self):
        return self.__map_form.map

    def get_width_max(self):
        return self.__map_form.max_width

    def get_depth_max(self):
        return self.__map_form.max_depth

    def get_start_pos(self):
        start_pos = self.__map_form.start_pos
        return [start_pos.x, start_pos.y]

    def create_angle(self):
        now_pos = self.__map_form.now_pos
        goal_pos = self.__map_form.goal_pos
        now_way = self.__map_form.now_way
        compass_angle = 0
        if now_pos.y == goal_pos.y:
            if now_pos.x < goal_pos.x:
                compass_angle = Form.__compass_way(180, now_way)
            elif now_pos.x > goal_pos.x:
                compass_angle = Form.__compass_way(0, now_way)
            else:
                compass_angle = Form.__compass_way(90, now_way)
        elif now_pos.y > goal_pos.y:
            if now_pos.x < goal_pos.x:
                angel = math.degrees(math.atan((goal_pos.y - now_pos.y)) / (goal_pos.x - now_pos.x))
                compass_angle = Form.__compass_way(angel + 180, now_way)
            elif now_pos.x > goal_pos.x:
                angel = math.degrees(math.atan((goal_pos.y - now_pos.y) / (goal_pos.x - now_pos.x)))
                compass_angle = Form.__compass_way(angel, now_way)
            else:
                compass_angle = Form.__compass_way(90, now_way)
        elif now_pos.y < goal_pos.y:
            if now_pos.x < goal_pos.x:
                angel = math.degrees(math.atan((goal_pos.y - now_pos.y) / (goal_pos.x - now_pos.x)))
                compass_angle = Form.__compass_way(angel + 180, now_way)
            elif now_pos.x > goal_pos.x:
                angel = math.degrees(math.atan((goal_pos.y - now_pos.y) / (now_pos.x - goal_pos.x)))
                compass_angle = Form.__compass_way(-angel, now_way)
            else:
                compass_angle = Form.__compass_way(270, now_way)
        return compass_angle

    @staticmethod
    def __compass_way(compass_way, now_way):
        if WAY.UP() == now_way:
            add_way = 0
        elif WAY.RIGHT() == now_way:
            add_way = 90
        elif WAY.LEFT() == now_way:
            add_way = 270
        else:
            add_way = 180
        return compass_way + add_way + random.randint(-2, 2)

    # [ENEMY] START
    def disappearance_enemy(self, index):
        return self.__map_form.disappearance_enemy(index)

    def ENEMY_COUNT(self):
        return self.__map_form.get_enemy_count()

    def APPEAR_FLAG(self, index):
        return self.__map_form.get_appear_flag(index)

    def get_enemy_type(self, index):
        return self.__map_form.get_enemy_type(index)

    def get_enemy_pos(self, index):
        return self.__map_form.get_enemy_pos(index)
    # [ENEMY] END

    def event_flag_off(self):
        self.__map_form.event_flag_off()

    # [ITEM] START
    def search_item(self):
        self.__map_form.get_item()

    def watch_box(self, num):
        return self.__box_form.watch(num)

    def item_set_box(self, item: int = -3, load_flag: bool = False):
        if load_flag:
            return self.__box_form.item_set(item)
        else:
            return self.__box_form.item_set(self.__map_form.get_item())

    def ITEM_GET_FLAG(self):
        return self.__map_form.get_item_flag()

    def item_flag_off(self):
        return self.__map_form.item_flag_off()

    def itemBoxPreUpdate(self):
        return self.__box_form.update_pre()

    def itemBoxClear(self):
        return self.__box_form.clear()

    def item_box_use(self, index):
        return self.__box_form.use_item(index)

    def set_box_button(self, index, x, y):
        return self.__button_form.set_box_button_pos(index, x, y)

    def get_box_button(self, index):
        return self.__button_form.get_box_button_pos(index) + self.__button_form.get_box_button_size(index)

    def itemBoxUseFlag(self, index):
        return self.__box_form.get_use_flag(index)

    def itemBoxFlagOn(self):
        self.__box_form.flag_on()

    def BOX_FLAG(self):
        self.__box_form.get_flag()
    # [ITEM] END

    @property
    def img_list(self):
        return self.__img_list

    # [ACTION FORM] START
    def action_flag_on(self):
        self.__action_form.flag_on()

    def action_flag_off(self):
        if self.__action_form.flag_off():
            self.__action_form.count_up()
            self.__box_form.use_turn_count_up()

    def get_action_flag(self):
        return self.__action_form.get_flag()

    def get_count(self):
        return self.__action_form.get_count()

    def set_total_count(self, count: int):
        return self.__action_form.count_to_total_count(count)

    def get_total_count(self):
        return self.__action_form.get_total_count()
    # [ACTION FORM] END

    def existDiffWay(self):
        return self.__map_form.is_diff_way()

    def existDiffPos(self):
        return self.__map_form.is_diff_pos()

    def existDiffView(self):
        return self.__map_form.is_diff_view()

    # [SYSTEM BUTTON] START
    def set_config_button(self, x, y):
        self.__button_form.set_config_button_pos(x, y)

    def get_config_button(self):
        return self.__button_form.get_config_button_pos() + self.__button_form.get_config_button_size()

    def set_save_button(self, x, y):
        self.__button_form.set_save_button_pos(x, y)

    def get_save_button(self):
        return self.__button_form.get_save_button_pos() + self.__button_form.get_save_button_size()
    # [SYSTEM BUTTON] END

    # [ACTION BUTTON] START
    def set_retry_button(self, x, y):
        self.__button_form.set_retry_button_pos(x, y)

    def get_retry_button(self):
        return self.__button_form.get_retry_button_pos() + self.__button_form.get_retry_button_size()

    def set_action_button(self, index, x, y):
        self.__button_form.set_action_button_pos(index, x, y)

    def get_action_button(self, index):
        return self.__button_form.get_action_button_pos(index) + self.__button_form.get_action_button_size(index)
    # [ACTION BUTTON] END

    # ゲーム終了 処理
    def death(self):
        return self.__abnormal_form.death()

    def is_death(self):
        return self.__abnormal_form.IS_DEATH()

    @property
    def end_flag(self):
        return self.__end_flag

    @end_flag.setter
    def end_flag(self, flag_: bool):
        if flag_:
            dbg.LOG("ゲーム クリア!")
        self.__end_flag = flag_

    # [LOG] START
    def log_reset(self):
        self.__log_form.reset()

    def log_update(self):
        (text, event_type) = self.__map_form.get_event_text()
        if "" != text:
            self.__log_form.add_log(event_type + text)

    def get_log(self):
        return self.__log_form.get_log()

    def log_flag_off(self):
        self.__log_form.flag_off()

    def log_flag_on(self):
        self.__log_form.flag_on()

    def get_log_flag(self):
        return self.__log_form.get_flag()

    def get_log_num(self):
        return self.__log_form.get_log_num()
    # [LOG] END

    # [FONT] START
    @staticmethod
    def font():
        return pygame.font.Font(str(cmn.resource_path(cPass.getFontPass("DotGothic16-Regular.ttf"))), 34)

    @staticmethod
    def event_font():
        return pygame.font.Font(str(cmn.resource_path(cPass.getFontPass("DotGothic16-Regular.ttf"))), 16)

    @staticmethod
    def item_font():
        return pygame.font.Font(str(cmn.resource_path(cPass.getFontPass("DotGothic16-Regular.ttf"))), 16)
    # [FONT] END

    # [SAVE/LOAD] START
    def create_input_data(self):
        data0 = str(self.__map_form.floor)
        data1 = str(self.__action_form.get_total_count())
        data2 = str(self.__box_form.get_pre_num())
        (item0, itemNum0) = self.__box_form.pre_watch(0)
        data3 = str(item0) + "," + str(itemNum0)
        (item1, itemNum1) = self.__box_form.pre_watch(1)
        data4 = str(item1) + "," + str(itemNum1)
        (item2, itemNum2) = self.__box_form.pre_watch(2)
        data5 = str(item2) + "," + str(itemNum2)
        return data0 + "," + data1 + "," + data2 + "," + data3 + "," + data4 + "," + data5
    # [SAVE/LOAD] END
