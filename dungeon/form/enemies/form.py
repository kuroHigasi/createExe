import common.debug.debug as dbg


class Form:
    def __init__(self):
        self.__enemyCount = 0
        self.__enemyMove = []
        self.__enemyMoveIndex = []
        self.__enemyMoveDistance = []
        self.__enemyType = []
        self.__appearFlag = []
        self.__enemyWay = []

    def regist(self, enemyList):
        count: int = 0
        self.__enemyCount = 0
        self.__enemyMove = []
        self.__enemyMoveIndex = []
        self.__enemyMoveDistance = []
        self.__enemyType = []
        self.__appearFlag = []
        self.__enemyWay = []
        for enemy in enemyList:
            i: int = 0
            posList = []
            for pos in enemy.move:
                posList.insert(i, [pos[0], pos[1]])
                i += 1
            self.__enemyMove.insert(count, posList)
            self.__enemyType.insert(count, enemy.type)
            count += 1
        if count == 0:
            print(self.__enemyMove)
            dbg.ERROR_LOG("敵がいないMAP")
        self.__enemyCount = count
        for k in range(0, count, 1):
            self.__enemyMoveIndex.insert(k, 0)
            self.__enemyMoveDistance.insert(k, len(self.__enemyMove[k]))
            self.__appearFlag.insert(k, True)
            self.__enemyWay.insert(k, True)

    def disappearanceEnemy(self, index):
        self.__appearFlag[index] = False

    def APPEAR_FLAG(self, index):
        return self.__appearFlag[index]

    def ENEMY_COUNT(self):
        return self.__enemyCount

    def ENEMY_POS(self, index):
        return self.__enemyMove[index][self.__enemyMoveIndex[index]]

    def ENEMY_TYPE(self, index):
        return self.__enemyType[index]

    def enemyMove(self):
        for i in range(0, self.__enemyCount, 1):
            if self.__enemyWay[i]:  # 加算
                if self.__enemyMoveIndex[i]+1 < self.__enemyMoveDistance[i]:
                    self.__enemyMoveIndex[i] += 1
                else:
                    self.__enemyWay[i] = False
                    self.__enemyMoveIndex[i] -= 1
            else:  # 減算
                if self.__enemyMoveIndex[i]-1 >= 0:
                    self.__enemyMoveIndex[i] -= 1
                else:
                    self.__enemyMoveIndex[i] += 1
                    self.__enemyWay[i] = True
