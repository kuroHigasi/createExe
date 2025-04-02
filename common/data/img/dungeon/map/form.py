import dungeon.data.map.map as dungeonMap
import dungeon.enemies.form as EnemiesForm
import dungeon.events.form as EventsForm
import dungeon.items.form as ItemsForm
import common.debug.debug as dbg
import dungeon.data.img.img as dungeonImg
import dungeon.pyd.way as WAY
import dungeon.common as cmnDungeon


dungeon = [dungeonMap.FirstFloor, dungeonMap.SecondFloor, dungeonMap.ThirdFloor, dungeonMap.ForthFloor]


class Form:
    def __init__(self, floor=1):
        if 0 < floor and floor <= len(dungeon):
            initMap = dungeon[floor-1].map
            initWay = dungeon[floor-1].start_way
            initPos = dungeon[floor-1].start_pos
            goalPos = dungeon[floor-1].goal_pos
            maxWidth = dungeon[floor-1].maxWidth
            maxDepth = dungeon[floor-1].maxDepth
            enemyList = dungeon[floor-1].enemyList
            eventList = dungeon[floor-1].eventList
            itemList = dungeon[floor-1].itemList
        else:
            initMap = dungeon[0].map
            initWay = dungeon[0].start_way
            initPos = dungeon[0].start_pos
            goalPos = dungeon[0].goal_pos
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
        self.__nowPos = initPos
        self.__prePos = initPos
        self.__startPos = initPos
        self.__goalPos = goalPos
        self.__maxWidth = maxWidth
        self.__maxDepth = maxDepth
        self.__situation = Form.__getSituation(initMap, initWay, initPos[0], initPos[1], maxWidth, maxDepth)
        self.__nowView = Form.__setView(self.__situation)
        self.__preView = self.__nowView
        self.__map = initMap
        self.__enemiesForm = EnemiesForm.Form()
        self.__enemiesForm.regist(enemyList)
        self.__eventsForm = EventsForm.Form()
        self.__eventsForm.regist(eventList)
        self.__itemsForm = ItemsForm.Form()
        self.__itemsForm.regist(itemList)

    def reset(self, floor=1):
        if 0 < floor and floor <= len(dungeon):
            initMap = dungeon[floor-1].map
            initWay = dungeon[floor-1].start_way
            initPos = dungeon[floor-1].start_pos
            goalPos = dungeon[floor-1].goal_pos
            maxWidth = dungeon[floor-1].maxWidth
            maxDepth = dungeon[floor-1].maxDepth
            enemyList = dungeon[floor-1].enemyList
            eventList = dungeon[floor-1].eventList
            itemList = dungeon[floor-1].itemList
            self.__floor = floor
            self.__nowWay = initWay
            self.__preWay = initWay
            self.__nowPos = initPos
            self.__prePos = initPos
            self.__startPos = initPos
            self.__goalPos = goalPos
            self.__maxWidth = maxWidth
            self.__maxDepth = maxDepth
            self.__situation = Form.__getSituation(initMap, initWay, initPos[0], initPos[1], maxWidth, maxDepth)
            self.__nowView = Form.__setView(self.__situation)
            self.__preView = self.__nowView
            self.__map = initMap
            self.__enemiesForm.regist(enemyList)
            self.__eventsForm.regist(eventList)
            self.__itemsForm.regist(itemList)
        else:
            dbg.ERROR_LOG("[MapForm.__set]存在しない階数を指定しています")

    def updateWay(self, way: int):
        self.__preWay = self.__nowWay
        self.__nowWay = way

    def updatePos(self, pos: list[int]):
        self.__prePos = self.__nowPos
        self.__nowPos = pos

    def updateView(self):
        self.__preView = self.__nowView
        self.__nowView = Form.__setView(self.__situation)

    def updateSituation(self):
        Map = self.__map
        Way = self.__nowWay
        Pos = self.__nowPos
        Width = self.__maxWidth
        Depth = self.__maxDepth
        self.__situation = Form.__getSituation(Map, Way, Pos[0], Pos[1], Width, Depth)

    def updateMap(self, map: list[int]):
        self.__map = map

    def updateMaxDepth(self, max_width: int):
        self.__maxWidth = max_width

    def updateMaxWidth(self, max_depth: int):
        self.__maxDepth = max_depth

    def DUNGEON_FLOOR_MAX(self):
        return len(dungeon)

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
        return self.__preWay == self.__nowWay

    def existDiffPos(self):
        return self.__prePos[0] == self.__nowPos[0] and self.__prePos[1] == self.__nowPos[1]

    def existDiffView(self):
        return self.__preView == self.__nowView

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

    def __setView(situation):
        status = 0x000
        # L pos set
        status = dungeonImg.pos.L(situation, status)
        # C pos set
        status = dungeonImg.pos.C(situation, status)
        # R pos set
        status = dungeonImg.pos.R(situation, status)
        return status

    def __getSituation(map, now_way, depth, width, maxWidth, maxDepth):
        sSituation = []
        if now_way == WAY.UP:
            sSituation.insert(0, Form.__createSituation(map, depth, width-1, maxWidth, maxDepth))
            sSituation.insert(1, Form.__createSituation(map, depth-1, width-1, maxWidth, maxDepth))
            sSituation.insert(2, Form.__createSituation(map, depth-1, width, maxWidth, maxDepth))
            sSituation.insert(3, Form.__createSituation(map, depth-1, width+1, maxWidth, maxDepth))
            sSituation.insert(4, Form.__createSituation(map, depth, width+1, maxWidth, maxDepth))
            sSituation.insert(5, Form.__createSituation(map, depth-2, width, maxWidth, maxDepth))
            sSituation.insert(6, Form.__createSituation(map, depth-2, width-1, maxWidth, maxDepth))
            sSituation.insert(7, Form.__createSituation(map, depth-2, width+1, maxWidth, maxDepth))
            sSituation.insert(8, Form.__createSituation(map, depth-3, width, maxWidth, maxDepth))
            sSituation.insert(9, Form.__createSituation(map, depth-3, width-1, maxWidth, maxDepth))
            sSituation.insert(10, Form.__createSituation(map, depth-3, width+1, maxWidth, maxDepth))
            sSituation.insert(11, Form.__createSituation(map, depth+1, width, maxWidth, maxDepth))
            sSituation.insert(12, Form.__createSituation(map, depth+1, width-1, maxWidth, maxDepth))
            sSituation.insert(13, Form.__createSituation(map, depth+1, width+1, maxWidth, maxDepth))
            sSituation.insert(14, Form.__createSituation(map, depth+2, width, maxWidth, maxDepth))
            sSituation.insert(15, Form.__createSituation(map, depth+2, width-1, maxWidth, maxDepth))
            sSituation.insert(16, Form.__createSituation(map, depth+2, width+1, maxWidth, maxDepth))
            sSituation.insert(17, Form.__createSituation(map, depth+3, width, maxWidth, maxDepth))
            sSituation.insert(18, Form.__createSituation(map, depth+3, width-1, maxWidth, maxDepth))
            sSituation.insert(19, Form.__createSituation(map, depth+3, width+1, maxWidth, maxDepth))
            sSituation.insert(20, Form.__createSituation(map, depth-3, width-2, maxWidth, maxDepth))
            sSituation.insert(21, Form.__createSituation(map, depth-2, width-2, maxWidth, maxDepth))
            sSituation.insert(22, Form.__createSituation(map, depth-1, width-2, maxWidth, maxDepth))
            sSituation.insert(23, Form.__createSituation(map, depth, width-2, maxWidth, maxDepth))
            sSituation.insert(24, Form.__createSituation(map, depth+1, width-2, maxWidth, maxDepth))
            sSituation.insert(25, Form.__createSituation(map, depth+2, width-2, maxWidth, maxDepth))
            sSituation.insert(26, Form.__createSituation(map, depth+3, width-2, maxWidth, maxDepth))
            sSituation.insert(27, Form.__createSituation(map, depth-3, width+2, maxWidth, maxDepth))
            sSituation.insert(28, Form.__createSituation(map, depth-2, width+2, maxWidth, maxDepth))
            sSituation.insert(29, Form.__createSituation(map, depth-1, width+2, maxWidth, maxDepth))
            sSituation.insert(30, Form.__createSituation(map, depth, width+2, maxWidth, maxDepth))
            sSituation.insert(31, Form.__createSituation(map, depth+1, width+2, maxWidth, maxDepth))
            sSituation.insert(32, Form.__createSituation(map, depth+2, width+2, maxWidth, maxDepth))
            sSituation.insert(33, Form.__createSituation(map, depth+3, width+2, maxWidth, maxDepth))
            sSituation.insert(34, Form.__createSituation(map, depth-3, width-3, maxWidth, maxDepth))
            sSituation.insert(35, Form.__createSituation(map, depth-2, width-3, maxWidth, maxDepth))
            sSituation.insert(36, Form.__createSituation(map, depth-1, width-3, maxWidth, maxDepth))
            sSituation.insert(37, Form.__createSituation(map, depth, width-3, maxWidth, maxDepth))
            sSituation.insert(38, Form.__createSituation(map, depth+1, width-3, maxWidth, maxDepth))
            sSituation.insert(39, Form.__createSituation(map, depth+2, width-3, maxWidth, maxDepth))
            sSituation.insert(40, Form.__createSituation(map, depth+3, width-3, maxWidth, maxDepth))
            sSituation.insert(41, Form.__createSituation(map, depth-3, width+3, maxWidth, maxDepth))
            sSituation.insert(42, Form.__createSituation(map, depth-2, width+3, maxWidth, maxDepth))
            sSituation.insert(43, Form.__createSituation(map, depth-1, width+3, maxWidth, maxDepth))
            sSituation.insert(44, Form.__createSituation(map, depth, width+3, maxWidth, maxDepth))
            sSituation.insert(45, Form.__createSituation(map, depth+1, width+3, maxWidth, maxDepth))
            sSituation.insert(46, Form.__createSituation(map, depth+2, width+3, maxWidth, maxDepth))
            sSituation.insert(47, Form.__createSituation(map, depth+3, width+3, maxWidth, maxDepth))
        elif now_way == WAY.RIGHT:
            sSituation.insert(0, Form.__createSituation(map, depth-1, width, maxWidth, maxDepth))
            sSituation.insert(1, Form.__createSituation(map, depth-1, width+1, maxWidth, maxDepth))
            sSituation.insert(2, Form.__createSituation(map, depth, width+1, maxWidth, maxDepth))
            sSituation.insert(3, Form.__createSituation(map, depth+1, width+1, maxWidth, maxDepth))
            sSituation.insert(4, Form.__createSituation(map, depth+1, width, maxWidth, maxDepth))
            sSituation.insert(5, Form.__createSituation(map, depth, width+2, maxWidth, maxDepth))
            sSituation.insert(6, Form.__createSituation(map, depth-1, width+2, maxWidth, maxDepth))
            sSituation.insert(7, Form.__createSituation(map, depth+1, width+2, maxWidth, maxDepth))
            sSituation.insert(8, Form.__createSituation(map, depth, width+3, maxWidth, maxDepth))
            sSituation.insert(9, Form.__createSituation(map, depth-1, width+3, maxWidth, maxDepth))
            sSituation.insert(10, Form.__createSituation(map, depth+1, width+3, maxWidth, maxDepth))
            sSituation.insert(11, Form.__createSituation(map, depth, width-1, maxWidth, maxDepth))
            sSituation.insert(12, Form.__createSituation(map, depth-1, width-1, maxWidth, maxDepth))
            sSituation.insert(13, Form.__createSituation(map, depth+1, width-1, maxWidth, maxDepth))
            sSituation.insert(14, Form.__createSituation(map, depth, width-2, maxWidth, maxDepth))
            sSituation.insert(15, Form.__createSituation(map, depth-1, width-2, maxWidth, maxDepth))
            sSituation.insert(16, Form.__createSituation(map, depth+1, width-2, maxWidth, maxDepth))
            sSituation.insert(17, Form.__createSituation(map, depth, width-3, maxWidth, maxDepth))
            sSituation.insert(18, Form.__createSituation(map, depth-1, width-3, maxWidth, maxDepth))
            sSituation.insert(19, Form.__createSituation(map, depth+1, width-3, maxWidth, maxDepth))
            sSituation.insert(20, Form.__createSituation(map, depth-2, width+3, maxWidth, maxDepth))
            sSituation.insert(21, Form.__createSituation(map, depth-2, width+2, maxWidth, maxDepth))
            sSituation.insert(22, Form.__createSituation(map, depth-2, width+1, maxWidth, maxDepth))
            sSituation.insert(23, Form.__createSituation(map, depth-2, width, maxWidth, maxDepth))
            sSituation.insert(24, Form.__createSituation(map, depth-2, width-1, maxWidth, maxDepth))
            sSituation.insert(25, Form.__createSituation(map, depth-2, width-2, maxWidth, maxDepth))
            sSituation.insert(26, Form.__createSituation(map, depth-2, width-3, maxWidth, maxDepth))
            sSituation.insert(27, Form.__createSituation(map, depth+2, width+3, maxWidth, maxDepth))
            sSituation.insert(28, Form.__createSituation(map, depth+2, width+2, maxWidth, maxDepth))
            sSituation.insert(29, Form.__createSituation(map, depth+2, width+1, maxWidth, maxDepth))
            sSituation.insert(30, Form.__createSituation(map, depth+2, width, maxWidth, maxDepth))
            sSituation.insert(31, Form.__createSituation(map, depth+2, width-1, maxWidth, maxDepth))
            sSituation.insert(32, Form.__createSituation(map, depth+2, width-2, maxWidth, maxDepth))
            sSituation.insert(33, Form.__createSituation(map, depth+2, width-3, maxWidth, maxDepth))
            sSituation.insert(34, Form.__createSituation(map, depth-3, width+3, maxWidth, maxDepth))
            sSituation.insert(35, Form.__createSituation(map, depth-3, width+2, maxWidth, maxDepth))
            sSituation.insert(36, Form.__createSituation(map, depth-3, width+1, maxWidth, maxDepth))
            sSituation.insert(37, Form.__createSituation(map, depth-3, width, maxWidth, maxDepth))
            sSituation.insert(38, Form.__createSituation(map, depth-3, width-1, maxWidth, maxDepth))
            sSituation.insert(39, Form.__createSituation(map, depth-3, width-2, maxWidth, maxDepth))
            sSituation.insert(40, Form.__createSituation(map, depth-3, width-3, maxWidth, maxDepth))
            sSituation.insert(41, Form.__createSituation(map, depth+3, width+3, maxWidth, maxDepth))
            sSituation.insert(42, Form.__createSituation(map, depth+3, width+2, maxWidth, maxDepth))
            sSituation.insert(43, Form.__createSituation(map, depth+3, width+1, maxWidth, maxDepth))
            sSituation.insert(44, Form.__createSituation(map, depth+3, width, maxWidth, maxDepth))
            sSituation.insert(45, Form.__createSituation(map, depth+3, width-1, maxWidth, maxDepth))
            sSituation.insert(46, Form.__createSituation(map, depth+3, width-2, maxWidth, maxDepth))
            sSituation.insert(47, Form.__createSituation(map, depth+3, width-3, maxWidth, maxDepth))
        elif now_way == WAY.LEFT:
            sSituation.insert(0, Form.__createSituation(map, depth+1, width, maxWidth, maxDepth))
            sSituation.insert(1, Form.__createSituation(map, depth+1, width-1, maxWidth, maxDepth))
            sSituation.insert(2, Form.__createSituation(map, depth, width-1, maxWidth, maxDepth))
            sSituation.insert(3, Form.__createSituation(map, depth-1, width-1, maxWidth, maxDepth))
            sSituation.insert(4, Form.__createSituation(map, depth-1, width, maxWidth, maxDepth))
            sSituation.insert(5, Form.__createSituation(map, depth, width-2, maxWidth, maxDepth))
            sSituation.insert(6, Form.__createSituation(map, depth+1, width-2, maxWidth, maxDepth))
            sSituation.insert(7, Form.__createSituation(map, depth-1, width-2, maxWidth, maxDepth))
            sSituation.insert(8, Form.__createSituation(map, depth, width-3, maxWidth, maxDepth))
            sSituation.insert(9, Form.__createSituation(map, depth+1, width-3, maxWidth, maxDepth))
            sSituation.insert(10, Form.__createSituation(map, depth-1, width-3, maxWidth, maxDepth))
            sSituation.insert(11, Form.__createSituation(map, depth, width+1, maxWidth, maxDepth))
            sSituation.insert(12, Form.__createSituation(map, depth+1, width+1, maxWidth, maxDepth))
            sSituation.insert(13, Form.__createSituation(map, depth-1, width+1, maxWidth, maxDepth))
            sSituation.insert(14, Form.__createSituation(map, depth, width+2, maxWidth, maxDepth))
            sSituation.insert(15, Form.__createSituation(map, depth+1, width+2, maxWidth, maxDepth))
            sSituation.insert(16, Form.__createSituation(map, depth-1, width+2, maxWidth, maxDepth))
            sSituation.insert(17, Form.__createSituation(map, depth, width+3, maxWidth, maxDepth))
            sSituation.insert(18, Form.__createSituation(map, depth+1, width+3, maxWidth, maxDepth))
            sSituation.insert(19, Form.__createSituation(map, depth-1, width+3, maxWidth, maxDepth))
            sSituation.insert(20, Form.__createSituation(map, depth+2, width-3, maxWidth, maxDepth))
            sSituation.insert(21, Form.__createSituation(map, depth+2, width-2, maxWidth, maxDepth))
            sSituation.insert(22, Form.__createSituation(map, depth+2, width-1, maxWidth, maxDepth))
            sSituation.insert(23, Form.__createSituation(map, depth+2, width, maxWidth, maxDepth))
            sSituation.insert(24, Form.__createSituation(map, depth+2, width+1, maxWidth, maxDepth))
            sSituation.insert(25, Form.__createSituation(map, depth+2, width+2, maxWidth, maxDepth))
            sSituation.insert(26, Form.__createSituation(map, depth+2, width+3, maxWidth, maxDepth))
            sSituation.insert(27, Form.__createSituation(map, depth-2, width-3, maxWidth, maxDepth))
            sSituation.insert(28, Form.__createSituation(map, depth-2, width-2, maxWidth, maxDepth))
            sSituation.insert(29, Form.__createSituation(map, depth-2, width-1, maxWidth, maxDepth))
            sSituation.insert(30, Form.__createSituation(map, depth-2, width, maxWidth, maxDepth))
            sSituation.insert(31, Form.__createSituation(map, depth-2, width+1, maxWidth, maxDepth))
            sSituation.insert(32, Form.__createSituation(map, depth-2, width+2, maxWidth, maxDepth))
            sSituation.insert(33, Form.__createSituation(map, depth-2, width+3, maxWidth, maxDepth))
            sSituation.insert(34, Form.__createSituation(map, depth+3, width-3, maxWidth, maxDepth))
            sSituation.insert(35, Form.__createSituation(map, depth+3, width-2, maxWidth, maxDepth))
            sSituation.insert(36, Form.__createSituation(map, depth+3, width-1, maxWidth, maxDepth))
            sSituation.insert(37, Form.__createSituation(map, depth+3, width, maxWidth, maxDepth))
            sSituation.insert(38, Form.__createSituation(map, depth+3, width+1, maxWidth, maxDepth))
            sSituation.insert(39, Form.__createSituation(map, depth+3, width+2, maxWidth, maxDepth))
            sSituation.insert(40, Form.__createSituation(map, depth+3, width+3, maxWidth, maxDepth))
            sSituation.insert(41, Form.__createSituation(map, depth-3, width-3, maxWidth, maxDepth))
            sSituation.insert(42, Form.__createSituation(map, depth-3, width-2, maxWidth, maxDepth))
            sSituation.insert(43, Form.__createSituation(map, depth-3, width-1, maxWidth, maxDepth))
            sSituation.insert(44, Form.__createSituation(map, depth-3, width, maxWidth, maxDepth))
            sSituation.insert(45, Form.__createSituation(map, depth-3, width+1, maxWidth, maxDepth))
            sSituation.insert(46, Form.__createSituation(map, depth-3, width+2, maxWidth, maxDepth))
            sSituation.insert(47, Form.__createSituation(map, depth-3, width+3, maxWidth, maxDepth))
        elif now_way == WAY.DOWN:
            sSituation.insert(0, Form.__createSituation(map, depth, width+1, maxWidth, maxDepth))
            sSituation.insert(1, Form.__createSituation(map, depth+1, width+1, maxWidth, maxDepth))
            sSituation.insert(2, Form.__createSituation(map, depth+1, width, maxWidth, maxDepth))
            sSituation.insert(3, Form.__createSituation(map, depth+1, width-1, maxWidth, maxDepth))
            sSituation.insert(4, Form.__createSituation(map, depth, width-1, maxWidth, maxDepth))
            sSituation.insert(5, Form.__createSituation(map, depth+2, width, maxWidth, maxDepth))
            sSituation.insert(6, Form.__createSituation(map, depth+2, width+1, maxWidth, maxDepth))
            sSituation.insert(7, Form.__createSituation(map, depth+2, width-1, maxWidth, maxDepth))
            sSituation.insert(8, Form.__createSituation(map, depth+3, width, maxWidth, maxDepth))
            sSituation.insert(9, Form.__createSituation(map, depth+3, width+1, maxWidth, maxDepth))
            sSituation.insert(10, Form.__createSituation(map, depth+3, width-1, maxWidth, maxDepth))
            sSituation.insert(11, Form.__createSituation(map, depth-1, width, maxWidth, maxDepth))
            sSituation.insert(12, Form.__createSituation(map, depth-1, width+1, maxWidth, maxDepth))
            sSituation.insert(13, Form.__createSituation(map, depth-1, width-1, maxWidth, maxDepth))
            sSituation.insert(14, Form.__createSituation(map, depth-2, width, maxWidth, maxDepth))
            sSituation.insert(15, Form.__createSituation(map, depth-2, width+1, maxWidth, maxDepth))
            sSituation.insert(16, Form.__createSituation(map, depth-2, width-1, maxWidth, maxDepth))
            sSituation.insert(17, Form.__createSituation(map, depth-3, width, maxWidth, maxDepth))
            sSituation.insert(18, Form.__createSituation(map, depth-3, width+1, maxWidth, maxDepth))
            sSituation.insert(19, Form.__createSituation(map, depth-3, width-1, maxWidth, maxDepth))
            sSituation.insert(20, Form.__createSituation(map, depth+3, width+2, maxWidth, maxDepth))
            sSituation.insert(21, Form.__createSituation(map, depth+2, width+2, maxWidth, maxDepth))
            sSituation.insert(22, Form.__createSituation(map, depth+1, width+2, maxWidth, maxDepth))
            sSituation.insert(23, Form.__createSituation(map, depth, width+2, maxWidth, maxDepth))
            sSituation.insert(24, Form.__createSituation(map, depth-1, width+2, maxWidth, maxDepth))
            sSituation.insert(25, Form.__createSituation(map, depth-2, width+2, maxWidth, maxDepth))
            sSituation.insert(26, Form.__createSituation(map, depth-3, width+2, maxWidth, maxDepth))
            sSituation.insert(27, Form.__createSituation(map, depth+3, width-2, maxWidth, maxDepth))
            sSituation.insert(28, Form.__createSituation(map, depth+2, width-2, maxWidth, maxDepth))
            sSituation.insert(29, Form.__createSituation(map, depth+1, width-2, maxWidth, maxDepth))
            sSituation.insert(30, Form.__createSituation(map, depth, width-2, maxWidth, maxDepth))
            sSituation.insert(31, Form.__createSituation(map, depth-1, width-2, maxWidth, maxDepth))
            sSituation.insert(32, Form.__createSituation(map, depth-2, width-2, maxWidth, maxDepth))
            sSituation.insert(33, Form.__createSituation(map, depth-3, width-2, maxWidth, maxDepth))
            sSituation.insert(34, Form.__createSituation(map, depth+3, width+3, maxWidth, maxDepth))
            sSituation.insert(35, Form.__createSituation(map, depth+2, width+3, maxWidth, maxDepth))
            sSituation.insert(36, Form.__createSituation(map, depth+1, width+3, maxWidth, maxDepth))
            sSituation.insert(37, Form.__createSituation(map, depth, width+3, maxWidth, maxDepth))
            sSituation.insert(38, Form.__createSituation(map, depth-1, width+3, maxWidth, maxDepth))
            sSituation.insert(39, Form.__createSituation(map, depth-2, width+3, maxWidth, maxDepth))
            sSituation.insert(40, Form.__createSituation(map, depth-3, width+3, maxWidth, maxDepth))
            sSituation.insert(41, Form.__createSituation(map, depth+3, width-3, maxWidth, maxDepth))
            sSituation.insert(42, Form.__createSituation(map, depth+2, width-3, maxWidth, maxDepth))
            sSituation.insert(43, Form.__createSituation(map, depth+1, width-3, maxWidth, maxDepth))
            sSituation.insert(44, Form.__createSituation(map, depth, width-3, maxWidth, maxDepth))
            sSituation.insert(45, Form.__createSituation(map, depth-1, width-3, maxWidth, maxDepth))
            sSituation.insert(46, Form.__createSituation(map, depth-2, width-3, maxWidth, maxDepth))
            sSituation.insert(47, Form.__createSituation(map, depth-3, width-3, maxWidth, maxDepth))
        return sSituation

    def __createSituation(map, depth, width, maxWidth, maxDepth):
        return [cmnDungeon.Common.isPosPath(map, depth, width, maxWidth, maxDepth), depth, width]
