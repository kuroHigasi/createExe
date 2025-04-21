import dataclasses


@dataclasses.dataclass
class Form:
    __pos: any
    __type: int

    def __init__(self, pos, item_type):
        self.__pos = pos
        self.__type = item_type

    @property
    def pos(self):
        return self.__pos

    @property
    def type(self):
        return self.__type
