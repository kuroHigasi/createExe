

class Form:
    def __init__(self, posList, type):
        self.__move = posList
        self.__type = type

    def MOVE(self):
        return self.__move

    def TYPE(self):
        return self.__type
