import dataclasses

import common.debug.debug as dbg


@dataclasses.dataclass
class Form:
    __enemy_count: int
    __enemy_move: list
    __enemy_move_index: list
    __enemy_move_distance: list
    __enemy_type: list
    __appear_flag: list
    __enemy_way: list

    def __init__(self):
        self.__enemy_count = 0
        self.__enemy_move = []
        self.__enemy_move_index = []
        self.__enemy_move_distance = []
        self.__enemy_type = []
        self.__appear_flag = []
        self.__enemy_way = []

    def registry(self, enemy_list):
        count: int = 0
        self.__enemy_count = 0
        self.__enemy_move = []
        self.__enemy_move_index = []
        self.__enemy_move_distance = []
        self.__enemy_type = []
        self.__appear_flag = []
        self.__enemy_way = []
        for enemy in enemy_list:
            i: int = 0
            pos_list = []
            for pos in enemy.route:
                pos_list.insert(i, [pos[0], pos[1]])
                i += 1
            self.__enemy_move.insert(count, pos_list)
            self.__enemy_type.insert(count, enemy.type)
            count += 1
        if count == 0:
            print(self.__enemy_move)
            dbg.ERROR_LOG("敵がいないMAP")
        self.__enemy_count = count
        for k in range(0, count, 1):
            self.__enemy_move_index.insert(k, 0)
            self.__enemy_move_distance.insert(k, len(self.__enemy_move[k]))
            self.__appear_flag.insert(k, True)
            self.__enemy_way.insert(k, True)

    def disappearanceEnemy(self, index):
        self.__appear_flag[index] = False

    def APPEAR_FLAG(self, index):
        return self.__appear_flag[index]

    @property
    def enemy_count(self):
        return self.__enemy_count

    def ENEMY_POS(self, index):
        return self.__enemy_move[index][self.__enemy_move_index[index]]

    def ENEMY_TYPE(self, index):
        return self.__enemy_type[index]

    def enemyMove(self):
        for i in range(0, self.__enemy_count, 1):
            if self.__enemy_way[i]:  # 加算
                if self.__enemy_move_index[i]+1 < self.__enemy_move_distance[i]:
                    self.__enemy_move_index[i] += 1
                else:
                    self.__enemy_way[i] = False
                    self.__enemy_move_index[i] -= 1
            else:  # 減算
                if self.__enemy_move_index[i]-1 >= 0:
                    self.__enemy_move_index[i] -= 1
                else:
                    self.__enemy_move_index[i] += 1
                    self.__enemy_way[i] = True
