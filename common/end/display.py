import pyd.indexEnd as INDEX
import pyd.hitJudge as judge
import common.common as cmn


class Display:
    def endDisplay(screen, endForm, opeForm, posX: int, posY: int):
        imgList = endForm.IMG_LIST()
        font = endForm.FONT()
        screen.blit(imgList[INDEX.END()][0], (posX, posY))
        # TEXT
        Display.__dispText(screen, font, "総行動数:" + str(endForm.COUNT()), 50, 200)
        # HOME
        Display.__dispButton(screen, imgList, opeForm, 4, 50, 670)
        endForm.updateHomeButton(50, 670)

    def __dispButton(screen, imgList, opeForm, buttonIndex: int, posX: int, posY: int):
        (x, y) = opeForm.MOUSE()
        if judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[INDEX.BUTTON()][buttonIndex+1], (posX, posY))
        else:
            screen.blit(imgList[INDEX.BUTTON()][buttonIndex], (posX, posY))

    def __dispText(screen, font, text: str, x: int, y: int):
        text_surface = font.render(text, True, cmn.Colors.black)
        text_rect = text_surface.get_rect(center=(x+text_surface.get_width()/2, y))
        screen.blit(text_surface, text_rect)
