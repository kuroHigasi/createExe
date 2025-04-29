import dungeon.img as DungeonImg
# Form
import dungeon.form.map.form as MapForm
import dungeon.form.button.form as ButtonForm
import dungeon.form.action.form as ActionForm
import dungeon.form.abnormal.form as AbnormalForm
import dungeon.form.log.form as LogForm
import dungeon.form.box.form as BoxForm
# method
import pyd.createPass as cPass
import pyd.way as WAY
import dungeon.common as cmnDungeon
import common.debug.debug as dbg
import common.common as cmn
import pygame
import math
import random


class Form:
    def __init__(self, floor: int):
        self.__map_form = MapForm.Form(floor)
        self.__button_form = ButtonForm.Form()
        self.__action_form = ActionForm.Form()
        self.__abnormal_form = AbnormalForm.Form()
        self.__log_form = LogForm.Form()
        self.__box_form = BoxForm.Form()
        self.__img_list = DungeonImg.Download.dungeonImag()
        self.__end_flag = False

    def reset(self, floor: int):
        if floor > len(MapForm.dungeon):
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
        now_way = self.__map_form.get_now_way()
        next_way = now_way
        if now_way == WAY.UP:
            if ope_form.get_up():
                next_way = WAY.UP
            elif ope_form.get_left():
                next_way = WAY.LEFT
            elif ope_form.get_right():
                next_way = WAY.RIGHT
            elif ope_form.get_down():
                next_way = WAY.DOWN
        if now_way == WAY.RIGHT:
            if ope_form.get_up():
                next_way = WAY.RIGHT
            elif ope_form.get_left():
                next_way = WAY.UP
            elif ope_form.get_right():
                next_way = WAY.DOWN
            elif ope_form.get_down():
                next_way = WAY.LEFT
        if now_way == WAY.LEFT:
            if ope_form.get_up():
                next_way = WAY.LEFT
            elif ope_form.get_left():
                next_way = WAY.DOWN
            elif ope_form.get_right():
                next_way = WAY.UP
            elif ope_form.get_down():
                next_way = WAY.RIGHT
        if now_way == WAY.DOWN:
            if ope_form.get_up():
                next_way = WAY.DOWN
            elif ope_form.get_left():
                next_way = WAY.RIGHT
            elif ope_form.get_right():
                next_way = WAY.LEFT
            elif ope_form.get_down():
                next_way = WAY.UP
        self.__map_form.set_pre_way()
        self.__map_form.set_now_way(next_way)

    def player_move(self):
        judDepth = self.__map_form.get_now_pos()[0]
        judWidth = self.__map_form.get_now_pos()[1]
        nowWay = self.__map_form.get_now_way()
        map = self.__map_form.get_map()
        maxWidth = self.__map_form.get_max_width()
        maxDepth = self.__map_form.get_max_depth()
        nextPos = []
        if nowWay == WAY.UP:
            if cmnDungeon.Common.isPosPath(map, judDepth-1, judWidth, maxWidth, maxDepth):
                nextPos.insert(0, judDepth-1)
                nextPos.insert(1, judWidth)
            else:
                nextPos.insert(0, judDepth)
                nextPos.insert(1, judWidth)
        elif nowWay == WAY.RIGHT:
            if cmnDungeon.Common.isPosPath(map, judDepth, judWidth+1, maxWidth, maxDepth):
                nextPos.insert(0, judDepth)
                nextPos.insert(1, judWidth+1)
            else:
                nextPos.insert(0, judDepth)
                nextPos.insert(1, judWidth)
        elif nowWay == WAY.LEFT:
            if cmnDungeon.Common.isPosPath(map, judDepth, judWidth-1, maxWidth, maxDepth):
                nextPos.insert(0, judDepth)
                nextPos.insert(1, judWidth-1)
            else:
                nextPos.insert(0, judDepth)
                nextPos.insert(1, judWidth)
        elif nowWay == WAY.DOWN:
            if cmnDungeon.Common.isPosPath(map, judDepth+1, judWidth, maxWidth, maxDepth):
                nextPos.insert(0, judDepth+1)
                nextPos.insert(1, judWidth)
            else:
                nextPos.insert(0, judDepth)
                nextPos.insert(1, judWidth)
        else:
            dbg.ERROR_LOG("[action.go]存在しないWAY")
        self.__map_form.set_pos(nextPos)

    def update_view(self):
        self.__map_form.set_pre_view()
        self.__map_form.set_now_view()

    def update_situation(self):
        self.__map_form.set_situation()

    def enemy_move(self):
        if self.__action_form.get_flag():
            self.__map_form.enemy_move()

    def get_floor(self):
        return self.__map_form.get_now_floor()

    def NOW_WAY(self):
        return self.__map_form.get_now_way()

    def NOW_POS(self):
        return self.__map_form.get_now_pos()

    def NOW_VIEW(self):
        return self.__map_form.get_now_view()

    def PRE_WAY(self):
        return self.__map_form.get_pre_way()

    def PRE_POS(self):
        return self.__map_form.get_pre_pos()

    def PRE_VIEW(self):
        return self.__map_form.get_pre_view()

    def SITUATION(self):
        return self.__map_form.get_situation()

    def get_dungeon_map(self):
        return self.__map_form.get_map()

    def get_start_pos(self):
        return self.__map_form.get_start_pos()

    def create_angle(self):
        now_pos = self.__map_form.get_now_pos()
        goal_pos = self.__map_form.get_goal_pos()
        now_way = self.__map_form.get_now_way()
        compass_angle = 0
        if now_pos[1] == goal_pos[1]:
            if now_pos[0] < goal_pos[0]:
                compass_angle = Form.__compass_way(180, now_way)
            elif now_pos[0] > goal_pos[0]:
                compass_angle = Form.__compass_way(0, now_way)
            else:
                compass_angle = Form.__compass_way(90, now_way)
        elif now_pos[1] > goal_pos[1]:
            if now_pos[0] < goal_pos[0]:
                angel = math.degrees(math.atan((goal_pos[1] - now_pos[1])) / (goal_pos[0] - now_pos[0]))
                compass_angle = Form.__compass_way(angel + 180, now_way)
            elif now_pos[0] > goal_pos[0]:
                angel = math.degrees(math.atan((goal_pos[1] - now_pos[1]) / (goal_pos[0] - now_pos[0])))
                compass_angle = Form.__compass_way(angel, now_way)
            else:
                compass_angle = Form.__compass_way(90, now_way)
        elif now_pos[1] < goal_pos[1]:
            if now_pos[0] < goal_pos[0]:
                angel = math.degrees(math.atan((goal_pos[1] - now_pos[1]) / (goal_pos[0] - now_pos[0])))
                compass_angle = Form.__compass_way(angel + 180, now_way)
            elif now_pos[0] > goal_pos[0]:
                angel = math.degrees(math.atan((goal_pos[1] - now_pos[1]) / (now_pos[0] - goal_pos[0])))
                compass_angle = Form.__compass_way(-angel, now_way)
            else:
                compass_angle = Form.__compass_way(270, now_way)
        return compass_angle

    @staticmethod
    def __compass_way(compass_way, now_way):
        if WAY.UP == now_way:
            add_way = 0
        elif WAY.RIGHT == now_way:
            add_way = 90
        elif WAY.LEFT == now_way:
            add_way = 270
        else:
            add_way = 180
        return compass_way + add_way + random.randint(-2, 2)

    # [ENEMY] START
    def disappearanceEnemy(self, index):
        return self.__map_form.disappearance_enemy(index)

    def ENEMY_COUNT(self):
        return self.__map_form.get_enemy_count()

    def APPEAR_FLAG(self, index):
        return self.__map_form.get_appear_flag(index)

    def ENEMIS_TYPE(self, index):
        return self.__map_form.get_enemy_type(index)

    def ENEMIS_POS(self, index):
        return self.__map_form.get_enemy_pos(index)
    # [ENEMY] END

    def eventFlagOff(self):
        self.__map_form.event_flag_off()

    def getEventText(self):
        return self.__map_form.get_event_text()

    # [ITEM] START
    def searchItem(self):
        self.__map_form.get_item()

    def watchBox(self, num):
        return self.__box_form.watch(num)

    def itemIntoBox(self):
        return self.__box_form.item_set(self.__map_form.get_item())

    def ITEM_GET_FLAG(self):
        return self.__map_form.get_item_flag()

    def itemFlagOff(self):
        return self.__map_form.item_flag_off()

    def itemBoxPreUpdate(self):
        return self.__box_form.update_pre()

    def itemBoxReset(self):
        return self.__box_form.reset()

    def itemBoxClear(self):
        return self.__box_form.clear()

    def itemBoxUse(self, index):
        return self.__box_form.use_item(index)

    def itemBoxButtonUpdate(self, index, x, y):
        return self.__box_form.set_box_button_pos(index, x, y)

    def BOX_BUTTON(self, index):
        return self.__box_form.get_box_button_pos(index) + self.__box_form.get_box_button_size(index)

    def itemBoxUseFlag(self, index):
        return self.__box_form.get_use_flag(index)

    def itemBoxDispIndex(self, index):
        if self.__box_form.get_use_flag(index):
            return 1
        return 0

    def itemBoxPickUp(self, index):
        return self.__box_form.pickup(index)

    def itemBoxUseTurnCount(self):
        return self.__box_form.use_turn_count_up()

    def itemBoxFlagOn(self):
        self.__box_form.flag_on()

    def BOX_FLAG(self):
        self.__box_form.get_flag()
    # [ITEM] END

    def IMG_LIST(self):
        return self.__img_list

    # [ACTION FORM] START
    def actionFlagOn(self):
        self.__action_form.flag_on()

    def actionFlagOff(self):
        if self.__action_form.flag_off():
            self.__action_form.count_up()

    def ACTION_FLAG(self):
        return self.__action_form.get_flag()

    def COUNT(self):
        return self.__action_form.get_count()

    def updateTotalCount(self, count: int):
        return self.__action_form.count_to_total_count(count)

    def TOTAL_COUNT(self):
        return self.__action_form.get_total_count()
    # [ACTION FORM] END

    def existDiffWay(self):
        return self.__map_form.is_diff_way()

    def existDiffPos(self):
        return self.__map_form.is_diff_pos()

    def existDiffView(self):
        return self.__map_form.is_diff_view()

    # [SYSTEM BUTTON] START
    def updateConfigButton(self, x, y):
        self.__button_form.set_config_button_pos(x, y)

    def get_config_button(self):
        return self.__button_form.get_config_button_pos() + self.__button_form.get_config_button_size()

    def set_home_button(self, x, y):
        self.__button_form.set_home_button_pos(x, y)

    def get_home_button(self):
        return self.__button_form.get_home_button_pos() + self.__button_form.get_home_button_size()

    def updateExitButton(self, x, y):
        self.__button_form.set_exit_button_pos(x, y)

    def EXIT_BUTTON(self):
        return self.__button_form.get_exit_button_pos() + self.__button_form.get_exit_button_size()
    # [SYSTEM BUTTON] END

    # [ACTION BUTTON] START
    def updateRetryButton(self, x, y):
        self.__button_form.set_retry_button_pos(x, y)

    def RETRY_BUTTON(self):
        return self.__button_form.get_retry_button_pos() + self.__button_form.get_retry_button_size()

    def updateSaveButton(self, x, y):
        self.__button_form.set_save_button_pos(x, y)

    def SAVE_BUTTON(self):
        return self.__button_form.get_save_button_pos() + self.__button_form.get_save_button_size()

    def updateActionButton(self, index, x, y):
        self.__button_form.set_action_button_pos(index, x, y)

    def resetActionButton(self, index):
        self.__button_form.set_action_button_pos(index, -1, -1)

    def ACTION_BUTTON(self, index):
        return self.__button_form.get_action_button_pos(index) + self.__button_form.get_action_button_size(index)
    # [ACTION BUTTON] END

    # ゲーム終了 処理
    def death(self):
        return self.__abnormal_form.death()

    def is_death(self):
        return self.__abnormal_form.IS_DEATH()

    def end_flag_off(self):
        self.__end_flag = False

    def end_flag_on(self):
        dbg.LOG("ゲーム クリア!")
        self.__end_flag = True

    def get_dnd_flag(self):
        return self.__end_flag

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
        data0 = str(self.__map_form.get_now_floor())
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
