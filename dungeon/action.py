import common.common as cmn
import common.debug.debug as dbg
import pyd.typeAction as ACTION
import pyd.typeEnemy as ENEMY_TYPE


class Action:
    @staticmethod
    def go(DungeonForm, opeForm, configForm):
        isDeath = DungeonForm.IS_DEATH()
        goKeyType = configForm.get_go_key_type()
        if not (isDeath):  # 死亡時は行動しない
            if (opeForm.get_space() and goKeyType == 0) or (opeForm.get_enter() and goKeyType == 1):
                opeForm.space_off()  # 処理が連続で判定されないように実施
                opeForm.enter_off()  # 処理が連続で判定されないように実施
                # 更新(前進時)
                DungeonForm.go()
                if not (DungeonForm.existDiffPos()) and not (DungeonForm.ACTION_FLAG()):
                    DungeonForm.actionFlagOn()
                elif not (DungeonForm.existDiffPos()) and DungeonForm.ACTION_FLAG():
                    dbg.ERROR_LOG("[action.go]想定外の遷移")
            elif (opeForm.get_space() and goKeyType == 1) or (opeForm.get_enter() and goKeyType == 0):
                opeForm.space_off()  # 処理が連続で判定されないように実施
                opeForm.enter_off()  # 処理が連続で判定されないように実施
                if not (DungeonForm.ACTION_FLAG()):
                    DungeonForm.actionFlagOn()
            else:
                if DungeonForm.ACTION_FLAG():
                    DungeonForm.actionFlagOff()
            # 更新(毎ターン)
            DungeonForm.updateWay(opeForm)
            DungeonForm.updateSituation()
            DungeonForm.updateView()

    def updateFlag(DungeonForm):
        diffWayFlag = not (DungeonForm.existDiffWay())
        diffPosFlag = not (DungeonForm.existDiffPos())
        diffViewFlag = not (DungeonForm.existDiffView())
        logFlag = DungeonForm.UPDATE_LOG_FLAG()
        boxFlag = DungeonForm.BOX_FLAG()
        actFlag = DungeonForm.ACTION_FLAG()
        nowPos = DungeonForm.NOW_POS()
        startPos = DungeonForm.START_POS()
        if (diffWayFlag or diffPosFlag or diffViewFlag) and actFlag:
            if not (logFlag):
                DungeonForm.logFlagOn()
            if not (boxFlag):
                DungeonForm.itemBoxFlagOn()
        elif diffWayFlag:
            if not (logFlag):
                DungeonForm.logFlagOn()
        elif actFlag:
            if not (logFlag):
                DungeonForm.logFlagOn()
            if not (boxFlag):
                DungeonForm.itemBoxFlagOn()
        elif startPos[0] == nowPos[0] and startPos[1] == nowPos[1]:
            if not (logFlag):
                DungeonForm.logFlagOn()

    def enemyAction(DungeonForm):
        nowPos = DungeonForm.NOW_POS()
        prePos = DungeonForm.PRE_POS()
        preEnemyPos = []
        for index in range(0, DungeonForm.ENEMY_COUNT(), 1):
            preEnemyPos.insert(index, DungeonForm.ENEMIS_POS(index))
        DungeonForm.enemyMove()
        for index in range(0, DungeonForm.ENEMY_COUNT(), 1):
            enemyPos = DungeonForm.ENEMIS_POS(index)
            atackJudge1 = (enemyPos[0] == nowPos[0] and enemyPos[1] == nowPos[1])
            enemyAtackJudge = (enemyPos[0] == prePos[0] and enemyPos[1] == prePos[1])
            preEnemyAtackjudge = (preEnemyPos[index][0] == nowPos[0] and preEnemyPos[index][1] == nowPos[1])
            if atackJudge1 or (enemyAtackJudge and preEnemyAtackjudge):
                enemyType = DungeonForm.ENEMIS_TYPE(index)
                DungeonForm.disappearanceEnemy(index)
                if enemyType == ENEMY_TYPE.DANGER():
                    DungeonForm.death()
                else:
                    dbg.ERROR_LOG("[action.enemyAction]存在しないENEMY_TYPE")

    def actionButton(DungeonForm, opeForm):
        floor = DungeonForm.FLOOR()
        (x, y) = opeForm.get_mouse()
        (clickX, clickY) = opeForm.left_click_move_mouse()
        (actX, actY, actSizeW, actSizeH) = DungeonForm.ACTION_BUTTON(ACTION.GO_UP_THE_STAIRS())
        (searchX, searchY, searchSizeW, searchSizeH) = DungeonForm.ACTION_BUTTON(ACTION.SEARCH())
        # NEXT FLOOR
        if not (actX == -1 and actY == -1):
            if cmn.Judge.click(actX, actY, actSizeW, actSizeH, x, y, clickX, clickY, opeForm.is_left_click()):
                if DungeonForm.reset(floor+1):
                    DungeonForm.reset(1)
                    DungeonForm.onEndFlag()
                else:
                    DungeonForm.itemBoxPreUpdate()
                DungeonForm.resetActionButton(ACTION.GO_UP_THE_STAIRS())
        # SEARCH
        if not (searchX == -1 and searchY == -1):
            if cmn.Judge.click(searchX, searchY, searchSizeW, searchSizeH, x, y, clickX, clickY, opeForm.is_left_click()):
                if DungeonForm.ITEM_GET_FLAG():
                    if DungeonForm.itemIntoBox():
                        DungeonForm.itemFlagOff()
                        DungeonForm.eventFlagOff()
                DungeonForm.resetActionButton(ACTION.SEARCH())

    def retryButton(DungeonForm, opeForm):
        if DungeonForm.IS_DEATH():
            floor = DungeonForm.FLOOR()
            (x, y) = opeForm.get_mouse()
            (clickX, clickY) = opeForm.left_click_move_mouse()
            (retryX, retryY, retrySizeW, retrySizeH) = DungeonForm.RETRY_BUTTON()
            if cmn.Judge.click(retryX, retryY, retrySizeW, retrySizeH, x, y, clickX, clickY, opeForm.is_left_click()):
                DungeonForm.reset(floor)
                DungeonForm.resetActionButton(ACTION.GO_UP_THE_STAIRS())

    def useItemBox(dungeonForm, opeForm):
        (x, y) = opeForm.get_mouse()
        (clickX, clickY) = opeForm.left_click_move_mouse()
        (box0X, box0y, box0SizeW, box0SizeH) = dungeonForm.BOX_BUTTON(0)
        (box1X, box1y, box1SizeW, box1SizeH) = dungeonForm.BOX_BUTTON(1)
        (box2X, box2y, box2SizeW, box2SizeH) = dungeonForm.BOX_BUTTON(2)
        dungeonForm.itemBoxUseTurnCount()
        # BOX USE
        if not (box0X == -1 and box0y == -1):
            if cmn.Judge.click(box0X, box0y, box0SizeW, box0SizeH, x, y, clickX, clickY, opeForm.is_left_click()):
                dungeonForm.itemBoxUse(0)
        if not (box1X == -1 and box1y == -1):
            if cmn.Judge.click(box1X, box1y, box1SizeW, box1SizeH, x, y, clickX, clickY, opeForm.is_left_click()):
                dungeonForm.itemBoxUse(1)
        if not (box2X == -1 and box2y == -1):
            if cmn.Judge.click(box2X, box2y, box2SizeW, box2SizeH, x, y, clickX, clickY, opeForm.is_left_click()):
                dungeonForm.itemBoxUse(2)
