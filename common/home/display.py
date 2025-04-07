import common.home.pyd.index as index
import lib.hitJudge as judge


class Display:
    def dispHome(screen, homeFoem, opeForm, posX: int, posY: int):
        imgList = homeFoem.IMG_LIST()
        screen.blit(imgList[index.HOME()][0], (posX, posY))
        # START
        Display.__dispButton(screen, imgList, opeForm, 2, 50, 300)
        homeFoem.updateStartButton(50, 300)
        # LOAD
        Display.__dispButton(screen, imgList, opeForm, 6, 50, 390)
        homeFoem.updateLoadButton(50, 390)
        # CONFIG
        Display.__dispButton(screen, imgList, opeForm, 10, 50, 580)
        homeFoem.updateConfigButton(50, 580)
        # EXIT
        Display.__dispButton(screen, imgList, opeForm, 0, 50, 670)
        homeFoem.updateExitButton(50, 670)

    def __dispButton(screen, imgList, opeForm, buttonIndex: int, posX: int, posY: int):
        (x, y) = opeForm.MOUSE()
        if judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[index.BUTTON()][buttonIndex+1], (posX, posY))
        else:
            screen.blit(imgList[index.BUTTON()][buttonIndex], (posX, posY))
