import common.download as homeImg


class Form:
    def __init__(self):
        self.__imgList = homeImg.Download.homeImag()
        self.__configButton = (-1, -1)
        self.__statrButton = (-1, -1)
        self.__exitButton = (-1, -1)
        self.__loadButton = (-1, -1)

    def IMG_LIST(self):
        return self.__imgList

    def updateConfigButton(self, x, y):
        self.__configButton = (x, y)

    def CONFIG_BUTTON(self):
        return self.__configButton

    def updateStartButton(self, x, y):
        self.__statrButton = (x, y)

    def START_BUTTON(self):
        return self.__statrButton

    def updateExitButton(self, x, y):
        self.__exitButton = (x, y)

    def EXIT_BUTTON(self):
        return self.__exitButton

    def updateLoadButton(self, x, y):
        self.__loadButton = (x, y)

    def LOAD_BUTTON(self):
        return self.__loadButton
