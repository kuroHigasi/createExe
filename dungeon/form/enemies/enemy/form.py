import dataclasses


@dataclasses.dataclass
class Form:
    _route: list
    _type: int
    _index: int
    _route_len: int
    _way: bool
    _appear_flag: bool

    def __init__(self, pos_list: list, enemy_type: int):
        self._route = pos_list
        self._type = enemy_type
        self._index = 0
        self._route_len = len(self._route)
        self._way = True
        self._appear_flag = True

    @property
    def appear_flag(self):
        return self._appear_flag

    @appear_flag.setter
    def appear_flag(self, appear_flag):
        if not appear_flag:
            self._appear_flag = appear_flag

    @property
    def type(self):
        return self._type

    def get_pos(self):
        return self._route[self._index]

    def move(self):
        if self._way:  # 加算
            if self._index+1 < self._route_len:
                self._index += 1
            else:
                self._way = False
                self._index -= 1
        else:  # 減算
            if self._index > 0:
                self._index -= 1
            else:
                self._index += 1
                self._way = True
