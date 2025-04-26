import dataclasses
import pyd.status as STATUS
import common.debug.debug as dbg


@dataclasses.dataclass
class Form:
    __now_status: int
    __pre_status: int

    def __init__(self, init_status):
        self.__now_status = init_status
        self.__pre_status = init_status

    def update_status(self, status):
        if STATUS.existStatus(status):
            if self.__now_status != status:
                dbg.LOG("変更前ステータス:" + str(self.__now_status))
                dbg.LOG("変更後ステータス:" + str(status))
            self.__pre_status = self.__now_status
            self.__now_status = status
            return True
        else:
            dbg.ERROR_LOG("[StatusForm.update_status]存在しないステータスに更新しようとしています")
            return False

    @property
    def now_status(self):
        return self.__now_status

    @property
    def pre_status(self):
        return self.__pre_status
