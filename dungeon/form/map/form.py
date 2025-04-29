import dungeon.data.map.map as dungeonMap
import dungeon.form.enemies.form as EnemiesForm
import dungeon.form.events.form as EventsForm
import dungeon.form.items.form as ItemsForm
import common.debug.debug as dbg
import dungeon.img as dungeonImg
import pyd.way as WAY
import dungeon.common as cmnDungeon


dungeon = [dungeonMap.FirstFloor, dungeonMap.SecondFloor, dungeonMap.ThirdFloor, dungeonMap.ForthFloor]


class Form:
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
        self.__now_pos = [init_pos.x, init_pos.y]
        self.__pre_pos = [init_pos.x, init_pos.y]
        self.__start_pos = [init_pos.x, init_pos.y]
        self.__goal_pos = [goal_pos.x, goal_pos.y]
        self.__max_width = max_width
        self.__max_depth = max_depth
        self.__situation = Form.__get_situation(init_map, init_way, init_pos.x, init_pos.y, max_width, max_depth)
        self.__now_view = Form.__set_view(self.__situation)
        self.__pre_view = self.__now_view
        self.__map = init_map
        self.__enemies_form = EnemiesForm.Form()
        self.__enemies_form.regist(enemy_list)
        self.__events_form = EventsForm.Form()
        self.__events_form.regist(event_list)
        self.__items_form = ItemsForm.Form()
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
            self.__now_pos = [init_pos.x, init_pos.y]
            self.__pre_pos = [init_pos.x, init_pos.y]
            self.__start_pos = [init_pos.x, init_pos.y]
            self.__goal_pos = [goal_pos.x, goal_pos.y]
            self.__max_width = max_width
            self.__max_depth = max_depth
            self.__situation = Form.__get_situation(init_map, init_way, init_pos.x, init_pos.y, max_width, max_depth)
            self.__now_view = Form.__set_view(self.__situation)
            self.__pre_view = self.__now_view
            self.__map = init_map
            self.__enemies_form.regist(enemy_list)
            self.__events_form.regist(event_list)
            self.__items_form.register(item_list)
        else:
            dbg.ERROR_LOG("[MapForm.__set]存在しない階数を指定しています")

    def set_pre_way(self):
        self.__pre_way = self.__now_way

    def set_now_way(self, way: int):
        self.__now_way = way

    def set_pos(self, pos: list[int]):
        self.__pre_pos = self.__now_pos
        self.__now_pos = pos

    def set_pre_view(self):
        self.__pre_view = self.__now_view

    def set_now_view(self):
        self.__now_view = Form.__set_view(self.__situation)

    def set_situation(self):
        dungeon_map = self.__map
        way = self.__now_way
        pos = self.__now_pos
        width = self.__max_width
        depth = self.__max_depth
        self.__situation = Form.__get_situation(dungeon_map, way, pos[0], pos[1], width, depth)

    def get_now_floor(self):
        return self.__floor

    def get_now_way(self):
        return self.__now_way

    def get_now_pos(self):
        return self.__now_pos

    def get_now_view(self):
        return self.__now_view

    def get_pre_way(self):
        return self.__pre_way

    def get_pre_pos(self):
        return self.__pre_pos

    def get_pre_view(self):
        return self.__pre_view

    def get_situation(self):
        return self.__situation

    def get_map(self):
        return self.__map

    def get_max_width(self):
        return self.__max_width

    def get_max_depth(self):
        return self.__max_depth

    def is_diff_way(self):
        return self.__pre_way != self.__now_way

    def is_diff_pos(self):
        return self.__pre_pos[0] == self.__now_pos[0] and self.__pre_pos[1] == self.__now_pos[1]

    def is_diff_view(self):
        return self.__pre_view != self.__now_view

    def get_enemy_count(self):
        return self.__enemies_form.ENEMY_COUNT()

    def disappearance_enemy(self, index):
        self.__enemies_form.disappearanceEnemy(index)

    def get_appear_flag(self, index):
        return self.__enemies_form.APPEAR_FLAG(index)

    def get_enemy_type(self, index):
        return self.__enemies_form.ENEMY_TYPE(index)

    def get_enemy_pos(self, index):
        return self.__enemies_form.ENEMY_POS(index)

    def enemy_move(self):
        return self.__enemies_form.enemyMove()

    def get_event_text(self):
        return self.__events_form.getEventText(self.__now_pos, self.__now_way)

    def event_flag_off(self):
        self.__events_form.eventFlagOff(self.__now_pos)

    def get_item(self):
        return self.__items_form.getItem(self.__now_pos)

    def item_flag_off(self):
        return self.__items_form.flagOff()

    def get_item_flag(self):
        return self.__items_form.ITEM_GET_FLAG()

    def get_start_pos(self):
        return self.__start_pos

    def get_goal_pos(self):
        return self.__goal_pos

    @staticmethod
    def __set_view(situation):
        status = 0x000
        # L pos set
        status = dungeonImg.pos.L(situation, status)
        # C pos set
        status = dungeonImg.pos.C(situation, status)
        # R pos set
        status = dungeonImg.pos.R(situation, status)
        return status

    @staticmethod
    def __get_situation(dungeon_map, now_way, depth, width, max_width, max_depth):
        situation = []
        if now_way == WAY.UP:
            situation.insert(0, Form._create_situation(dungeon_map, depth, width-1, max_width, max_depth))
            situation.insert(1, Form._create_situation(dungeon_map, depth-1, width-1, max_width, max_depth))
            situation.insert(2, Form._create_situation(dungeon_map, depth-1, width, max_width, max_depth))
            situation.insert(3, Form._create_situation(dungeon_map, depth-1, width+1, max_width, max_depth))
            situation.insert(4, Form._create_situation(dungeon_map, depth, width+1, max_width, max_depth))
            situation.insert(5, Form._create_situation(dungeon_map, depth-2, width, max_width, max_depth))
            situation.insert(6, Form._create_situation(dungeon_map, depth-2, width-1, max_width, max_depth))
            situation.insert(7, Form._create_situation(dungeon_map, depth-2, width+1, max_width, max_depth))
            situation.insert(8, Form._create_situation(dungeon_map, depth-3, width, max_width, max_depth))
            situation.insert(9, Form._create_situation(dungeon_map, depth-3, width-1, max_width, max_depth))
            situation.insert(10, Form._create_situation(dungeon_map, depth-3, width+1, max_width, max_depth))
            situation.insert(11, Form._create_situation(dungeon_map, depth+1, width, max_width, max_depth))
            situation.insert(12, Form._create_situation(dungeon_map, depth+1, width-1, max_width, max_depth))
            situation.insert(13, Form._create_situation(dungeon_map, depth+1, width+1, max_width, max_depth))
            situation.insert(14, Form._create_situation(dungeon_map, depth+2, width, max_width, max_depth))
            situation.insert(15, Form._create_situation(dungeon_map, depth+2, width-1, max_width, max_depth))
            situation.insert(16, Form._create_situation(dungeon_map, depth+2, width+1, max_width, max_depth))
            situation.insert(17, Form._create_situation(dungeon_map, depth+3, width, max_width, max_depth))
            situation.insert(18, Form._create_situation(dungeon_map, depth+3, width-1, max_width, max_depth))
            situation.insert(19, Form._create_situation(dungeon_map, depth+3, width+1, max_width, max_depth))
            situation.insert(20, Form._create_situation(dungeon_map, depth-3, width-2, max_width, max_depth))
            situation.insert(21, Form._create_situation(dungeon_map, depth-2, width-2, max_width, max_depth))
            situation.insert(22, Form._create_situation(dungeon_map, depth-1, width-2, max_width, max_depth))
            situation.insert(23, Form._create_situation(dungeon_map, depth, width-2, max_width, max_depth))
            situation.insert(24, Form._create_situation(dungeon_map, depth+1, width-2, max_width, max_depth))
            situation.insert(25, Form._create_situation(dungeon_map, depth+2, width-2, max_width, max_depth))
            situation.insert(26, Form._create_situation(dungeon_map, depth+3, width-2, max_width, max_depth))
            situation.insert(27, Form._create_situation(dungeon_map, depth-3, width+2, max_width, max_depth))
            situation.insert(28, Form._create_situation(dungeon_map, depth-2, width+2, max_width, max_depth))
            situation.insert(29, Form._create_situation(dungeon_map, depth-1, width+2, max_width, max_depth))
            situation.insert(30, Form._create_situation(dungeon_map, depth, width+2, max_width, max_depth))
            situation.insert(31, Form._create_situation(dungeon_map, depth+1, width+2, max_width, max_depth))
            situation.insert(32, Form._create_situation(dungeon_map, depth+2, width+2, max_width, max_depth))
            situation.insert(33, Form._create_situation(dungeon_map, depth+3, width+2, max_width, max_depth))
            situation.insert(34, Form._create_situation(dungeon_map, depth-3, width-3, max_width, max_depth))
            situation.insert(35, Form._create_situation(dungeon_map, depth-2, width-3, max_width, max_depth))
            situation.insert(36, Form._create_situation(dungeon_map, depth-1, width-3, max_width, max_depth))
            situation.insert(37, Form._create_situation(dungeon_map, depth, width-3, max_width, max_depth))
            situation.insert(38, Form._create_situation(dungeon_map, depth+1, width-3, max_width, max_depth))
            situation.insert(39, Form._create_situation(dungeon_map, depth+2, width-3, max_width, max_depth))
            situation.insert(40, Form._create_situation(dungeon_map, depth+3, width-3, max_width, max_depth))
            situation.insert(41, Form._create_situation(dungeon_map, depth-3, width+3, max_width, max_depth))
            situation.insert(42, Form._create_situation(dungeon_map, depth-2, width+3, max_width, max_depth))
            situation.insert(43, Form._create_situation(dungeon_map, depth-1, width+3, max_width, max_depth))
            situation.insert(44, Form._create_situation(dungeon_map, depth, width+3, max_width, max_depth))
            situation.insert(45, Form._create_situation(dungeon_map, depth+1, width+3, max_width, max_depth))
            situation.insert(46, Form._create_situation(dungeon_map, depth+2, width+3, max_width, max_depth))
            situation.insert(47, Form._create_situation(dungeon_map, depth+3, width+3, max_width, max_depth))
        elif now_way == WAY.RIGHT:
            situation.insert(0, Form._create_situation(dungeon_map, depth-1, width, max_width, max_depth))
            situation.insert(1, Form._create_situation(dungeon_map, depth-1, width+1, max_width, max_depth))
            situation.insert(2, Form._create_situation(dungeon_map, depth, width+1, max_width, max_depth))
            situation.insert(3, Form._create_situation(dungeon_map, depth+1, width+1, max_width, max_depth))
            situation.insert(4, Form._create_situation(dungeon_map, depth+1, width, max_width, max_depth))
            situation.insert(5, Form._create_situation(dungeon_map, depth, width+2, max_width, max_depth))
            situation.insert(6, Form._create_situation(dungeon_map, depth-1, width+2, max_width, max_depth))
            situation.insert(7, Form._create_situation(dungeon_map, depth+1, width+2, max_width, max_depth))
            situation.insert(8, Form._create_situation(dungeon_map, depth, width+3, max_width, max_depth))
            situation.insert(9, Form._create_situation(dungeon_map, depth-1, width+3, max_width, max_depth))
            situation.insert(10, Form._create_situation(dungeon_map, depth+1, width+3, max_width, max_depth))
            situation.insert(11, Form._create_situation(dungeon_map, depth, width-1, max_width, max_depth))
            situation.insert(12, Form._create_situation(dungeon_map, depth-1, width-1, max_width, max_depth))
            situation.insert(13, Form._create_situation(dungeon_map, depth+1, width-1, max_width, max_depth))
            situation.insert(14, Form._create_situation(dungeon_map, depth, width-2, max_width, max_depth))
            situation.insert(15, Form._create_situation(dungeon_map, depth-1, width-2, max_width, max_depth))
            situation.insert(16, Form._create_situation(dungeon_map, depth+1, width-2, max_width, max_depth))
            situation.insert(17, Form._create_situation(dungeon_map, depth, width-3, max_width, max_depth))
            situation.insert(18, Form._create_situation(dungeon_map, depth-1, width-3, max_width, max_depth))
            situation.insert(19, Form._create_situation(dungeon_map, depth+1, width-3, max_width, max_depth))
            situation.insert(20, Form._create_situation(dungeon_map, depth-2, width+3, max_width, max_depth))
            situation.insert(21, Form._create_situation(dungeon_map, depth-2, width+2, max_width, max_depth))
            situation.insert(22, Form._create_situation(dungeon_map, depth-2, width+1, max_width, max_depth))
            situation.insert(23, Form._create_situation(dungeon_map, depth-2, width, max_width, max_depth))
            situation.insert(24, Form._create_situation(dungeon_map, depth-2, width-1, max_width, max_depth))
            situation.insert(25, Form._create_situation(dungeon_map, depth-2, width-2, max_width, max_depth))
            situation.insert(26, Form._create_situation(dungeon_map, depth-2, width-3, max_width, max_depth))
            situation.insert(27, Form._create_situation(dungeon_map, depth+2, width+3, max_width, max_depth))
            situation.insert(28, Form._create_situation(dungeon_map, depth+2, width+2, max_width, max_depth))
            situation.insert(29, Form._create_situation(dungeon_map, depth+2, width+1, max_width, max_depth))
            situation.insert(30, Form._create_situation(dungeon_map, depth+2, width, max_width, max_depth))
            situation.insert(31, Form._create_situation(dungeon_map, depth+2, width-1, max_width, max_depth))
            situation.insert(32, Form._create_situation(dungeon_map, depth+2, width-2, max_width, max_depth))
            situation.insert(33, Form._create_situation(dungeon_map, depth+2, width-3, max_width, max_depth))
            situation.insert(34, Form._create_situation(dungeon_map, depth-3, width+3, max_width, max_depth))
            situation.insert(35, Form._create_situation(dungeon_map, depth-3, width+2, max_width, max_depth))
            situation.insert(36, Form._create_situation(dungeon_map, depth-3, width+1, max_width, max_depth))
            situation.insert(37, Form._create_situation(dungeon_map, depth-3, width, max_width, max_depth))
            situation.insert(38, Form._create_situation(dungeon_map, depth-3, width-1, max_width, max_depth))
            situation.insert(39, Form._create_situation(dungeon_map, depth-3, width-2, max_width, max_depth))
            situation.insert(40, Form._create_situation(dungeon_map, depth-3, width-3, max_width, max_depth))
            situation.insert(41, Form._create_situation(dungeon_map, depth+3, width+3, max_width, max_depth))
            situation.insert(42, Form._create_situation(dungeon_map, depth+3, width+2, max_width, max_depth))
            situation.insert(43, Form._create_situation(dungeon_map, depth+3, width+1, max_width, max_depth))
            situation.insert(44, Form._create_situation(dungeon_map, depth+3, width, max_width, max_depth))
            situation.insert(45, Form._create_situation(dungeon_map, depth+3, width-1, max_width, max_depth))
            situation.insert(46, Form._create_situation(dungeon_map, depth+3, width-2, max_width, max_depth))
            situation.insert(47, Form._create_situation(dungeon_map, depth+3, width-3, max_width, max_depth))
        elif now_way == WAY.LEFT:
            situation.insert(0, Form._create_situation(dungeon_map, depth+1, width, max_width, max_depth))
            situation.insert(1, Form._create_situation(dungeon_map, depth+1, width-1, max_width, max_depth))
            situation.insert(2, Form._create_situation(dungeon_map, depth, width-1, max_width, max_depth))
            situation.insert(3, Form._create_situation(dungeon_map, depth-1, width-1, max_width, max_depth))
            situation.insert(4, Form._create_situation(dungeon_map, depth-1, width, max_width, max_depth))
            situation.insert(5, Form._create_situation(dungeon_map, depth, width-2, max_width, max_depth))
            situation.insert(6, Form._create_situation(dungeon_map, depth+1, width-2, max_width, max_depth))
            situation.insert(7, Form._create_situation(dungeon_map, depth-1, width-2, max_width, max_depth))
            situation.insert(8, Form._create_situation(dungeon_map, depth, width-3, max_width, max_depth))
            situation.insert(9, Form._create_situation(dungeon_map, depth+1, width-3, max_width, max_depth))
            situation.insert(10, Form._create_situation(dungeon_map, depth-1, width-3, max_width, max_depth))
            situation.insert(11, Form._create_situation(dungeon_map, depth, width+1, max_width, max_depth))
            situation.insert(12, Form._create_situation(dungeon_map, depth+1, width+1, max_width, max_depth))
            situation.insert(13, Form._create_situation(dungeon_map, depth-1, width+1, max_width, max_depth))
            situation.insert(14, Form._create_situation(dungeon_map, depth, width+2, max_width, max_depth))
            situation.insert(15, Form._create_situation(dungeon_map, depth+1, width+2, max_width, max_depth))
            situation.insert(16, Form._create_situation(dungeon_map, depth-1, width+2, max_width, max_depth))
            situation.insert(17, Form._create_situation(dungeon_map, depth, width+3, max_width, max_depth))
            situation.insert(18, Form._create_situation(dungeon_map, depth+1, width+3, max_width, max_depth))
            situation.insert(19, Form._create_situation(dungeon_map, depth-1, width+3, max_width, max_depth))
            situation.insert(20, Form._create_situation(dungeon_map, depth+2, width-3, max_width, max_depth))
            situation.insert(21, Form._create_situation(dungeon_map, depth+2, width-2, max_width, max_depth))
            situation.insert(22, Form._create_situation(dungeon_map, depth+2, width-1, max_width, max_depth))
            situation.insert(23, Form._create_situation(dungeon_map, depth+2, width, max_width, max_depth))
            situation.insert(24, Form._create_situation(dungeon_map, depth+2, width+1, max_width, max_depth))
            situation.insert(25, Form._create_situation(dungeon_map, depth+2, width+2, max_width, max_depth))
            situation.insert(26, Form._create_situation(dungeon_map, depth+2, width+3, max_width, max_depth))
            situation.insert(27, Form._create_situation(dungeon_map, depth-2, width-3, max_width, max_depth))
            situation.insert(28, Form._create_situation(dungeon_map, depth-2, width-2, max_width, max_depth))
            situation.insert(29, Form._create_situation(dungeon_map, depth-2, width-1, max_width, max_depth))
            situation.insert(30, Form._create_situation(dungeon_map, depth-2, width, max_width, max_depth))
            situation.insert(31, Form._create_situation(dungeon_map, depth-2, width+1, max_width, max_depth))
            situation.insert(32, Form._create_situation(dungeon_map, depth-2, width+2, max_width, max_depth))
            situation.insert(33, Form._create_situation(dungeon_map, depth-2, width+3, max_width, max_depth))
            situation.insert(34, Form._create_situation(dungeon_map, depth+3, width-3, max_width, max_depth))
            situation.insert(35, Form._create_situation(dungeon_map, depth+3, width-2, max_width, max_depth))
            situation.insert(36, Form._create_situation(dungeon_map, depth+3, width-1, max_width, max_depth))
            situation.insert(37, Form._create_situation(dungeon_map, depth+3, width, max_width, max_depth))
            situation.insert(38, Form._create_situation(dungeon_map, depth+3, width+1, max_width, max_depth))
            situation.insert(39, Form._create_situation(dungeon_map, depth+3, width+2, max_width, max_depth))
            situation.insert(40, Form._create_situation(dungeon_map, depth+3, width+3, max_width, max_depth))
            situation.insert(41, Form._create_situation(dungeon_map, depth-3, width-3, max_width, max_depth))
            situation.insert(42, Form._create_situation(dungeon_map, depth-3, width-2, max_width, max_depth))
            situation.insert(43, Form._create_situation(dungeon_map, depth-3, width-1, max_width, max_depth))
            situation.insert(44, Form._create_situation(dungeon_map, depth-3, width, max_width, max_depth))
            situation.insert(45, Form._create_situation(dungeon_map, depth-3, width+1, max_width, max_depth))
            situation.insert(46, Form._create_situation(dungeon_map, depth-3, width+2, max_width, max_depth))
            situation.insert(47, Form._create_situation(dungeon_map, depth-3, width+3, max_width, max_depth))
        elif now_way == WAY.DOWN:
            situation.insert(0, Form._create_situation(dungeon_map, depth, width+1, max_width, max_depth))
            situation.insert(1, Form._create_situation(dungeon_map, depth+1, width+1, max_width, max_depth))
            situation.insert(2, Form._create_situation(dungeon_map, depth+1, width, max_width, max_depth))
            situation.insert(3, Form._create_situation(dungeon_map, depth+1, width-1, max_width, max_depth))
            situation.insert(4, Form._create_situation(dungeon_map, depth, width-1, max_width, max_depth))
            situation.insert(5, Form._create_situation(dungeon_map, depth+2, width, max_width, max_depth))
            situation.insert(6, Form._create_situation(dungeon_map, depth+2, width+1, max_width, max_depth))
            situation.insert(7, Form._create_situation(dungeon_map, depth+2, width-1, max_width, max_depth))
            situation.insert(8, Form._create_situation(dungeon_map, depth+3, width, max_width, max_depth))
            situation.insert(9, Form._create_situation(dungeon_map, depth+3, width+1, max_width, max_depth))
            situation.insert(10, Form._create_situation(dungeon_map, depth+3, width-1, max_width, max_depth))
            situation.insert(11, Form._create_situation(dungeon_map, depth-1, width, max_width, max_depth))
            situation.insert(12, Form._create_situation(dungeon_map, depth-1, width+1, max_width, max_depth))
            situation.insert(13, Form._create_situation(dungeon_map, depth-1, width-1, max_width, max_depth))
            situation.insert(14, Form._create_situation(dungeon_map, depth-2, width, max_width, max_depth))
            situation.insert(15, Form._create_situation(dungeon_map, depth-2, width+1, max_width, max_depth))
            situation.insert(16, Form._create_situation(dungeon_map, depth-2, width-1, max_width, max_depth))
            situation.insert(17, Form._create_situation(dungeon_map, depth-3, width, max_width, max_depth))
            situation.insert(18, Form._create_situation(dungeon_map, depth-3, width+1, max_width, max_depth))
            situation.insert(19, Form._create_situation(dungeon_map, depth-3, width-1, max_width, max_depth))
            situation.insert(20, Form._create_situation(dungeon_map, depth+3, width+2, max_width, max_depth))
            situation.insert(21, Form._create_situation(dungeon_map, depth+2, width+2, max_width, max_depth))
            situation.insert(22, Form._create_situation(dungeon_map, depth+1, width+2, max_width, max_depth))
            situation.insert(23, Form._create_situation(dungeon_map, depth, width+2, max_width, max_depth))
            situation.insert(24, Form._create_situation(dungeon_map, depth-1, width+2, max_width, max_depth))
            situation.insert(25, Form._create_situation(dungeon_map, depth-2, width+2, max_width, max_depth))
            situation.insert(26, Form._create_situation(dungeon_map, depth-3, width+2, max_width, max_depth))
            situation.insert(27, Form._create_situation(dungeon_map, depth+3, width-2, max_width, max_depth))
            situation.insert(28, Form._create_situation(dungeon_map, depth+2, width-2, max_width, max_depth))
            situation.insert(29, Form._create_situation(dungeon_map, depth+1, width-2, max_width, max_depth))
            situation.insert(30, Form._create_situation(dungeon_map, depth, width-2, max_width, max_depth))
            situation.insert(31, Form._create_situation(dungeon_map, depth-1, width-2, max_width, max_depth))
            situation.insert(32, Form._create_situation(dungeon_map, depth-2, width-2, max_width, max_depth))
            situation.insert(33, Form._create_situation(dungeon_map, depth-3, width-2, max_width, max_depth))
            situation.insert(34, Form._create_situation(dungeon_map, depth+3, width+3, max_width, max_depth))
            situation.insert(35, Form._create_situation(dungeon_map, depth+2, width+3, max_width, max_depth))
            situation.insert(36, Form._create_situation(dungeon_map, depth+1, width+3, max_width, max_depth))
            situation.insert(37, Form._create_situation(dungeon_map, depth, width+3, max_width, max_depth))
            situation.insert(38, Form._create_situation(dungeon_map, depth-1, width+3, max_width, max_depth))
            situation.insert(39, Form._create_situation(dungeon_map, depth-2, width+3, max_width, max_depth))
            situation.insert(40, Form._create_situation(dungeon_map, depth-3, width+3, max_width, max_depth))
            situation.insert(41, Form._create_situation(dungeon_map, depth+3, width-3, max_width, max_depth))
            situation.insert(42, Form._create_situation(dungeon_map, depth+2, width-3, max_width, max_depth))
            situation.insert(43, Form._create_situation(dungeon_map, depth+1, width-3, max_width, max_depth))
            situation.insert(44, Form._create_situation(dungeon_map, depth, width-3, max_width, max_depth))
            situation.insert(45, Form._create_situation(dungeon_map, depth-1, width-3, max_width, max_depth))
            situation.insert(46, Form._create_situation(dungeon_map, depth-2, width-3, max_width, max_depth))
            situation.insert(47, Form._create_situation(dungeon_map, depth-3, width-3, max_width, max_depth))
        return situation

    @staticmethod
    def _create_situation(dungeon_map, depth, width, max_width, max_depth):
        return [cmnDungeon.Common.isPosPath(dungeon_map, depth, width, max_width, max_depth), depth, width]
