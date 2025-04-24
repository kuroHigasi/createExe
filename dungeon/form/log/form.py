import dataclasses


@dataclasses.dataclass
class Form:
    __log: list
    __maxNum: int
    __index: int
    __flag: bool

    def __init__(self):
        self.__log = []
        self.__maxNum = 10
        self.__index = 0
        self.__flag = False

    def add_log(self, log):
        if log != "":
            self.__log.insert(0, log)
            self.__index += 1
            if self.__index > self.__maxNum:
                del self.__log[self.__index-1]
                self.__index -= 1

    def flag_off(self):
        self.__flag = False

    def flag_on(self):
        self.__flag = True

    def get_flag(self):
        return self.__flag

    def reset(self):
        self.__log = []
        self.__index = 0

    def get_log(self):
        return self.__log

    def get_log_num(self):
        return self.__index
