import common.debug as dbg


ACTION_ERROR_TEXT = "存在しないACTION"


class Form:
    def __init__(self):
        self.__configButton = [-1, -1, 0, 0]
        self.__homeButton = [-1, -1, 0, 0]
        self.__saveButton = [-1, -1, 0, 0]
        self.__retryButton = [-1, -1, 0, 0]
        self.__exitButton = [-1, -1, 0, 0]
        self.__actionButton = [[-1, -1, 0, 0], [-1, -1, 0, 0]]

    def updateConfigButton(self, x, y, sizeW, sizeH):
        self.__configButton = [x, y, sizeW, sizeH]

    def resetConfigButton(self):
        self.__configButton = [-1, -1, 0, 0]

    def CONFIG_BUTTON(self):
        return (self.__configButton[0],
                self.__configButton[1],
                self.__configButton[2],
                self.__configButton[3])

    def updateHomeButton(self, x, y, sizeW, sizeH):
        self.__homeButton = [x, y, sizeW, sizeH]

    def resetHomeButton(self):
        self.__homeButton = [-1, -1, 0, 0]

    def HOME_BUTTON(self):
        return (self.__homeButton[0],
                self.__homeButton[1],
                self.__homeButton[2],
                self.__homeButton[3])

    def updateExitButton(self, x, y, sizeW, sizeH):
        self.__exitButton = [x, y, sizeW, sizeH]

    def resetExitButton(self):
        self.__exitButton = [-1, -1, 0, 0]

    def EXIT_BUTTON(self):
        return (self.__exitButton[0],
                self.__exitButton[1],
                self.__exitButton[2],
                self.__exitButton[3])

    def updateSaveButton(self, x, y, sizeW, sizeH):
        self.__saveButton = [x, y, sizeW, sizeH]

    def resetSaveButton(self):
        self.__saveButton = [-1, -1, 0, 0]

    def SAVE_BUTTON(self):
        return (self.__saveButton[0],
                self.__saveButton[1],
                self.__saveButton[2],
                self.__saveButton[3])

    def updateRetryButton(self, x, y, sizeW, sizeH):
        self.__retryButton = [x, y, sizeW, sizeH]

    def resetRetryButton(self):
        self.__retryButton = [-1, -1, 0, 0]

    def RETRY_BUTTON(self):
        return (self.__retryButton[0],
                self.__retryButton[1],
                self.__retryButton[2],
                self.__retryButton[3])

    def updateActionButton(self, actIndex, x, y, sizeW, sizeH):
        if actIndex < len(self.__actionButton):
            self.__actionButton[actIndex][0] = x
            self.__actionButton[actIndex][1] = y
            self.__actionButton[actIndex][2] = sizeW
            self.__actionButton[actIndex][3] = sizeH
        else:
            dbg.ERROR_LOG(ACTION_ERROR_TEXT)

    def resetActionButton(self, actIndex):
        if actIndex < len(self.__actionButton):
            self.__actionButton[actIndex][0] = -1
            self.__actionButton[actIndex][1] = -1
            self.__actionButton[actIndex][2] = 0
            self.__actionButton[actIndex][3] = 0
        else:
            dbg.ERROR_LOG(ACTION_ERROR_TEXT)

    def ACTION_BUTTON(self, actIndex):
        if actIndex < len(self.__actionButton):
            return (self.__actionButton[actIndex][0],
                    self.__actionButton[actIndex][1],
                    self.__actionButton[actIndex][2],
                    self.__actionButton[actIndex][3])
        else:
            dbg.ERROR_LOG(ACTION_ERROR_TEXT)
            return (-1, -1, 0, 0)
