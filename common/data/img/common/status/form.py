import common.pyd.status as STATUS
import common.debug.debug as dbg


class Form:
    def __init__(self, init_status):
        self.__nowStatus = init_status
        self.__preStatus = init_status

    def updateStatus(self, status):
        if STATUS.existStatus(status):
            if not (self.__nowStatus == status):
                dbg.LOG("変更前ステータス:" + str(self.__nowStatus))
                dbg.LOG("変更後ステータス:" + str(status))
            self.__preStatus = self.__nowStatus
            self.__nowStatus = status
            return True
        else:
            dbg.ERROR_LOG("[StatusForm.updateStatus]存在しないステータスに更新しようとしています")
            return False

    def NOW_STATUS(self):
        return self.__nowStatus

    def PRE_STATUS(self):
        return self.__preStatus

    def diffStatus(self):
        return not (self.__nowStatus == self.__preStatus)
