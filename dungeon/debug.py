
import common.debug.debug as dbg
import common.common as cmn
import dungeon.data.map.map as map
import dungeon.pyd.way as WAY


class Debug:
    def showPos(form):
        if (not (form.existDiffPos())) and cmn.DEBUG_FLAG:
            dbg.LOG('=====POSITION START=====')
            dbg.LOG(str(form.PRE_POS()))
            dbg.LOG('↓↓↓↓↓↓↓↓↓')
            dbg.LOG(str(form.NOW_POS()))
            dbg.LOG('=====POSITION   END=====')

    def showWay(form):
        if (not (form.existDiffWay())) and cmn.DEBUG_FLAG:
            dbg.LOG('=====WAY START=====')
            errorFlag = Debug.__printWay(form.PRE_WAY())
            if errorFlag:
                dbg.ERROR_LOG('↓↓↓↓↓↓↓↓↓')
            else:
                dbg.LOG('↓↓↓↓↓↓↓↓↓')
            Debug.__printWay(form.NOW_WAY())
            dbg.LOG('=====WAY   END=====')

    def showView(form):
        if (not (form.existDiffView())) and cmn.DEBUG_FLAG:
            dbg.LOG('=====VIEW_STATUS START=====')
            Debug.__printStatus(form.PRE_VIEW())
            dbg.LOG('↓↓↓↓↓')
            Debug.__printStatus(form.NOW_VIEW())
            dbg.LOG('=====VIEW_STATUS   END=====')

    def showSituation(situation, errorFlg=False):
        if cmn.DEBUG_FLAG:
            test = []
            test.insert(0, Debug.__convertSituation(situation[0][0]))
            test.insert(1, Debug.__convertSituation(situation[1][0]))
            test.insert(2, Debug.__convertSituation(situation[2][0]))
            test.insert(3, Debug.__convertSituation(situation[3][0]))
            test.insert(4, Debug.__convertSituation(situation[4][0]))
            test.insert(5, Debug.__convertSituation(situation[5][0]))
            test.insert(6, Debug.__convertSituation(situation[6][0]))
            test.insert(7, Debug.__convertSituation(situation[7][0]))
            test.insert(8, Debug.__convertSituation(situation[8][0]))
            test.insert(9, Debug.__convertSituation(situation[9][0]))
            test.insert(10, Debug.__convertSituation(situation[10][0]))
            dbg.LOG('=====SITUATION START=====')
            if errorFlg:
                dbg.ERROR_LOG(test[9] + test[8] + test[10])
                dbg.ERROR_LOG(test[6] + test[5] + test[7])
                dbg.ERROR_LOG(test[1] + test[2] + test[3])
                dbg.ERROR_LOG(test[0] + "○" + test[4])
            else:
                dbg.LOG(test[9] + test[8] + test[10])
                dbg.LOG(test[6] + test[5] + test[7])
                dbg.LOG(test[1] + test[2] + test[3])
                dbg.LOG(test[0] + "○" + test[4])
            dbg.LOG('=====SITUATION   END=====')

    def __convertSituation(flag: int):
        if cmn.DEBUG_FLAG:
            if map.Judge.isNotWall(flag):
                return "□"
            else:
                return "■"

    def __printWay(now_way: int):
        if cmn.DEBUG_FLAG:
            if now_way == WAY.UP and cmn.DEBUG_FLAG:
                dbg.LOG('UP_WAY')
                return False
            elif now_way == WAY.RIGHT and cmn.DEBUG_FLAG:
                dbg.LOG('RIGHT_WAY')
                return False
            elif now_way == WAY.LEFT and cmn.DEBUG_FLAG:
                dbg.LOG('LEFT_WAY')
                return False
            elif now_way == WAY.DOWN and cmn.DEBUG_FLAG:
                dbg.LOG('DOWN_WAY')
                return False
            else:
                dbg.ERROR_LOG("存在しない方角方向:"+str(now_way))
                return True

    def __printStatus(now_status):
        if cmn.DEBUG_FLAG:
            dbg.LOG(hex(now_status))
