class Form:
    def __init__(self):
        self.__log = []
        self.__maxNum = 10
        self.__index = 0
        self.__flag = False

    def addLog(self, log):
        if (log != ""):
            self.__log.insert(0, log)
            self.__index += 1
            if self.__index > self.__maxNum:
                del self.__log[self.__index-1]
                self.__index -= 1

    def logFlagOff(self):
        self.__flag = False

    def logFlagOn(self):
        self.__flag = True

    def UPDATE_LOG_FLAG(self):
        return self.__flag

    def resetLog(self):
        self.__log = []
        self.__index = 0

    def LOG(self):
        return self.__log

    def LOG_NUM(self):
        return self.__index
