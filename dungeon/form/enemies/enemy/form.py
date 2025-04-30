import dataclasses


@dataclasses.dataclass
class Form:
    _route: list
    _type: int
    _index: int

    def __init__(self, pos_list, enemy_type):
        self._route = pos_list
        self._type = enemy_type
        self._index = 0
        self._max_num = len(self._route)

    @property
    def route(self):
        return self._route

    @property
    def type(self):
        return self._type
