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
        if 0 < floor and floor <= len(dungeon):
            initMap = dungeon[floor-1].map
            initWay = dungeon[floor-1].start_way
            init_pos = dungeon[floor-1].start_pos
            goal_pos = dungeon[floor-1].goal_pos
            maxWidth = dungeon[floor-1].maxWidth
            maxDepth = dungeon[floor-1].maxDepth
            enemyList = dungeon[floor-1].enemyList
            eventList = dungeon[floor-1].eventList
            itemList = dungeon[floor-1].itemList
        else:
            initMap = dungeon[0].map
            initWay = dungeon[0].start_way
            init_pos = dungeon[0].start_pos
            goal_pos = dungeon[0].goal_pos
            maxWidth = dungeon[0].maxWidth
            maxDepth = dungeon[0].maxDepth
            enemyList = dungeon[0].enemyList
            eventList = dungeon[0].eventList
            itemList = dungeon[0].itemList
            dbg.ERROR_LOG("[MapForm.__init__]存在しない階数を指定しています")
            dbg.ERROR_LOG("[MapForm.__init__]暫定的に1階で初期化します")
        self.__floor = floor
        self.__nowWay = initWay
        self.__preWay = initWay
        self.__nowPos = [init_pos.x, init_pos.y]
        self.__prePos = [init_pos.x, init_pos.y]
        self.__startPos = [init_pos.x, init_pos.y]
        self.__goalPos = [goal_pos.x, goal_pos.y]
        self.__maxWidth = maxWidth
        self.__maxDepth = maxDepth
        self.__situation = Form.__get_situation(initMap, initWay, init_pos.x, init_pos.y, maxWidth, maxDepth)
        self.__nowView = Form.__set_view(self.__situation)
        self.__preView = self.__nowView
        self.__map = initMap
        self.__enemiesForm = EnemiesForm.Form()
        self.__enemiesForm.regist(enemyList)
        self.__eventsForm = EventsForm.Form()
        self.__eventsForm.regist(eventList)
        self.__itemsForm = ItemsForm.Form()
        self.__itemsForm.register(itemList)

    def reset(self, floor=1):
        if 0 < floor and floor <= len(dungeon):
            initMap = dungeon[floor-1].map
            initWay = dungeon[floor-1].start_way
            init_pos = dungeon[floor-1].start_pos
            goal_pos = dungeon[floor-1].goal_pos
            maxWidth = dungeon[floor-1].maxWidth
            maxDepth = dungeon[floor-1].maxDepth
            enemyList = dungeon[floor-1].enemyList
            eventList = dungeon[floor-1].eventList
            itemList = dungeon[floor-1].itemList
            self.__floor = floor
            self.__nowWay = initWay
            self.__preWay = initWay
            self.__nowPos = [init_pos.x, init_pos.y]
            self.__prePos = [init_pos.x, init_pos.y]
            self.__startPos = [init_pos.x, init_pos.y]
            self.__goalPos = [goal_pos.x, goal_pos.y]
            self.__maxWidth = maxWidth
            self.__maxDepth = maxDepth
            self.__situation = Form.__get_situation(initMap, initWay, init_pos.x, init_pos.y, maxWidth, maxDepth)
            self.__nowView = Form.__set_view(self.__situation)
            self.__preView = self.__nowView
            self.__map = initMap
            self.__enemiesForm.regist(enemyList)
            self.__eventsForm.regist(eventList)
            self.__itemsForm.register(itemList)
        else:
            dbg.ERROR_LOG("[MapForm.__set]存在しない階数を指定しています")

    def set_pre_way(self):
        self.__preWay = self.__nowWay

    def set_now_way(self, way: int):
        self.__nowWay = way

    def set_pos(self, pos: list[int]):
        self.__prePos = self.__nowPos
        self.__nowPos = pos

    def set_pre_view(self):
        self.__preView = self.__nowView

    def set_now_view(self):
        self.__nowView = Form.__set_view(self.__situation)

    def set_situation(self):
        Map = self.__map
        Way = self.__nowWay
        Pos = self.__nowPos
        Width = self.__maxWidth
        Depth = self.__maxDepth
        self.__situation = Form.__get_situation(Map, Way, Pos[0], Pos[1], Width, Depth)

    def FLOOR(self):
        return self.__floor

    def NOW_WAY(self):
        return self.__nowWay

    def NOW_POS(self):
        return self.__nowPos

    def NOW_VIEW(self):
        return self.__nowView

    def PRE_WAY(self):
        return self.__preWay

    def PRE_POS(self):
        return self.__prePos

    def PRE_VIEW(self):
        return self.__preView

    def SITUATION(self):
        return self.__situation

    def MAP(self):
        return self.__map

    def MAX_WIDTH(self):
        return self.__maxWidth

    def MAX_DEPTH(self):
        return self.__maxDepth

    def existDiffWay(self):
        return self.__preWay != self.__nowWay

    def existDiffPos(self):
        return self.__prePos[0] == self.__nowPos[0] and self.__prePos[1] == self.__nowPos[1]

    def existDiffView(self):
        return self.__preView != self.__nowView

    def ENEMY_COUNT(self):
        return self.__enemiesForm.ENEMY_COUNT()

    def disappearanceEnemy(self, index):
        self.__enemiesForm.disappearanceEnemy(index)

    def APPEAR_FLAG(self, index):
        return self.__enemiesForm.APPEAR_FLAG(index)

    def ENEMY_TYPE(self, index):
        return self.__enemiesForm.ENEMY_TYPE(index)

    def ENEMY_POS(self, index):
        return self.__enemiesForm.ENEMY_POS(index)

    def enemyMove(self):
        return self.__enemiesForm.enemyMove()

    def EVENT_FONT(self):
        self.__eventsForm.EVENT_FONT()

    def getEventText(self):
        return self.__eventsForm.getEventText(self.__nowPos, self.__nowWay)

    def eventFlagOff(self):
        self.__eventsForm.eventFlagOff(self.__nowPos)

    def getItem(self):
        return self.__itemsForm.getItem(self.__nowPos)

    def itemFlagOff(self):
        return self.__itemsForm.flagOff()

    def ITEM_GET_FLAG(self):
        return self.__itemsForm.ITEM_GET_FLAG()

    def START_POS(self):
        return self.__startPos

    def GOAL_POS(self):
        return self.__goalPos

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
    def __get_situation(map, now_way, depth, width, max_width, max_depth):
        situation = []
        if now_way == WAY.UP:
            situation.insert(0, Form.__create_situation(map, depth, width-1, max_width, max_depth))
            situation.insert(1, Form.__create_situation(map, depth-1, width-1, max_width, max_depth))
            situation.insert(2, Form.__create_situation(map, depth-1, width, max_width, max_depth))
            situation.insert(3, Form.__create_situation(map, depth-1, width+1, max_width, max_depth))
            situation.insert(4, Form.__create_situation(map, depth, width+1, max_width, max_depth))
            situation.insert(5, Form.__create_situation(map, depth-2, width, max_width, max_depth))
            situation.insert(6, Form.__create_situation(map, depth-2, width-1, max_width, max_depth))
            situation.insert(7, Form.__create_situation(map, depth-2, width+1, max_width, max_depth))
            situation.insert(8, Form.__create_situation(map, depth-3, width, max_width, max_depth))
            situation.insert(9, Form.__create_situation(map, depth-3, width-1, max_width, max_depth))
            situation.insert(10, Form.__create_situation(map, depth-3, width+1, max_width, max_depth))
            situation.insert(11, Form.__create_situation(map, depth+1, width, max_width, max_depth))
            situation.insert(12, Form.__create_situation(map, depth+1, width-1, max_width, max_depth))
            situation.insert(13, Form.__create_situation(map, depth+1, width+1, max_width, max_depth))
            situation.insert(14, Form.__create_situation(map, depth+2, width, max_width, max_depth))
            situation.insert(15, Form.__create_situation(map, depth+2, width-1, max_width, max_depth))
            situation.insert(16, Form.__create_situation(map, depth+2, width+1, max_width, max_depth))
            situation.insert(17, Form.__create_situation(map, depth+3, width, max_width, max_depth))
            situation.insert(18, Form.__create_situation(map, depth+3, width-1, max_width, max_depth))
            situation.insert(19, Form.__create_situation(map, depth+3, width+1, max_width, max_depth))
            situation.insert(20, Form.__create_situation(map, depth-3, width-2, max_width, max_depth))
            situation.insert(21, Form.__create_situation(map, depth-2, width-2, max_width, max_depth))
            situation.insert(22, Form.__create_situation(map, depth-1, width-2, max_width, max_depth))
            situation.insert(23, Form.__create_situation(map, depth, width-2, max_width, max_depth))
            situation.insert(24, Form.__create_situation(map, depth+1, width-2, max_width, max_depth))
            situation.insert(25, Form.__create_situation(map, depth+2, width-2, max_width, max_depth))
            situation.insert(26, Form.__create_situation(map, depth+3, width-2, max_width, max_depth))
            situation.insert(27, Form.__create_situation(map, depth-3, width+2, max_width, max_depth))
            situation.insert(28, Form.__create_situation(map, depth-2, width+2, max_width, max_depth))
            situation.insert(29, Form.__create_situation(map, depth-1, width+2, max_width, max_depth))
            situation.insert(30, Form.__create_situation(map, depth, width+2, max_width, max_depth))
            situation.insert(31, Form.__create_situation(map, depth+1, width+2, max_width, max_depth))
            situation.insert(32, Form.__create_situation(map, depth+2, width+2, max_width, max_depth))
            situation.insert(33, Form.__create_situation(map, depth+3, width+2, max_width, max_depth))
            situation.insert(34, Form.__create_situation(map, depth-3, width-3, max_width, max_depth))
            situation.insert(35, Form.__create_situation(map, depth-2, width-3, max_width, max_depth))
            situation.insert(36, Form.__create_situation(map, depth-1, width-3, max_width, max_depth))
            situation.insert(37, Form.__create_situation(map, depth, width-3, max_width, max_depth))
            situation.insert(38, Form.__create_situation(map, depth+1, width-3, max_width, max_depth))
            situation.insert(39, Form.__create_situation(map, depth+2, width-3, max_width, max_depth))
            situation.insert(40, Form.__create_situation(map, depth+3, width-3, max_width, max_depth))
            situation.insert(41, Form.__create_situation(map, depth-3, width+3, max_width, max_depth))
            situation.insert(42, Form.__create_situation(map, depth-2, width+3, max_width, max_depth))
            situation.insert(43, Form.__create_situation(map, depth-1, width+3, max_width, max_depth))
            situation.insert(44, Form.__create_situation(map, depth, width+3, max_width, max_depth))
            situation.insert(45, Form.__create_situation(map, depth+1, width+3, max_width, max_depth))
            situation.insert(46, Form.__create_situation(map, depth+2, width+3, max_width, max_depth))
            situation.insert(47, Form.__create_situation(map, depth+3, width+3, max_width, max_depth))
        elif now_way == WAY.RIGHT:
            situation.insert(0, Form.__create_situation(map, depth-1, width, max_width, max_depth))
            situation.insert(1, Form.__create_situation(map, depth-1, width+1, max_width, max_depth))
            situation.insert(2, Form.__create_situation(map, depth, width+1, max_width, max_depth))
            situation.insert(3, Form.__create_situation(map, depth+1, width+1, max_width, max_depth))
            situation.insert(4, Form.__create_situation(map, depth+1, width, max_width, max_depth))
            situation.insert(5, Form.__create_situation(map, depth, width+2, max_width, max_depth))
            situation.insert(6, Form.__create_situation(map, depth-1, width+2, max_width, max_depth))
            situation.insert(7, Form.__create_situation(map, depth+1, width+2, max_width, max_depth))
            situation.insert(8, Form.__create_situation(map, depth, width+3, max_width, max_depth))
            situation.insert(9, Form.__create_situation(map, depth-1, width+3, max_width, max_depth))
            situation.insert(10, Form.__create_situation(map, depth+1, width+3, max_width, max_depth))
            situation.insert(11, Form.__create_situation(map, depth, width-1, max_width, max_depth))
            situation.insert(12, Form.__create_situation(map, depth-1, width-1, max_width, max_depth))
            situation.insert(13, Form.__create_situation(map, depth+1, width-1, max_width, max_depth))
            situation.insert(14, Form.__create_situation(map, depth, width-2, max_width, max_depth))
            situation.insert(15, Form.__create_situation(map, depth-1, width-2, max_width, max_depth))
            situation.insert(16, Form.__create_situation(map, depth+1, width-2, max_width, max_depth))
            situation.insert(17, Form.__create_situation(map, depth, width-3, max_width, max_depth))
            situation.insert(18, Form.__create_situation(map, depth-1, width-3, max_width, max_depth))
            situation.insert(19, Form.__create_situation(map, depth+1, width-3, max_width, max_depth))
            situation.insert(20, Form.__create_situation(map, depth-2, width+3, max_width, max_depth))
            situation.insert(21, Form.__create_situation(map, depth-2, width+2, max_width, max_depth))
            situation.insert(22, Form.__create_situation(map, depth-2, width+1, max_width, max_depth))
            situation.insert(23, Form.__create_situation(map, depth-2, width, max_width, max_depth))
            situation.insert(24, Form.__create_situation(map, depth-2, width-1, max_width, max_depth))
            situation.insert(25, Form.__create_situation(map, depth-2, width-2, max_width, max_depth))
            situation.insert(26, Form.__create_situation(map, depth-2, width-3, max_width, max_depth))
            situation.insert(27, Form.__create_situation(map, depth+2, width+3, max_width, max_depth))
            situation.insert(28, Form.__create_situation(map, depth+2, width+2, max_width, max_depth))
            situation.insert(29, Form.__create_situation(map, depth+2, width+1, max_width, max_depth))
            situation.insert(30, Form.__create_situation(map, depth+2, width, max_width, max_depth))
            situation.insert(31, Form.__create_situation(map, depth+2, width-1, max_width, max_depth))
            situation.insert(32, Form.__create_situation(map, depth+2, width-2, max_width, max_depth))
            situation.insert(33, Form.__create_situation(map, depth+2, width-3, max_width, max_depth))
            situation.insert(34, Form.__create_situation(map, depth-3, width+3, max_width, max_depth))
            situation.insert(35, Form.__create_situation(map, depth-3, width+2, max_width, max_depth))
            situation.insert(36, Form.__create_situation(map, depth-3, width+1, max_width, max_depth))
            situation.insert(37, Form.__create_situation(map, depth-3, width, max_width, max_depth))
            situation.insert(38, Form.__create_situation(map, depth-3, width-1, max_width, max_depth))
            situation.insert(39, Form.__create_situation(map, depth-3, width-2, max_width, max_depth))
            situation.insert(40, Form.__create_situation(map, depth-3, width-3, max_width, max_depth))
            situation.insert(41, Form.__create_situation(map, depth+3, width+3, max_width, max_depth))
            situation.insert(42, Form.__create_situation(map, depth+3, width+2, max_width, max_depth))
            situation.insert(43, Form.__create_situation(map, depth+3, width+1, max_width, max_depth))
            situation.insert(44, Form.__create_situation(map, depth+3, width, max_width, max_depth))
            situation.insert(45, Form.__create_situation(map, depth+3, width-1, max_width, max_depth))
            situation.insert(46, Form.__create_situation(map, depth+3, width-2, max_width, max_depth))
            situation.insert(47, Form.__create_situation(map, depth+3, width-3, max_width, max_depth))
        elif now_way == WAY.LEFT:
            situation.insert(0, Form.__create_situation(map, depth+1, width, max_width, max_depth))
            situation.insert(1, Form.__create_situation(map, depth+1, width-1, max_width, max_depth))
            situation.insert(2, Form.__create_situation(map, depth, width-1, max_width, max_depth))
            situation.insert(3, Form.__create_situation(map, depth-1, width-1, max_width, max_depth))
            situation.insert(4, Form.__create_situation(map, depth-1, width, max_width, max_depth))
            situation.insert(5, Form.__create_situation(map, depth, width-2, max_width, max_depth))
            situation.insert(6, Form.__create_situation(map, depth+1, width-2, max_width, max_depth))
            situation.insert(7, Form.__create_situation(map, depth-1, width-2, max_width, max_depth))
            situation.insert(8, Form.__create_situation(map, depth, width-3, max_width, max_depth))
            situation.insert(9, Form.__create_situation(map, depth+1, width-3, max_width, max_depth))
            situation.insert(10, Form.__create_situation(map, depth-1, width-3, max_width, max_depth))
            situation.insert(11, Form.__create_situation(map, depth, width+1, max_width, max_depth))
            situation.insert(12, Form.__create_situation(map, depth+1, width+1, max_width, max_depth))
            situation.insert(13, Form.__create_situation(map, depth-1, width+1, max_width, max_depth))
            situation.insert(14, Form.__create_situation(map, depth, width+2, max_width, max_depth))
            situation.insert(15, Form.__create_situation(map, depth+1, width+2, max_width, max_depth))
            situation.insert(16, Form.__create_situation(map, depth-1, width+2, max_width, max_depth))
            situation.insert(17, Form.__create_situation(map, depth, width+3, max_width, max_depth))
            situation.insert(18, Form.__create_situation(map, depth+1, width+3, max_width, max_depth))
            situation.insert(19, Form.__create_situation(map, depth-1, width+3, max_width, max_depth))
            situation.insert(20, Form.__create_situation(map, depth+2, width-3, max_width, max_depth))
            situation.insert(21, Form.__create_situation(map, depth+2, width-2, max_width, max_depth))
            situation.insert(22, Form.__create_situation(map, depth+2, width-1, max_width, max_depth))
            situation.insert(23, Form.__create_situation(map, depth+2, width, max_width, max_depth))
            situation.insert(24, Form.__create_situation(map, depth+2, width+1, max_width, max_depth))
            situation.insert(25, Form.__create_situation(map, depth+2, width+2, max_width, max_depth))
            situation.insert(26, Form.__create_situation(map, depth+2, width+3, max_width, max_depth))
            situation.insert(27, Form.__create_situation(map, depth-2, width-3, max_width, max_depth))
            situation.insert(28, Form.__create_situation(map, depth-2, width-2, max_width, max_depth))
            situation.insert(29, Form.__create_situation(map, depth-2, width-1, max_width, max_depth))
            situation.insert(30, Form.__create_situation(map, depth-2, width, max_width, max_depth))
            situation.insert(31, Form.__create_situation(map, depth-2, width+1, max_width, max_depth))
            situation.insert(32, Form.__create_situation(map, depth-2, width+2, max_width, max_depth))
            situation.insert(33, Form.__create_situation(map, depth-2, width+3, max_width, max_depth))
            situation.insert(34, Form.__create_situation(map, depth+3, width-3, max_width, max_depth))
            situation.insert(35, Form.__create_situation(map, depth+3, width-2, max_width, max_depth))
            situation.insert(36, Form.__create_situation(map, depth+3, width-1, max_width, max_depth))
            situation.insert(37, Form.__create_situation(map, depth+3, width, max_width, max_depth))
            situation.insert(38, Form.__create_situation(map, depth+3, width+1, max_width, max_depth))
            situation.insert(39, Form.__create_situation(map, depth+3, width+2, max_width, max_depth))
            situation.insert(40, Form.__create_situation(map, depth+3, width+3, max_width, max_depth))
            situation.insert(41, Form.__create_situation(map, depth-3, width-3, max_width, max_depth))
            situation.insert(42, Form.__create_situation(map, depth-3, width-2, max_width, max_depth))
            situation.insert(43, Form.__create_situation(map, depth-3, width-1, max_width, max_depth))
            situation.insert(44, Form.__create_situation(map, depth-3, width, max_width, max_depth))
            situation.insert(45, Form.__create_situation(map, depth-3, width+1, max_width, max_depth))
            situation.insert(46, Form.__create_situation(map, depth-3, width+2, max_width, max_depth))
            situation.insert(47, Form.__create_situation(map, depth-3, width+3, max_width, max_depth))
        elif now_way == WAY.DOWN:
            situation.insert(0, Form.__create_situation(map, depth, width+1, max_width, max_depth))
            situation.insert(1, Form.__create_situation(map, depth+1, width+1, max_width, max_depth))
            situation.insert(2, Form.__create_situation(map, depth+1, width, max_width, max_depth))
            situation.insert(3, Form.__create_situation(map, depth+1, width-1, max_width, max_depth))
            situation.insert(4, Form.__create_situation(map, depth, width-1, max_width, max_depth))
            situation.insert(5, Form.__create_situation(map, depth+2, width, max_width, max_depth))
            situation.insert(6, Form.__create_situation(map, depth+2, width+1, max_width, max_depth))
            situation.insert(7, Form.__create_situation(map, depth+2, width-1, max_width, max_depth))
            situation.insert(8, Form.__create_situation(map, depth+3, width, max_width, max_depth))
            situation.insert(9, Form.__create_situation(map, depth+3, width+1, max_width, max_depth))
            situation.insert(10, Form.__create_situation(map, depth+3, width-1, max_width, max_depth))
            situation.insert(11, Form.__create_situation(map, depth-1, width, max_width, max_depth))
            situation.insert(12, Form.__create_situation(map, depth-1, width+1, max_width, max_depth))
            situation.insert(13, Form.__create_situation(map, depth-1, width-1, max_width, max_depth))
            situation.insert(14, Form.__create_situation(map, depth-2, width, max_width, max_depth))
            situation.insert(15, Form.__create_situation(map, depth-2, width+1, max_width, max_depth))
            situation.insert(16, Form.__create_situation(map, depth-2, width-1, max_width, max_depth))
            situation.insert(17, Form.__create_situation(map, depth-3, width, max_width, max_depth))
            situation.insert(18, Form.__create_situation(map, depth-3, width+1, max_width, max_depth))
            situation.insert(19, Form.__create_situation(map, depth-3, width-1, max_width, max_depth))
            situation.insert(20, Form.__create_situation(map, depth+3, width+2, max_width, max_depth))
            situation.insert(21, Form.__create_situation(map, depth+2, width+2, max_width, max_depth))
            situation.insert(22, Form.__create_situation(map, depth+1, width+2, max_width, max_depth))
            situation.insert(23, Form.__create_situation(map, depth, width+2, max_width, max_depth))
            situation.insert(24, Form.__create_situation(map, depth-1, width+2, max_width, max_depth))
            situation.insert(25, Form.__create_situation(map, depth-2, width+2, max_width, max_depth))
            situation.insert(26, Form.__create_situation(map, depth-3, width+2, max_width, max_depth))
            situation.insert(27, Form.__create_situation(map, depth+3, width-2, max_width, max_depth))
            situation.insert(28, Form.__create_situation(map, depth+2, width-2, max_width, max_depth))
            situation.insert(29, Form.__create_situation(map, depth+1, width-2, max_width, max_depth))
            situation.insert(30, Form.__create_situation(map, depth, width-2, max_width, max_depth))
            situation.insert(31, Form.__create_situation(map, depth-1, width-2, max_width, max_depth))
            situation.insert(32, Form.__create_situation(map, depth-2, width-2, max_width, max_depth))
            situation.insert(33, Form.__create_situation(map, depth-3, width-2, max_width, max_depth))
            situation.insert(34, Form.__create_situation(map, depth+3, width+3, max_width, max_depth))
            situation.insert(35, Form.__create_situation(map, depth+2, width+3, max_width, max_depth))
            situation.insert(36, Form.__create_situation(map, depth+1, width+3, max_width, max_depth))
            situation.insert(37, Form.__create_situation(map, depth, width+3, max_width, max_depth))
            situation.insert(38, Form.__create_situation(map, depth-1, width+3, max_width, max_depth))
            situation.insert(39, Form.__create_situation(map, depth-2, width+3, max_width, max_depth))
            situation.insert(40, Form.__create_situation(map, depth-3, width+3, max_width, max_depth))
            situation.insert(41, Form.__create_situation(map, depth+3, width-3, max_width, max_depth))
            situation.insert(42, Form.__create_situation(map, depth+2, width-3, max_width, max_depth))
            situation.insert(43, Form.__create_situation(map, depth+1, width-3, max_width, max_depth))
            situation.insert(44, Form.__create_situation(map, depth, width-3, max_width, max_depth))
            situation.insert(45, Form.__create_situation(map, depth-1, width-3, max_width, max_depth))
            situation.insert(46, Form.__create_situation(map, depth-2, width-3, max_width, max_depth))
            situation.insert(47, Form.__create_situation(map, depth-3, width-3, max_width, max_depth))
        return situation

    @staticmethod
    def __create_situation(map, depth, width, max_width, max_depth):
        return [cmnDungeon.Common.isPosPath(map, depth, width, max_width, max_depth), depth, width]
