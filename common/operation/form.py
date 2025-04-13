import pyd.calc as calc
import common.debug.debug as dbg


class OperationForm:
    def __init__(self):
        self.__directionKey = 0b0000
        self.__space = 0
        self.__enter = 0
        self.__click = 0b0000
        self.__mouseX = 0
        self.__mouseY = 0
        self.__mouseXclickR = -1
        self.__mouseYclickR = -1
        self.__mouseXclickL = -1
        self.__mouseYclickL = -1

    def reset(self):
        self.__directionKey = 0b0000

    def upOn(self):
        self.__directionKey = calc.bitmask(self.__directionKey, 0b0001)

    def upOff(self):
        self.__directionKey = calc.maskAndRight(self.__directionKey, 0b1110, 0)

    def UP(self):
        return (calc.maskAndRight(self.__directionKey, 0b0001, 0) == 0b0001)

    def leftOn(self):
        self.__directionKey = calc.bitmask(self.__directionKey, 0b0010)

    def leftOff(self):
        self.__directionKey = calc.maskAndRight(self.__directionKey, 0b1101, 0)

    def LEFT(self):
        return (calc.maskAndRight(self.__directionKey, 0b0010, 1) == 0b0001)

    def rightOn(self):
        self.__directionKey = calc.bitmask(self.__directionKey, 0b0100)

    def rightOff(self):
        self.__directionKey = calc.maskAndRight(self.__directionKey, 0b1011, 0)

    def RIGHT(self):
        return (calc.maskAndRight(self.__directionKey, 0b0100, 2) == 0b0001)

    def downOn(self):
        self.__directionKey = calc.bitmask(self.__directionKey, 0b1000)

    def downOff(self):
        self.__directionKey = calc.maskAndRight(self.__directionKey, 0b0111, 0)

    def DOWN(self):
        return (calc.maskAndRight(self.__directionKey, 0b1000, 3) == 0b0001)

    def spaceOn(self):
        self.__space = 1

    def spaceOff(self):
        self.__space = 0

    def SPACE(self):
        return (self.__space == 1)

    def enterOn(self):
        self.__enter = 1

    def enterOff(self):
        self.__enter = 0

    def ENTER(self):
        return (self.__enter == 1)

    def rightClickOn(self):
        if calc.maskAndRight(self.__click, 0b0001, 0) == 0:
            self.__mouseXclickR = self.__mouseX
            self.__mouseYclickR = self.__mouseY
            dbg.LOG("RIGHT CLICK ONESHOT")
        self.__click = calc.bitmask(self.__click, 0b0001)

    def rightClickOff(self):
        if calc.maskAndRight(self.__click, 0b0001, 0) == 1:
            self.__mouseXclickR = -1
            self.__mouseYclickR = -1
        self.__click = calc.maskAndRight(self.__click, 0b1110, 0)

    def isRightClick(self):
        return (calc.maskAndRight(self.__click, 0b0001, 0) == 1)

    def rightClickMoveMouse(self):
        return (self.__mouseXclickR, self.__mouseYclickR)

    def leftClickOn(self):
        if calc.maskAndRight(self.__click, 0b0010, 1) == 0:
            self.__mouseXclickL = self.__mouseX
            self.__mouseYclickL = self.__mouseY
            dbg.LOG("LEFT CLICK ONESHOT")
        self.__click = calc.bitmask(self.__click, 0b0010)

    def leftClickOff(self):
        if calc.maskAndRight(self.__click, 0b0010, 1) == 1:
            self.__mouseXclickL = -1
            self.__mouseYclickL = -1
        self.__click = calc.maskAndRight(self.__click, 0b1101, 0)

    def isLeftClick(self):
        return (calc.maskAndRight(self.__click, 0b0010, 1) == 1)

    def leftClickMoveMouse(self):
        return (self.__mouseXclickL, self.__mouseYclickL)

    def resetClick(self):
        self.__click = 0b0000
        self.__mouseXclickR = 0
        self.__mouseYclickR = 0
        self.__mouseXclickL = 0
        self.__mouseYclickL = 0

    def setMouse(self, x, y):
        self.__mouseX = x
        self.__mouseY = y

    def resetMouseClickR(self):
        self.__mouseXclickR = -1
        self.__mouseYclickR = -1

    def resetMouseClickL(self):
        self.__mouseXclickL = -1
        self.__mouseYclickL = -1

    def MOUSE(self):
        return (self.__mouseX, self.__mouseY)
