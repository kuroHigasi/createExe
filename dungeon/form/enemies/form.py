import copy
import dataclasses
import dungeon.form.enemies.enemy.form as enemy_form
import common.debug.debug as dbg


@dataclasses.dataclass
class Form:
    __enemy_count: int
    __enemy_list: list

    def __init__(self):
        self.__enemy_count = 0
        self.__enemy_list = []

    def registry(self, enemy_list: list):
        self.__enemy_count = len(enemy_list)
        self.__enemy_list = copy.deepcopy(enemy_list)

    def disappearanceEnemy(self, index):
        self.__enemy_list[index].appear_flag = False

    def APPEAR_FLAG(self, index):
        return self.__enemy_list[index].appear_flag

    @property
    def enemy_count(self):
        return self.__enemy_count

    def get_enemy_pos(self, index):
        return self.__enemy_list[index].get_pos()

    def ENEMY_TYPE(self, index):
        return self.__enemy_list[index].type

    def enemy_move(self):
        for i in range(0, self.__enemy_count, 1):
            self.__enemy_list[i].move()
