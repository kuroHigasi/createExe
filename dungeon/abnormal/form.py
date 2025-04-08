import pyd.calc as calc


class Form:
    def __init__(self):
        self.__status = 0b0000

    def recover(self):
        self.__status = 0b0000

    def death(self):
        self.__status = calc.bitmask(self.__status, 0b0001)

    def IS_DEATH(self):
        return (calc.maskAndRight(self.__status, 0b0001, 0) == 0b0001)
