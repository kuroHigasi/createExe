import dungeon.form.form as dungeon_form
import common.debug.debug as dbg
import common.common as cmn
import dungeon.data.map.map as dungeon_map
import pyd.way as WAY


class Debug:
    @staticmethod
    def show_position(form: dungeon_form.Form):
        if (not (form.existDiffPos())) and cmn.DEBUG_FLAG:
            dbg.LOG('=====POSITION START=====')
            dbg.LOG(str(form.debug_pre_pos()))
            dbg.LOG('↓↓↓↓↓↓↓↓↓')
            dbg.LOG(str(form.debug_now_pos()))
            dbg.LOG('=====POSITION   END=====')

    @staticmethod
    def show_way(form: dungeon_form.Form):
        if (not (form.existDiffWay())) and cmn.DEBUG_FLAG:
            dbg.LOG('=====WAY START=====')
            if Debug.__print_way(form.debug_pre_way()):
                dbg.ERROR_LOG('↓↓↓↓↓↓↓↓↓')
            else:
                dbg.LOG('↓↓↓↓↓↓↓↓↓')
            Debug.__print_way(form.debug_now_way())
            dbg.LOG('=====WAY   END=====')

    @staticmethod
    def show_view(form: dungeon_form.Form):
        if (not (form.existDiffView())) and cmn.DEBUG_FLAG:
            dbg.LOG('=====VIEW_STATUS START=====')
            Debug.__print_status(form.debug_pre_view())
            dbg.LOG('↓↓↓↓↓')
            Debug.__print_status(form.debug_now_view())
            dbg.LOG('=====VIEW_STATUS   END=====')

    @staticmethod
    def show_situation(form=None, get_situation=None, error_flag=False):
        if get_situation is None:
            if form is None:
                dbg.ERROR_LOG("[dungeon_debug]show_situation 引数不備")
                return
            else:
                temp_situation = form.get_situation()
        else:
            temp_situation = get_situation
        if cmn.DEBUG_FLAG:
            test = []
            test.insert(0, Debug.__convert_situation(temp_situation[0][0]))
            test.insert(1, Debug.__convert_situation(temp_situation[1][0]))
            test.insert(2, Debug.__convert_situation(temp_situation[2][0]))
            test.insert(3, Debug.__convert_situation(temp_situation[3][0]))
            test.insert(4, Debug.__convert_situation(temp_situation[4][0]))
            test.insert(5, Debug.__convert_situation(temp_situation[5][0]))
            test.insert(6, Debug.__convert_situation(temp_situation[6][0]))
            test.insert(7, Debug.__convert_situation(temp_situation[7][0]))
            test.insert(8, Debug.__convert_situation(temp_situation[8][0]))
            test.insert(9, Debug.__convert_situation(temp_situation[9][0]))
            test.insert(10, Debug.__convert_situation(temp_situation[10][0]))
            dbg.LOG('=====SITUATION START=====')
            if error_flag:
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

    @staticmethod
    def __convert_situation(pos_flag: int):
        if cmn.DEBUG_FLAG:
            if dungeon_map.Judge.isNotWall(pos_flag):
                return "□"
            else:
                return "■"

    @staticmethod
    def __print_way(now_way: int):
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

    @staticmethod
    def __print_status(now_status):
        if cmn.DEBUG_FLAG:
            dbg.LOG(hex(now_status))
