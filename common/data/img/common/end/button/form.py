class Form:
    def __init__(self):
        self.__homeButton = [-1, -1, 0, 0]

    def updateHomeButton(self, x, y, sizeW, sizeH):
        self.__homeButton[0] = x
        self.__homeButton[1] = y
        self.__homeButton[2] = sizeW
        self.__homeButton[3] = sizeH

    def HOME_BUTTON(self):
        return (self.__homeButton[0],
                self.__homeButton[1],
                self.__homeButton[2],
                self.__homeButton[3])
