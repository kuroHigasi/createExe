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
        self.__mapForm = MapForm.Form(floor)
        self.__buttonForm = ButtonForm.Form()
        self.__actionForm = ActionForm.Form()
        self.__abnormalForm = AbnormalForm.Form()
        self.__logForm = LogForm.Form()
        self.__boxForm = BoxForm.Form()
        self.__imgList = DungeonImg.Download.dungeonImag()
        self.__eventFont = pygame.font.Font(cmn.resource_path(cPass.getFontPass("DotGothic16-Regular.ttf")), 16)
        self.__itemFont = pygame.font.Font(cmn.resource_path(cPass.getFontPass("DotGothic16-Regular.ttf")), 16)
        self.__endFlag = False

    def reset(self, floor: int):
        if floor > len(MapForm.dungeon):
            self.__actionForm.countTotal()
            self.__actionForm.countReset()
            self.__abnormalForm.recover()
            self.__logForm.resetLog()
            if self.__actionForm.FLAG() is True:
                self.__actionForm.flagOff()
            dbg.LOG("最上階へ到達しました")
            return True
        else:
            self.__mapForm.reset(floor)
            self.__actionForm.countTotal()
            self.__actionForm.countReset()
            self.__abnormalForm.recover()
            self.__logForm.resetLog()
            if self.__actionForm.FLAG() is True:
                self.__actionForm.flagOff()
            return False

    def updateWay(self, opeForm):
        now_way = self.__mapForm.NOW_WAY()
        next_way = now_way
        if now_way == WAY.UP:
            if opeForm.get_up():
                next_way = WAY.UP
            elif opeForm.get_left():
                next_way = WAY.LEFT
            elif opeForm.get_right():
                next_way = WAY.RIGHT
            elif opeForm.get_down():
                next_way = WAY.DOWN
        if now_way == WAY.RIGHT:
            if opeForm.get_up():
                next_way = WAY.RIGHT
            elif opeForm.get_left():
                next_way = WAY.UP
            elif opeForm.get_right():
                next_way = WAY.DOWN
            elif opeForm.get_down():
                next_way = WAY.LEFT
        if now_way == WAY.LEFT:
            if opeForm.get_up():
                next_way = WAY.LEFT
            elif opeForm.get_left():
                next_way = WAY.DOWN
            elif opeForm.get_right():
                next_way = WAY.UP
            elif opeForm.get_down():
                next_way = WAY.RIGHT
        if now_way == WAY.DOWN:
            if opeForm.get_up():
                next_way = WAY.DOWN
            elif opeForm.get_left():
                next_way = WAY.RIGHT
            elif opeForm.get_right():
                next_way = WAY.LEFT
            elif opeForm.get_down():
                next_way = WAY.UP
        self.__mapForm.updateWay(next_way)

    def go(self):
        judDepth = self.__mapForm.NOW_POS()[0]
        judWidth = self.__mapForm.NOW_POS()[1]
        nowWay = self.__mapForm.NOW_WAY()
        map = self.__mapForm.MAP()
        maxWidth = self.__mapForm.MAX_WIDTH()
        maxDepth = self.__mapForm.MAX_DEPTH()
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
        self.__mapForm.updatePos(nextPos)

    def updateView(self):
        self.__mapForm.updateView()

    def updateSituation(self):
        self.__mapForm.updateSituation()

    def enemyMove(self):
        if self.__actionForm.FLAG():
            self.__mapForm.enemyMove()

    def FLOOR(self):
        return self.__mapForm.FLOOR()

    def NOW_WAY(self):
        return self.__mapForm.NOW_WAY()

    def NOW_POS(self):
        return self.__mapForm.NOW_POS()

    def NOW_VIEW(self):
        return self.__mapForm.NOW_VIEW()

    def PRE_WAY(self):
        return self.__mapForm.PRE_WAY()

    def PRE_POS(self):
        return self.__mapForm.PRE_POS()

    def PRE_VIEW(self):
        return self.__mapForm.PRE_VIEW()

    def SITUATION(self):
        return self.__mapForm.SITUATION()

    def MAP(self):
        return self.__mapForm.MAP()

    def START_POS(self):
        return self.__mapForm.START_POS()

    def GOAL_POS(self):
        return self.__mapForm.GOAL_POS()

    def createAngle(self):
        nowPos = self.__mapForm.NOW_POS()
        goalPos = self.__mapForm.GOAL_POS()
        nowWay = self.__mapForm.NOW_WAY()
        compassAngle = 0
        if nowPos[1] == goalPos[1]:
            if nowPos[0] < goalPos[0]:
                compassAngle = Form.__compassWay(180, nowWay)
            elif nowPos[0] > goalPos[0]:
                compassAngle = Form.__compassWay(0, nowWay)
            else:
                compassAngle = Form.__compassWay(90, nowWay)
        elif nowPos[1] > goalPos[1]:
            if nowPos[0] < goalPos[0]:
                angel = math.degrees(math.atan((goalPos[1] - nowPos[1])) / (goalPos[0] - nowPos[0]))
                compassAngle = Form.__compassWay(angel + 180, nowWay)
            elif nowPos[0] > goalPos[0]:
                angel = math.degrees(math.atan((goalPos[1] - nowPos[1]) / (goalPos[0] - nowPos[0])))
                compassAngle = Form.__compassWay(angel, nowWay)
            else:
                compassAngle = Form.__compassWay(90, nowWay)
        elif nowPos[1] < goalPos[1]:
            if nowPos[0] < goalPos[0]:
                angel = math.degrees(math.atan((goalPos[1] - nowPos[1]) / (goalPos[0] - nowPos[0])))
                compassAngle = Form.__compassWay(angel + 180, nowWay)
            elif nowPos[0] > goalPos[0]:
                angel = math.degrees(math.atan((goalPos[1] - nowPos[1]) / (nowPos[0] - goalPos[0])))
                compassAngle = Form.__compassWay(-angel, nowWay)
            else:
                compassAngle = Form.__compassWay(270, nowWay)
        return compassAngle

    def __compassWay(compassWay, nowWay):
        addWay = 0
        if WAY.UP == nowWay:
            addWay = 0
        elif WAY.RIGHT == nowWay:
            addWay = 90
        elif WAY.LEFT == nowWay:
            addWay = 270
        else:
            addWay = 180
        return compassWay + addWay + random.randint(-2, 2)

    def MAX_WIDTH(self):
        return self.__mapForm.MAX_WIDTH()

    def MAX_DEPTH(self):
        return self.__mapForm.MAX_DEPTH()

    # [ENEMY] START
    def disappearanceEnemy(self, index):
        return self.__mapForm.disappearanceEnemy(index)

    def ENEMY_COUNT(self):
        return self.__mapForm.ENEMY_COUNT()

    def APPEAR_FLAG(self, index):
        return self.__mapForm.APPEAR_FLAG(index)

    def ENEMIS_TYPE(self, index):
        return self.__mapForm.ENEMY_TYPE(index)

    def ENEMIS_POS(self, index):
        return self.__mapForm.ENEMY_POS(index)
    # [ENEMY] END

    def eventFlagOff(self):
        self.__mapForm.eventFlagOff()

    def getEventText(self):
        return Form.__getEventText(self.__mapForm)

    # [ITEM] START
    def searchItem(self):
        self.__mapForm.getItem()

    def watchBox(self, num):
        return self.__boxForm.watch(num)

    def itemIntoBox(self):
        return self.__boxForm.set(self.__mapForm.getItem())

    def itemSetBox(self, item):
        return self.__boxForm.set(item)

    def ITEM(self):
        return self.__mapForm.getItem()

    def ITEM_GET_FLAG(self):
        return self.__mapForm.ITEM_GET_FLAG()

    def itemFlagOff(self):
        return self.__mapForm.itemFlagOff()

    def itemBoxPreUpdate(self):
        return self.__boxForm.updatePre()

    def itemBoxReset(self):
        return self.__boxForm.reset()

    def itemBoxClear(self):
        return self.__boxForm.clear()

    def itemBoxUse(self, index):
        return self.__boxForm.useItem(index)

    def itemBoxButtonUpdate(self, index, x, y):
        return self.__boxForm.updateBoxButton(index, x, y)

    def BOX_BUTTON(self, index):
        return self.__boxForm.BOX_BUTTON(index)

    def itemBoxUseFlag(self, index):
        return self.__boxForm.BOX_USE_FLAG(index)

    def itemBoxDispIndex(self, index):
        if self.__boxForm.BOX_USE_FLAG(index):
            return 1
        return 0

    def itemBoxPickUp(self, index):
        return self.__boxForm.pickUp(index)

    def itemBoxUseTurnCount(self):
        return self.__boxForm.useItemTurnCountup()

    def itemBoxFlagOn(self):
        self.__boxForm.flagOn()

    def BOX_FLAG(self):
        self.__boxForm.FLAG()
    # [ITEM] END

    def IMG_LIST(self):
        return self.__imgList

    # [ACTION FORM] START
    def actionFlagOn(self):
        self.__actionForm.flagOn()

    def actionFlagOff(self):
        if self.__actionForm.flagOff():
            self.__actionForm.countUp()

    def ACTION_FLAG(self):
        return self.__actionForm.FLAG()

    def COUNT(self):
        return self.__actionForm.COUNT()

    def updateTotalCount(self, count: int):
        return self.__actionForm.updateTotalCount(count)

    def TOTAL_COUNT(self):
        return self.__actionForm.TOTAL_COUNT()
    # [ACTION FORM] END

    def existDiffWay(self):
        return self.__mapForm.existDiffWay()

    def existDiffPos(self):
        return self.__mapForm.existDiffPos()

    def existDiffView(self):
        return self.__mapForm.existDiffView()

    # [SYSTEM BUTTON] START
    def updateConfigButton(self, x, y):
        self.__buttonForm.updateConfigButton(x, y, 150, 60)

    def resetConfigButton(self):
        self.__buttonForm.resetConfigButton()

    def CONFIG_BUTTON(self):
        return self.__buttonForm.CONFIG_BUTTON()

    def updateHomeButton(self, x, y):
        self.__buttonForm.updateHomeButton(x, y, 150, 60)

    def resetHomeButton(self):
        self.__buttonForm.resetHomeButton()

    def HOME_BUTTON(self):
        return self.__buttonForm.HOME_BUTTON()

    def updateExitButton(self, x, y):
        self.__buttonForm.updateExitButton(x, y, 150, 60)

    def EXIT_BUTTON(self):
        return self.__buttonForm.EXIT_BUTTON()

    def updateConfigButton(self, x, y):
        self.__buttonForm.updateConfigButton(x, y, 150, 60)

    def resetConfigButton(self):
        self.__buttonForm.resetConfigButton()

    def CONFIG_BUTTON(self):
        return self.__buttonForm.CONFIG_BUTTON()
    # [SYSTEM BUTTON] END

    # [ACTION BUTTON] START
    def updateRetryButton(self, x, y):
        self.__buttonForm.updateRetryButton(x, y, 150, 60)

    def RETRY_BUTTON(self):
        return self.__buttonForm.RETRY_BUTTON()

    def updateSaveButton(self, x, y):
        self.__buttonForm.updateSaveButton(x, y, 150, 60)

    def SAVE_BUTTON(self):
        return self.__buttonForm.SAVE_BUTTON()

    def updateActionButton(self, actIndex, x, y):
        self.__buttonForm.updateActionButton(actIndex, x, y, 150, 60)

    def resetActionButton(self, actIndex):
        self.__buttonForm.resetActionButton(actIndex)

    def ACTION_BUTTON(self, actIndex):
        return self.__buttonForm.ACTION_BUTTON(actIndex)
    # [ACTION BUTTON] END

    # ゲーム終了 処理
    def death(self):
        return self.__abnormalForm.death()

    def IS_DEATH(self):
        return self.__abnormalForm.IS_DEATH()

    def offEndFlag(self):
        self.__endFlag = False

    def onEndFlag(self):
        dbg.LOG("ゲーム クリア!")
        self.__endFlag = True

    def END_FLAG(self):
        return self.__endFlag

    # [LOG] START
    def resetLog(self):
        self.__logForm.resetLog()

    def updateLog(self):
        (text, type) = Form.__getEventText(self.__mapForm)
        if ("" != text):
            self.__logForm.addLog(type + text)

    def LOG(self):
        return self.__logForm.LOG()

    def logFlagOff(self):
        self.__logForm.logFlagOff()

    def logFlagOn(self):
        self.__logForm.logFlagOn()

    def UPDATE_LOG_FLAG(self):
        return self.__logForm.UPDATE_LOG_FLAG()

    def LOG_NUM(self):
        return self.__logForm.LOG_NUM()
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
    def CREATE_INPUTDATA(self):
        data0 = str(self.__mapForm.FLOOR())
        data1 = str(self.__actionForm.TOTAL_COUNT())
        data2 = str(self.__boxForm.PRE_NUM())
        (item0, itemNum0) = self.__boxForm.preWatch(0)
        data3 = str(item0) + "," + str(itemNum0)
        (item1, itemNum1) = self.__boxForm.preWatch(1)
        data4 = str(item1) + "," + str(itemNum1)
        (item2, itemNum2) = self.__boxForm.preWatch(2)
        data5 = str(item2) + "," + str(itemNum2)
        return data0 + "," + data1 + "," + data2 + "," + data3 + "," + data4 + "," + data5

    def __getEventText(mapForm):
        return mapForm.getEventText()
    # [SAVE/LOAD] END
