import common.debug.debug as dbg


class Form:
    def __init__(self):
        self.__flag = False
        self.__count = 0
        self.__totalCount = 0

    def flagOn(self):
        if not (self.__flag):
            self.__flag = True
            return True
        else:
            dbg.ERROR_LOG("[ActionForm.flagOn]フラグの初期化処理不備")
            return False

    def flagOff(self):
        if self.__flag:
            self.__flag = False
            return True
        else:
            dbg.ERROR_LOG("[ActionForm.flagOff]フラグを設定していないのに初期化を実施")
            return False

    def FLAG(self):
        return self.__flag

    def countUp(self):
        if self.__count < 1000:
            self.__count = self.__count+1
        else:
            dbg.ERROR_LOG("[ActionForm.countUp]カウント限界に到達")

    def countTotal(self):
        if self.__totalCount < 0xFC18:
            self.__totalCount = self.__totalCount + self.__count
        elif self.__totalCount == 0xFFFF:
            dbg.ERROR_LOG("[ActionForm.countTotal]カウント限界に到達")
        else:
            if self.__count >= 1000:
                dbg.ERROR_LOG("[ActionForm.countTotal]通常起こりえないケース")
                self.__totalCount = 0xFFFF
            elif self.__count > (0xFFFF - self.__totalCount):
                self.__totalCount = 0xFFFF
            else:
                self.__totalCount = self.__totalCount + self.__count

    def countReset(self):
        self.__count = 0

    def COUNT(self):
        return self.__count

    def updateTotalCount(self, count: int):
        if 0 < count and count < 0xFFFF:
            self.__totalCount = count
        elif count == 0 or count < 0:
            self.__totalCount = count
        else:
            self.__totalCount = 0xFFFF

    def TOTAL_COUNT(self):
        return self.__totalCount
