import dungeon.pyd.itemType as ITEM_TYPE


class Form:
    def __init__(self):
        self.__preBox = [ITEM_TYPE.RADER(), -1, -1]
        self.__preBoxNum = [1, 0, 0]
        self.__preNum = 1
        self.__box = [ITEM_TYPE.RADER(), -1, -1]
        self.__boxNum = [1, 0, 0]
        self.__boxButton = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
        self.__boxUseFlag = [True, False, False]
        self.__boxUseTurn = [-2, -1, -1]
        self.__flag = False
        self.__max = 3
        self.__num = 1

    def reset(self):
        self.__box = [self.__preBox[0], self.__preBox[1], self.__preBox[2]]
        self.__boxNum = [self.__preBoxNum[0], self.__preBoxNum[1], self.__preBoxNum[2]]
        self.__num = self.__preNum
        self.__boxButton = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
        self.__boxUseFlag = [True, False, False]
        self.__boxUseTurn = [-2, -1, -1]

    def clear(self):
        self.__preBox = [ITEM_TYPE.RADER(), -1, -1]
        self.__preBoxNum = [1, 0, 0]
        self.__preNum = 1
        self.__box = [ITEM_TYPE.RADER(), -1, -1]
        self.__boxNum = [1, 0, 0]
        self.__num = 1
        self.__boxButton = [[-1, -1, -1, -1], [-1, -1, -1, -1], [-1, -1, -1, -1]]
        self.__boxUseFlag = [True, False, False]
        self.__boxUseTurn = [-2, -1, -1]

    def set(self, item):
        flag = False
        itemIndex = -1
        if (self.__num < self.__max):
            # 同じアイテム存在チェック
            for index in (0, self.__num, 1):
                if self.__box[index] == item:
                    itemIndex = index
                    flag = True
            # アイテム被りなし
            if not (flag):
                for index in (0, self.__num, 1):
                    if self.__box[index] == -1:
                        self.__box[index] = item
                        self.__boxNum[index] += 1
                        self.__num += 1
                        break
            else:
                self.__boxNum[itemIndex] += 1
            return True
        else:
            return False

    def watch(self, num):
        return (self.__box[num], self.__boxNum[num])

    def preWatch(self, num):
        return (self.__preBox[num], self.__preBoxNum[num])

    def updatePre(self):
        self.__preBox = [self.__box[0], self.__box[1], self.__box[2]]
        self.__preBoxNum = [self.__boxNum[0], self.__boxNum[1], self.__boxNum[2]]
        self.__preNum = self.__num

    def updateBoxButton(self, index, x, y):
        if index < self.__max and 0 < self.__num:
            if self.__box[index] != -1:
                self.__boxButton[index][0] = x
                self.__boxButton[index][1] = y
                self.__boxButton[index][2] = 60
                self.__boxButton[index][3] = 60
            else:
                self.__boxButton[index][0] = -1
                self.__boxButton[index][1] = -1
                self.__boxButton[index][2] = -1
                self.__boxButton[index][3] = -1

    def BOX_BUTTON(self, index):
        if index < self.__max and 0 < self.__num:
            return (self.__boxButton[index][0],
                    self.__boxButton[index][1],
                    self.__boxButton[index][2],
                    self.__boxButton[index][3])
        else:
            return (-1, -1, -1, -1)

    def useItem(self, index):
        if index < self.__max and 0 < self.__num:
            if self.__box[index] != -1 and not (self.__boxUseFlag[index]):
                self.__boxUseFlag[index] = True
                self.__boxUseTurn[index] = 10

    def BOX_USE_FLAG(self, index):
        if index < self.__max and 0 < self.__num:
            return self.__boxUseFlag[index]
        else:
            return False

    def pickUp(self, index):
        if index < self.__max and 0 < self.__num:
            if self.__boxUseFlag[index]:
                if self.__boxUseTurn[index] == 0:
                    self.__boxUseFlag[index] = False
                    self.__boxNum[index] -= 1
                    if self.__boxNum[index] == 0:
                        self.__num -= 1
                        self.__box[index] = -1
                    return (-1, 0)
                elif self.__boxUseTurn[index] == -2:
                    return (self.__box[index], self.__boxNum[index])
                else:
                    # アイテム 使用期間中
                    return (self.__box[index], self.__boxNum[index])
            else:
                return (-1, 0)
        else:
            return (-1, 0)

    def flagOn(self):
        self.__flag = True

    def FLAG(self):
        return self.__flag

    def useItemTurnCountup(self):
        if self.__flag:
            self.__flag = False
            if self.__boxUseTurn[0] != -1:
                self.__boxUseTurn[0] -= 1
            if self.__boxUseTurn[1] != -1:
                self.__boxUseTurn[1] -= 1
            if self.__boxUseTurn[2] != -1:
                self.__boxUseTurn[2] -= 1

    def NUM(self):
        return self.__num

    def PRE_NUM(self):
        return self.__preNum
