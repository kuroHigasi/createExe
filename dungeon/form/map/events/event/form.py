import dataclasses


@dataclasses.dataclass
class Form:
    __pos: any
    __way: int
    __text: str
    __type: int
    __flag: bool

    def __init__(self, pos, way, text, event_type):
        self.__pos = pos
        self.__way = way
        self.__text = text
        self.__type = event_type
        self.__flag = True

    @property
    def pos(self):
        return self.__pos

    @property
    def way(self):
        return self.__way

    @property
    def text(self):
        return self.__text

    @property
    def type(self):
        return self.__type

    @property
    def flag(self):
        return self.__flag

    @flag.setter
    def flag(self, flag: bool):
        self.__flag = flag
