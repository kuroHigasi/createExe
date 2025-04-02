

class Form:
    def __init__(self, pos, way, text, type):
        self.__pos = pos
        self.__way = way
        self.__text = text
        self.__type = type

    def POS(self):
        return self.__pos

    def WAY(self):
        return self.__way

    def TEXT(self):
        return self.__text

    def TYPE(self):
        return self.__type
