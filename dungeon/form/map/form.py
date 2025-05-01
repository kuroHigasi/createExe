import copy
import dataclasses

import dungeon.data.map.map as dungeon_map
import dungeon.form.map.enemies.form as enemies_form
import dungeon.form.map.events.form as events_form
import dungeon.form.map.items.form as items_form
import dungeon.form.position.form as pos_form
import common.debug.debug as dbg
import dungeon.img as dungeon_img
import pyd.way as WAY
import dungeon.common as cmn_dungeon


dungeon = [dungeon_map.FirstFloor, dungeon_map.SecondFloor, dungeon_map.ThirdFloor, dungeon_map.ForthFloor]


@dataclasses.dataclass
class Form:
    __floor: int
    __now_way: any
    __pre_way: any
    __now_pos: pos_form.Form
    __pre_pos: pos_form.Form
    __start_pos: pos_form.Form
    __goal_pos: pos_form.Form
    __max_width: int
    __max_depth: int
    __situation: list
    __now_view: int
    __pre_view: int
    __map: list
    __enemies_form: enemies_form.Form
    __events_form: events_form.Form
    __items_form: items_form.Form()

    def __init__(self, floor=1):
        if 0 < floor <= len(dungeon):
            init_map = dungeon[floor-1].map
            init_way = dungeon[floor-1].start_way
            init_pos = dungeon[floor-1].start_pos
            goal_pos = dungeon[floor-1].goal_pos
            max_width = dungeon[floor-1].maxWidth
            max_depth = dungeon[floor-1].maxDepth
            enemy_list = dungeon[floor-1].enemyList
            event_list = dungeon[floor-1].eventList
            item_list = dungeon[floor-1].itemList
        else:
            init_map = dungeon[0].map
            init_way = dungeon[0].start_way
            init_pos = dungeon[0].start_pos
            goal_pos = dungeon[0].goal_pos
            max_width = dungeon[0].maxWidth
            max_depth = dungeon[0].maxDepth
            enemy_list = dungeon[0].enemyList
            event_list = dungeon[0].eventList
            item_list = dungeon[0].itemList
            dbg.ERROR_LOG("[MapForm.__init__]存在しない階数を指定しています")
            dbg.ERROR_LOG("[MapForm.__init__]暫定的に1階で初期化します")
        self.__floor = floor
        self.__now_way = init_way
        self.__pre_way = init_way
        self.__now_pos = copy.deepcopy(init_pos)
        self.__pre_pos = copy.deepcopy(init_pos)
        self.__start_pos = copy.deepcopy(init_pos)
        self.__goal_pos = goal_pos
        self.__max_width = max_width
        self.__max_depth = max_depth
        self.__situation = Form.__get_situation(init_map, init_way, init_pos.x, init_pos.y, max_width, max_depth)
        self.__now_view = Form.__set_view(self.__situation)
        self.__pre_view = self.__now_view
        self.__map = init_map
        self.__enemies_form = enemies_form.Form()
        self.__enemies_form.registry(enemy_list)
        self.__events_form = events_form.Form()
        self.__events_form.registry(event_list)
        self.__items_form = items_form.Form()
        self.__items_form.register(item_list)

    def reset(self, floor=1):
        if 0 < floor <= len(dungeon):
            init_map = dungeon[floor-1].map
            init_way = dungeon[floor-1].start_way
            init_pos = dungeon[floor-1].start_pos
            goal_pos = dungeon[floor-1].goal_pos
            max_width = dungeon[floor-1].maxWidth
            max_depth = dungeon[floor-1].maxDepth
            enemy_list = dungeon[floor-1].enemyList
            event_list = dungeon[floor-1].eventList
            item_list = dungeon[floor-1].itemList
            self.__floor = floor
            self.__now_way = init_way
            self.__pre_way = init_way
            self.__now_pos = copy.deepcopy(init_pos)
            self.__pre_pos = copy.deepcopy(init_pos)
            self.__start_pos = copy.deepcopy(init_pos)
            self.__goal_pos = goal_pos
            self.__max_width = max_width
            self.__max_depth = max_depth
            self.__situation = Form.__get_situation(init_map, init_way, init_pos.x, init_pos.y, max_width, max_depth)
            self.__now_view = Form.__set_view(self.__situation)
            self.__pre_view = self.__now_view
            self.__map = init_map
            self.__enemies_form.registry(enemy_list)
            self.__events_form.registry(event_list)
            self.__items_form.register(item_list)
        else:
            dbg.ERROR_LOG("[MapForm.__set]存在しない階数を指定しています")

    def update_way(self, way: int):
        self.__pre_way = self.__now_way
        self.__now_way = way

    def update_pos(self, pos: list[int]):
        self.__pre_pos = copy.deepcopy(self.__now_pos)
        self.__now_pos.x = pos[0]
        self.__now_pos.y = pos[1]

    def update_view(self):
        self.__pre_view = self.__now_view
        self.__now_view = Form.__set_view(self.__situation)

    def update_situation(self):
        dungeon_map_ = self.__map
        way_ = self.__now_way
        pos_ = self.__now_pos
        width_ = self.__max_width
        depth_ = self.__max_depth
        self.__situation = Form.__get_situation(dungeon_map_, way_, pos_.x, pos_.y, width_, depth_)

    @property
    def floor(self):
        return self.__floor

    @property
    def now_way(self):
        return self.__now_way

    @property
    def now_pos(self):
        return self.__now_pos

    @property
    def now_view(self):
        return self.__now_view

    @property
    def pre_way(self):
        return self.__pre_way

    @property
    def pre_pos(self):
        return self.__pre_pos

    @property
    def pre_view(self):
        return self.__pre_view

    @property
    def situation(self):
        return self.__situation

    @property
    def map(self):
        return self.__map

    @property
    def max_width(self):
        return self.__max_width

    @property
    def max_depth(self):
        return self.__max_depth

    @property
    def start_pos(self):
        return self.__start_pos

    @property
    def goal_pos(self):
        return self.__goal_pos

    def is_diff_way(self):
        return self.__pre_way != self.__now_way

    def is_diff_pos(self):
        return self.__pre_pos != self.__now_pos

    def is_diff_view(self):
        return self.__pre_view != self.__now_view

    def get_enemy_count(self):
        return self.__enemies_form.enemy_count

    def disappearance_enemy(self, index):
        self.__enemies_form.disappearanceEnemy(index)

    def get_appear_flag(self, index):
        return self.__enemies_form.APPEAR_FLAG(index)

    def get_enemy_type(self, index):
        return self.__enemies_form.get_type(index)

    def get_enemy_pos(self, index):
        return self.__enemies_form.get_enemy_pos(index)

    def enemy_move(self):
        return self.__enemies_form.update_pos()

    def get_event_text(self):
        return self.__events_form.get_text([self.__now_pos.x, self.__now_pos.y], self.__now_way)

    def event_flag_off(self):
        self.__events_form.flag_off([self.__now_pos.x, self.__now_pos.y])

    def get_item(self):
        return self.__items_form.getItem([self.__now_pos.x, self.__now_pos.y])

    def item_flag_off(self):
        return self.__items_form.flagOff()

    def get_item_flag(self):
        return self.__items_form.ITEM_GET_FLAG()

    @staticmethod
    def __set_view(situation):
        status = 0x000
        # L pos set
        status = dungeon_img.pos.L(situation, status)
        # C pos set
        status = dungeon_img.pos.C(situation, status)
        # R pos set
        status = dungeon_img.pos.R(situation, status)
        return status

    @staticmethod
    def __get_situation(dungeon_map_, now_way, depth, width, max_width, max_depth):
        situation = []
        if now_way == WAY.UP():
            situation.insert(0, Form._create_situation(dungeon_map_, depth, width-1, max_width, max_depth))
            situation.insert(1, Form._create_situation(dungeon_map_, depth-1, width-1, max_width, max_depth))
            situation.insert(2, Form._create_situation(dungeon_map_, depth-1, width, max_width, max_depth))
            situation.insert(3, Form._create_situation(dungeon_map_, depth-1, width+1, max_width, max_depth))
            situation.insert(4, Form._create_situation(dungeon_map_, depth, width+1, max_width, max_depth))
            situation.insert(5, Form._create_situation(dungeon_map_, depth-2, width, max_width, max_depth))
            situation.insert(6, Form._create_situation(dungeon_map_, depth-2, width-1, max_width, max_depth))
            situation.insert(7, Form._create_situation(dungeon_map_, depth-2, width+1, max_width, max_depth))
            situation.insert(8, Form._create_situation(dungeon_map_, depth-3, width, max_width, max_depth))
            situation.insert(9, Form._create_situation(dungeon_map_, depth-3, width-1, max_width, max_depth))
            situation.insert(10, Form._create_situation(dungeon_map_, depth-3, width+1, max_width, max_depth))
            situation.insert(11, Form._create_situation(dungeon_map_, depth+1, width, max_width, max_depth))
            situation.insert(12, Form._create_situation(dungeon_map_, depth+1, width-1, max_width, max_depth))
            situation.insert(13, Form._create_situation(dungeon_map_, depth+1, width+1, max_width, max_depth))
            situation.insert(14, Form._create_situation(dungeon_map_, depth+2, width, max_width, max_depth))
            situation.insert(15, Form._create_situation(dungeon_map_, depth+2, width-1, max_width, max_depth))
            situation.insert(16, Form._create_situation(dungeon_map_, depth+2, width+1, max_width, max_depth))
            situation.insert(17, Form._create_situation(dungeon_map_, depth+3, width, max_width, max_depth))
            situation.insert(18, Form._create_situation(dungeon_map_, depth+3, width-1, max_width, max_depth))
            situation.insert(19, Form._create_situation(dungeon_map_, depth+3, width+1, max_width, max_depth))
            situation.insert(20, Form._create_situation(dungeon_map_, depth-3, width-2, max_width, max_depth))
            situation.insert(21, Form._create_situation(dungeon_map_, depth-2, width-2, max_width, max_depth))
            situation.insert(22, Form._create_situation(dungeon_map_, depth-1, width-2, max_width, max_depth))
            situation.insert(23, Form._create_situation(dungeon_map_, depth, width-2, max_width, max_depth))
            situation.insert(24, Form._create_situation(dungeon_map_, depth+1, width-2, max_width, max_depth))
            situation.insert(25, Form._create_situation(dungeon_map_, depth+2, width-2, max_width, max_depth))
            situation.insert(26, Form._create_situation(dungeon_map_, depth+3, width-2, max_width, max_depth))
            situation.insert(27, Form._create_situation(dungeon_map_, depth-3, width+2, max_width, max_depth))
            situation.insert(28, Form._create_situation(dungeon_map_, depth-2, width+2, max_width, max_depth))
            situation.insert(29, Form._create_situation(dungeon_map_, depth-1, width+2, max_width, max_depth))
            situation.insert(30, Form._create_situation(dungeon_map_, depth, width+2, max_width, max_depth))
            situation.insert(31, Form._create_situation(dungeon_map_, depth+1, width+2, max_width, max_depth))
            situation.insert(32, Form._create_situation(dungeon_map_, depth+2, width+2, max_width, max_depth))
            situation.insert(33, Form._create_situation(dungeon_map_, depth+3, width+2, max_width, max_depth))
            situation.insert(34, Form._create_situation(dungeon_map_, depth-3, width-3, max_width, max_depth))
            situation.insert(35, Form._create_situation(dungeon_map_, depth-2, width-3, max_width, max_depth))
            situation.insert(36, Form._create_situation(dungeon_map_, depth-1, width-3, max_width, max_depth))
            situation.insert(37, Form._create_situation(dungeon_map_, depth, width-3, max_width, max_depth))
            situation.insert(38, Form._create_situation(dungeon_map_, depth+1, width-3, max_width, max_depth))
            situation.insert(39, Form._create_situation(dungeon_map_, depth+2, width-3, max_width, max_depth))
            situation.insert(40, Form._create_situation(dungeon_map_, depth+3, width-3, max_width, max_depth))
            situation.insert(41, Form._create_situation(dungeon_map_, depth-3, width+3, max_width, max_depth))
            situation.insert(42, Form._create_situation(dungeon_map_, depth-2, width+3, max_width, max_depth))
            situation.insert(43, Form._create_situation(dungeon_map_, depth-1, width+3, max_width, max_depth))
            situation.insert(44, Form._create_situation(dungeon_map_, depth, width+3, max_width, max_depth))
            situation.insert(45, Form._create_situation(dungeon_map_, depth+1, width+3, max_width, max_depth))
            situation.insert(46, Form._create_situation(dungeon_map_, depth+2, width+3, max_width, max_depth))
            situation.insert(47, Form._create_situation(dungeon_map_, depth+3, width+3, max_width, max_depth))
        elif now_way == WAY.RIGHT():
            situation.insert(0, Form._create_situation(dungeon_map_, depth-1, width, max_width, max_depth))
            situation.insert(1, Form._create_situation(dungeon_map_, depth-1, width+1, max_width, max_depth))
            situation.insert(2, Form._create_situation(dungeon_map_, depth, width+1, max_width, max_depth))
            situation.insert(3, Form._create_situation(dungeon_map_, depth+1, width+1, max_width, max_depth))
            situation.insert(4, Form._create_situation(dungeon_map_, depth+1, width, max_width, max_depth))
            situation.insert(5, Form._create_situation(dungeon_map_, depth, width+2, max_width, max_depth))
            situation.insert(6, Form._create_situation(dungeon_map_, depth-1, width+2, max_width, max_depth))
            situation.insert(7, Form._create_situation(dungeon_map_, depth+1, width+2, max_width, max_depth))
            situation.insert(8, Form._create_situation(dungeon_map_, depth, width+3, max_width, max_depth))
            situation.insert(9, Form._create_situation(dungeon_map_, depth-1, width+3, max_width, max_depth))
            situation.insert(10, Form._create_situation(dungeon_map_, depth+1, width+3, max_width, max_depth))
            situation.insert(11, Form._create_situation(dungeon_map_, depth, width-1, max_width, max_depth))
            situation.insert(12, Form._create_situation(dungeon_map_, depth-1, width-1, max_width, max_depth))
            situation.insert(13, Form._create_situation(dungeon_map_, depth+1, width-1, max_width, max_depth))
            situation.insert(14, Form._create_situation(dungeon_map_, depth, width-2, max_width, max_depth))
            situation.insert(15, Form._create_situation(dungeon_map_, depth-1, width-2, max_width, max_depth))
            situation.insert(16, Form._create_situation(dungeon_map_, depth+1, width-2, max_width, max_depth))
            situation.insert(17, Form._create_situation(dungeon_map_, depth, width-3, max_width, max_depth))
            situation.insert(18, Form._create_situation(dungeon_map_, depth-1, width-3, max_width, max_depth))
            situation.insert(19, Form._create_situation(dungeon_map_, depth+1, width-3, max_width, max_depth))
            situation.insert(20, Form._create_situation(dungeon_map_, depth-2, width+3, max_width, max_depth))
            situation.insert(21, Form._create_situation(dungeon_map_, depth-2, width+2, max_width, max_depth))
            situation.insert(22, Form._create_situation(dungeon_map_, depth-2, width+1, max_width, max_depth))
            situation.insert(23, Form._create_situation(dungeon_map_, depth-2, width, max_width, max_depth))
            situation.insert(24, Form._create_situation(dungeon_map_, depth-2, width-1, max_width, max_depth))
            situation.insert(25, Form._create_situation(dungeon_map_, depth-2, width-2, max_width, max_depth))
            situation.insert(26, Form._create_situation(dungeon_map_, depth-2, width-3, max_width, max_depth))
            situation.insert(27, Form._create_situation(dungeon_map_, depth+2, width+3, max_width, max_depth))
            situation.insert(28, Form._create_situation(dungeon_map_, depth+2, width+2, max_width, max_depth))
            situation.insert(29, Form._create_situation(dungeon_map_, depth+2, width+1, max_width, max_depth))
            situation.insert(30, Form._create_situation(dungeon_map_, depth+2, width, max_width, max_depth))
            situation.insert(31, Form._create_situation(dungeon_map_, depth+2, width-1, max_width, max_depth))
            situation.insert(32, Form._create_situation(dungeon_map_, depth+2, width-2, max_width, max_depth))
            situation.insert(33, Form._create_situation(dungeon_map_, depth+2, width-3, max_width, max_depth))
            situation.insert(34, Form._create_situation(dungeon_map_, depth-3, width+3, max_width, max_depth))
            situation.insert(35, Form._create_situation(dungeon_map_, depth-3, width+2, max_width, max_depth))
            situation.insert(36, Form._create_situation(dungeon_map_, depth-3, width+1, max_width, max_depth))
            situation.insert(37, Form._create_situation(dungeon_map_, depth-3, width, max_width, max_depth))
            situation.insert(38, Form._create_situation(dungeon_map_, depth-3, width-1, max_width, max_depth))
            situation.insert(39, Form._create_situation(dungeon_map_, depth-3, width-2, max_width, max_depth))
            situation.insert(40, Form._create_situation(dungeon_map_, depth-3, width-3, max_width, max_depth))
            situation.insert(41, Form._create_situation(dungeon_map_, depth+3, width+3, max_width, max_depth))
            situation.insert(42, Form._create_situation(dungeon_map_, depth+3, width+2, max_width, max_depth))
            situation.insert(43, Form._create_situation(dungeon_map_, depth+3, width+1, max_width, max_depth))
            situation.insert(44, Form._create_situation(dungeon_map_, depth+3, width, max_width, max_depth))
            situation.insert(45, Form._create_situation(dungeon_map_, depth+3, width-1, max_width, max_depth))
            situation.insert(46, Form._create_situation(dungeon_map_, depth+3, width-2, max_width, max_depth))
            situation.insert(47, Form._create_situation(dungeon_map_, depth+3, width-3, max_width, max_depth))
        elif now_way == WAY.LEFT():
            situation.insert(0, Form._create_situation(dungeon_map_, depth+1, width, max_width, max_depth))
            situation.insert(1, Form._create_situation(dungeon_map_, depth+1, width-1, max_width, max_depth))
            situation.insert(2, Form._create_situation(dungeon_map_, depth, width-1, max_width, max_depth))
            situation.insert(3, Form._create_situation(dungeon_map_, depth-1, width-1, max_width, max_depth))
            situation.insert(4, Form._create_situation(dungeon_map_, depth-1, width, max_width, max_depth))
            situation.insert(5, Form._create_situation(dungeon_map_, depth, width-2, max_width, max_depth))
            situation.insert(6, Form._create_situation(dungeon_map_, depth+1, width-2, max_width, max_depth))
            situation.insert(7, Form._create_situation(dungeon_map_, depth-1, width-2, max_width, max_depth))
            situation.insert(8, Form._create_situation(dungeon_map_, depth, width-3, max_width, max_depth))
            situation.insert(9, Form._create_situation(dungeon_map_, depth+1, width-3, max_width, max_depth))
            situation.insert(10, Form._create_situation(dungeon_map_, depth-1, width-3, max_width, max_depth))
            situation.insert(11, Form._create_situation(dungeon_map_, depth, width+1, max_width, max_depth))
            situation.insert(12, Form._create_situation(dungeon_map_, depth+1, width+1, max_width, max_depth))
            situation.insert(13, Form._create_situation(dungeon_map_, depth-1, width+1, max_width, max_depth))
            situation.insert(14, Form._create_situation(dungeon_map_, depth, width+2, max_width, max_depth))
            situation.insert(15, Form._create_situation(dungeon_map_, depth+1, width+2, max_width, max_depth))
            situation.insert(16, Form._create_situation(dungeon_map_, depth-1, width+2, max_width, max_depth))
            situation.insert(17, Form._create_situation(dungeon_map_, depth, width+3, max_width, max_depth))
            situation.insert(18, Form._create_situation(dungeon_map_, depth+1, width+3, max_width, max_depth))
            situation.insert(19, Form._create_situation(dungeon_map_, depth-1, width+3, max_width, max_depth))
            situation.insert(20, Form._create_situation(dungeon_map_, depth+2, width-3, max_width, max_depth))
            situation.insert(21, Form._create_situation(dungeon_map_, depth+2, width-2, max_width, max_depth))
            situation.insert(22, Form._create_situation(dungeon_map_, depth+2, width-1, max_width, max_depth))
            situation.insert(23, Form._create_situation(dungeon_map_, depth+2, width, max_width, max_depth))
            situation.insert(24, Form._create_situation(dungeon_map_, depth+2, width+1, max_width, max_depth))
            situation.insert(25, Form._create_situation(dungeon_map_, depth+2, width+2, max_width, max_depth))
            situation.insert(26, Form._create_situation(dungeon_map_, depth+2, width+3, max_width, max_depth))
            situation.insert(27, Form._create_situation(dungeon_map_, depth-2, width-3, max_width, max_depth))
            situation.insert(28, Form._create_situation(dungeon_map_, depth-2, width-2, max_width, max_depth))
            situation.insert(29, Form._create_situation(dungeon_map_, depth-2, width-1, max_width, max_depth))
            situation.insert(30, Form._create_situation(dungeon_map_, depth-2, width, max_width, max_depth))
            situation.insert(31, Form._create_situation(dungeon_map_, depth-2, width+1, max_width, max_depth))
            situation.insert(32, Form._create_situation(dungeon_map_, depth-2, width+2, max_width, max_depth))
            situation.insert(33, Form._create_situation(dungeon_map_, depth-2, width+3, max_width, max_depth))
            situation.insert(34, Form._create_situation(dungeon_map_, depth+3, width-3, max_width, max_depth))
            situation.insert(35, Form._create_situation(dungeon_map_, depth+3, width-2, max_width, max_depth))
            situation.insert(36, Form._create_situation(dungeon_map_, depth+3, width-1, max_width, max_depth))
            situation.insert(37, Form._create_situation(dungeon_map_, depth+3, width, max_width, max_depth))
            situation.insert(38, Form._create_situation(dungeon_map_, depth+3, width+1, max_width, max_depth))
            situation.insert(39, Form._create_situation(dungeon_map_, depth+3, width+2, max_width, max_depth))
            situation.insert(40, Form._create_situation(dungeon_map_, depth+3, width+3, max_width, max_depth))
            situation.insert(41, Form._create_situation(dungeon_map_, depth-3, width-3, max_width, max_depth))
            situation.insert(42, Form._create_situation(dungeon_map_, depth-3, width-2, max_width, max_depth))
            situation.insert(43, Form._create_situation(dungeon_map_, depth-3, width-1, max_width, max_depth))
            situation.insert(44, Form._create_situation(dungeon_map_, depth-3, width, max_width, max_depth))
            situation.insert(45, Form._create_situation(dungeon_map_, depth-3, width+1, max_width, max_depth))
            situation.insert(46, Form._create_situation(dungeon_map_, depth-3, width+2, max_width, max_depth))
            situation.insert(47, Form._create_situation(dungeon_map_, depth-3, width+3, max_width, max_depth))
        elif now_way == WAY.DOWN():
            situation.insert(0, Form._create_situation(dungeon_map_, depth, width+1, max_width, max_depth))
            situation.insert(1, Form._create_situation(dungeon_map_, depth+1, width+1, max_width, max_depth))
            situation.insert(2, Form._create_situation(dungeon_map_, depth+1, width, max_width, max_depth))
            situation.insert(3, Form._create_situation(dungeon_map_, depth+1, width-1, max_width, max_depth))
            situation.insert(4, Form._create_situation(dungeon_map_, depth, width-1, max_width, max_depth))
            situation.insert(5, Form._create_situation(dungeon_map_, depth+2, width, max_width, max_depth))
            situation.insert(6, Form._create_situation(dungeon_map_, depth+2, width+1, max_width, max_depth))
            situation.insert(7, Form._create_situation(dungeon_map_, depth+2, width-1, max_width, max_depth))
            situation.insert(8, Form._create_situation(dungeon_map_, depth+3, width, max_width, max_depth))
            situation.insert(9, Form._create_situation(dungeon_map_, depth+3, width+1, max_width, max_depth))
            situation.insert(10, Form._create_situation(dungeon_map_, depth+3, width-1, max_width, max_depth))
            situation.insert(11, Form._create_situation(dungeon_map_, depth-1, width, max_width, max_depth))
            situation.insert(12, Form._create_situation(dungeon_map_, depth-1, width+1, max_width, max_depth))
            situation.insert(13, Form._create_situation(dungeon_map_, depth-1, width-1, max_width, max_depth))
            situation.insert(14, Form._create_situation(dungeon_map_, depth-2, width, max_width, max_depth))
            situation.insert(15, Form._create_situation(dungeon_map_, depth-2, width+1, max_width, max_depth))
            situation.insert(16, Form._create_situation(dungeon_map_, depth-2, width-1, max_width, max_depth))
            situation.insert(17, Form._create_situation(dungeon_map_, depth-3, width, max_width, max_depth))
            situation.insert(18, Form._create_situation(dungeon_map_, depth-3, width+1, max_width, max_depth))
            situation.insert(19, Form._create_situation(dungeon_map_, depth-3, width-1, max_width, max_depth))
            situation.insert(20, Form._create_situation(dungeon_map_, depth+3, width+2, max_width, max_depth))
            situation.insert(21, Form._create_situation(dungeon_map_, depth+2, width+2, max_width, max_depth))
            situation.insert(22, Form._create_situation(dungeon_map_, depth+1, width+2, max_width, max_depth))
            situation.insert(23, Form._create_situation(dungeon_map_, depth, width+2, max_width, max_depth))
            situation.insert(24, Form._create_situation(dungeon_map_, depth-1, width+2, max_width, max_depth))
            situation.insert(25, Form._create_situation(dungeon_map_, depth-2, width+2, max_width, max_depth))
            situation.insert(26, Form._create_situation(dungeon_map_, depth-3, width+2, max_width, max_depth))
            situation.insert(27, Form._create_situation(dungeon_map_, depth+3, width-2, max_width, max_depth))
            situation.insert(28, Form._create_situation(dungeon_map_, depth+2, width-2, max_width, max_depth))
            situation.insert(29, Form._create_situation(dungeon_map_, depth+1, width-2, max_width, max_depth))
            situation.insert(30, Form._create_situation(dungeon_map_, depth, width-2, max_width, max_depth))
            situation.insert(31, Form._create_situation(dungeon_map_, depth-1, width-2, max_width, max_depth))
            situation.insert(32, Form._create_situation(dungeon_map_, depth-2, width-2, max_width, max_depth))
            situation.insert(33, Form._create_situation(dungeon_map_, depth-3, width-2, max_width, max_depth))
            situation.insert(34, Form._create_situation(dungeon_map_, depth+3, width+3, max_width, max_depth))
            situation.insert(35, Form._create_situation(dungeon_map_, depth+2, width+3, max_width, max_depth))
            situation.insert(36, Form._create_situation(dungeon_map_, depth+1, width+3, max_width, max_depth))
            situation.insert(37, Form._create_situation(dungeon_map_, depth, width+3, max_width, max_depth))
            situation.insert(38, Form._create_situation(dungeon_map_, depth-1, width+3, max_width, max_depth))
            situation.insert(39, Form._create_situation(dungeon_map_, depth-2, width+3, max_width, max_depth))
            situation.insert(40, Form._create_situation(dungeon_map_, depth-3, width+3, max_width, max_depth))
            situation.insert(41, Form._create_situation(dungeon_map_, depth+3, width-3, max_width, max_depth))
            situation.insert(42, Form._create_situation(dungeon_map_, depth+2, width-3, max_width, max_depth))
            situation.insert(43, Form._create_situation(dungeon_map_, depth+1, width-3, max_width, max_depth))
            situation.insert(44, Form._create_situation(dungeon_map_, depth, width-3, max_width, max_depth))
            situation.insert(45, Form._create_situation(dungeon_map_, depth-1, width-3, max_width, max_depth))
            situation.insert(46, Form._create_situation(dungeon_map_, depth-2, width-3, max_width, max_depth))
            situation.insert(47, Form._create_situation(dungeon_map_, depth-3, width-3, max_width, max_depth))
        return situation

    @staticmethod
    def _create_situation(dungeon_map_, depth, width, max_width, max_depth):
        return [cmn_dungeon.Common.isPosPath(dungeon_map_, depth, width, max_width, max_depth), depth, width]
