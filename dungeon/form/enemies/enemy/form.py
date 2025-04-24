import dataclasses


@dataclasses.dataclass
class Form:
    _move: list
    _type: int

    def __init__(self, pos_list, enemy_type):
        self._move = pos_list
        self._type = enemy_type

    @property
    def move(self):
        return self._move

    @property
    def type(self):
        return self._type
