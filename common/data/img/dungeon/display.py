import common.common as cmn
import common.pyd.hitJudge as hitJudge
import dungeon.data.img.img as img
import dungeon.data.map.map as map
import dungeon.pyd.index as INDEX
import dungeon.pyd.itemType as ITEM
import dungeon.pyd.action as ACTION
import pygame


class Display(cmn.cmnDisplay):
    def dispView(self, screen, dungeonForm, opeForm, posX: int, posY: int):
        (x, y) = opeForm.MOUSE()
        now_view = dungeonForm.NOW_VIEW()
        imgList = dungeonForm.IMG_LIST()
        if not (dungeonForm.IS_DEATH()):
            screen.blit(imgList[INDEX.RIGHT()][INDEX.UP_POS()][img.Select.RU(now_view)], (posX+600, posY))
            screen.blit(imgList[INDEX.RIGHT()][INDEX.CENTER_POS()][img.Select.RC(now_view)], (posX+600, posY+150))
            screen.blit(imgList[INDEX.RIGHT()][INDEX.DOWN_POS()][img.Select.RD(now_view)], (posX+600, posY+450))
            screen.blit(imgList[INDEX.CENTER()][INDEX.UP_POS()][img.Select.CU(now_view)], (posX+200, posY))
            screen.blit(imgList[INDEX.CENTER()][INDEX.CENTER_POS()][img.Select.CC(now_view)], (posX+200, posY+150))
            screen.blit(imgList[INDEX.CENTER()][INDEX.DOWN_POS()][img.Select.CD(now_view)], (posX+200, posY+450))
            screen.blit(imgList[INDEX.LEFT()][INDEX.UP_POS()][img.Select.LU(now_view)], (posX, posY))
            screen.blit(imgList[INDEX.LEFT()][INDEX.CENTER_POS()][img.Select.LC(now_view)], (posX, posY+150))
            screen.blit(imgList[INDEX.LEFT()][INDEX.DOWN_POS()][img.Select.LD(now_view)], (posX, posY+450))
            screen.blit(imgList[INDEX.FLAME()][img.Select.FLAME(now_view)], (posX, posY))
            # ITEM BOX
            Display.__dispBox(self, screen, imgList, posX+606, posY+526, x, y, dungeonForm)
            # USE ITEM
            Display.__dispItem(screen, dungeonForm, imgList)
        else:
            screen.blit(imgList[INDEX.FLAME()][1], (posX, posY))
            # RETRY
            Display.__dispButton(screen, imgList, x, y, posX+350, posY+270, 12)
            dungeonForm.updateRetryButton(posX+350, posY+270)

    def dispRader(self, screen, dungeonForm, flash, x: int, y: int):
        imgList = dungeonForm.IMG_LIST()
        posX = x + 70
        posY = y + 40
        screen.blit(imgList[INDEX.BOARD_S()][0], (x, y))
        screen.blit(imgList[INDEX.TEXT5()][img.Select.TEXT_FLASH(flash(1))], (posX - 10, posY - 20))
        if not (dungeonForm.IS_DEATH()):
            # 中心
            screen.blit(Display.__getRaderImg(dungeonForm, 9), (posX, posY))
            screen.blit(Display.__getRaderImg(dungeonForm, 6), (posX, posY + 20))
            screen.blit(Display.__getRaderImg(dungeonForm, 1), (posX, posY + 40))
            screen.blit(Display.__getRaderImg(dungeonForm, 0), (posX, posY + 60))
            screen.blit(Display.__getRaderImg(dungeonForm, 12), (posX, posY + 80))
            screen.blit(Display.__getRaderImg(dungeonForm, 15), (posX, posY + 100))
            screen.blit(Display.__getRaderImg(dungeonForm, 18), (posX, posY + 120))
            screen.blit(Display.__getRaderImg(dungeonForm, 8), (posX + 20, posY))
            screen.blit(Display.__getRaderImg(dungeonForm, 5), (posX + 20, posY + 20))
            screen.blit(Display.__getRaderImg(dungeonForm, 2), (posX + 20, posY + 40))
            screen.blit(imgList[INDEX.PLAYER()][img.Select.PLAYER(flash(0))], (posX + 20, posY + 60))
            screen.blit(Display.__getRaderImg(dungeonForm, 11), (posX + 20, posY + 80))
            screen.blit(Display.__getRaderImg(dungeonForm, 14), (posX + 20, posY + 100))
            screen.blit(Display.__getRaderImg(dungeonForm, 17), (posX + 20, posY + 120))
            screen.blit(Display.__getRaderImg(dungeonForm, 10), (posX + 40, posY))
            screen.blit(Display.__getRaderImg(dungeonForm, 7), (posX + 40, posY + 20))
            screen.blit(Display.__getRaderImg(dungeonForm, 3), (posX + 40, posY + 40))
            screen.blit(Display.__getRaderImg(dungeonForm, 4), (posX + 40, posY + 60))
            screen.blit(Display.__getRaderImg(dungeonForm, 13), (posX + 40, posY + 80))
            screen.blit(Display.__getRaderImg(dungeonForm, 16), (posX + 40, posY + 100))
            screen.blit(Display.__getRaderImg(dungeonForm, 19), (posX + 40, posY + 120))
            screen.blit(Display.__getRaderImg(dungeonForm, 20), (posX - 20, posY))
            screen.blit(Display.__getRaderImg(dungeonForm, 21), (posX - 20, posY + 20))
            screen.blit(Display.__getRaderImg(dungeonForm, 22), (posX - 20, posY + 40))
            screen.blit(Display.__getRaderImg(dungeonForm, 23), (posX - 20, posY + 60))
            screen.blit(Display.__getRaderImg(dungeonForm, 24), (posX - 20, posY + 80))
            screen.blit(Display.__getRaderImg(dungeonForm, 25), (posX - 20, posY + 100))
            screen.blit(Display.__getRaderImg(dungeonForm, 26), (posX - 20, posY + 120))
            screen.blit(Display.__getRaderImg(dungeonForm, 27), (posX + 60, posY))
            screen.blit(Display.__getRaderImg(dungeonForm, 28), (posX + 60, posY + 20))
            screen.blit(Display.__getRaderImg(dungeonForm, 29), (posX + 60, posY + 40))
            screen.blit(Display.__getRaderImg(dungeonForm, 30), (posX + 60, posY + 60))
            screen.blit(Display.__getRaderImg(dungeonForm, 31), (posX + 60, posY + 80))
            screen.blit(Display.__getRaderImg(dungeonForm, 32), (posX + 60, posY + 100))
            screen.blit(Display.__getRaderImg(dungeonForm, 33), (posX + 60, posY + 120))
            screen.blit(Display.__getRaderImg(dungeonForm, 34), (posX - 40, posY))
            screen.blit(Display.__getRaderImg(dungeonForm, 35), (posX - 40, posY + 20))
            screen.blit(Display.__getRaderImg(dungeonForm, 36), (posX - 40, posY + 40))
            screen.blit(Display.__getRaderImg(dungeonForm, 37), (posX - 40, posY + 60))
            screen.blit(Display.__getRaderImg(dungeonForm, 38), (posX - 40, posY + 80))
            screen.blit(Display.__getRaderImg(dungeonForm, 39), (posX - 40, posY + 100))
            screen.blit(Display.__getRaderImg(dungeonForm, 40), (posX - 40, posY + 120))
            screen.blit(Display.__getRaderImg(dungeonForm, 41), (posX + 80, posY))
            screen.blit(Display.__getRaderImg(dungeonForm, 42), (posX + 80, posY + 20))
            screen.blit(Display.__getRaderImg(dungeonForm, 43), (posX + 80, posY + 40))
            screen.blit(Display.__getRaderImg(dungeonForm, 44), (posX + 80, posY + 60))
            screen.blit(Display.__getRaderImg(dungeonForm, 45), (posX + 80, posY + 80))
            screen.blit(Display.__getRaderImg(dungeonForm, 46), (posX + 80, posY + 100))
            screen.blit(Display.__getRaderImg(dungeonForm, 47), (posX + 80, posY + 120))

    def dispInfo(self, screen, dungeonForm, flash, posX: int, posY: int):
        floor = dungeonForm.FLOOR()
        font = dungeonForm.FONT()
        imgList = dungeonForm.IMG_LIST()
        numberPosX = posX+90
        if not (dungeonForm.IS_DEATH()):
            screen.blit(imgList[INDEX.BOARD_S()][0], (posX, posY))
            # FLOOR
            screen.blit(imgList[INDEX.TEXT5()][img.Select.TEXT_FLASH(flash(1)) + 3], (posX + 60, posY + 20))
            super().dispNumber(screen, font, floor, numberPosX, posY+60)
            # ACTION COUNT
            screen.blit(imgList[INDEX.TEXT6()][img.Select.TEXT_FLASH(flash(1)) + 3], (posX + 27, posY + 90))
            screen.blit(imgList[INDEX.TEXT5()][img.Select.TEXT_FLASH(flash(1)) + 6], (posX + 103, posY + 90))
            super().dispNumber(screen, font, dungeonForm.COUNT(), numberPosX, posY+130)
        else:
            screen.blit(imgList[INDEX.BOARD_S()][1], (posX, posY))

    def dispConversationText(self, screen, dungeonForm, x: int, y: int):
        imgList = dungeonForm.IMG_LIST()
        font = dungeonForm.EVENT_FONT()
        log = dungeonForm.LOG()
        logNum = dungeonForm.LOG_NUM()
        screen.blit(imgList[INDEX.BOARD_M()][0], (x, y))
        (textX, textY) = (x+20, y+30)
        if (logNum != 0):
            index = 0
            for text in log:
                if index < 7:
                    super().dispText(screen, font, text, textX, textY)
                    textY += 23
                index += 1

    def dispSystemButton(self, screen, dungeonForm, opeForm, flash, posX, posY):
        (x, y) = opeForm.MOUSE()
        imgList = dungeonForm.IMG_LIST()
        buttonPosX = posX+25
        screen.blit(imgList[INDEX.BOARD_S()][0], (posX, posY))
        screen.blit(imgList[INDEX.TEXT6()][img.Select.TEXT_FLASH(flash(1))], (posX + 60, posY + 20))
        # CONFIG BUTTON
        Display.__dispButton(screen, imgList, x, y, buttonPosX, posY+45, 10)
        dungeonForm.updateConfigButton(buttonPosX, posY+45)
        # SAVE BUTTON
        Display.__dispButton(screen, imgList, x, y, buttonPosX, posY+115, 8)
        dungeonForm.updateSaveButton(buttonPosX, posY+115)

    def dispActionButton(self, screen, dungeonForm, opeForm, flash, posX: int, posY: int):
        (x, y) = opeForm.MOUSE()
        imgList = dungeonForm.IMG_LIST()
        if not (dungeonForm.IS_DEATH()):
            screen.blit(imgList[INDEX.BOARD_S()][0], (posX, posY))
            screen.blit(imgList[INDEX.TEXT6()][img.Select.TEXT_FLASH(flash(1))+3], (posX + 60, posY + 20))
            # 階段
            if map.Judge.isStairs(dungeonForm.MAP()[dungeonForm.NOW_POS()[0]][dungeonForm.NOW_POS()[1]]):
                Display.__dispActionButton(screen, imgList, dungeonForm, x, y, posX, posY, ACTION.GO_UP_THE_STAIRS())
            else:
                dungeonForm.updateActionButton(ACTION.GO_UP_THE_STAIRS(), -1, -1)
            dungeonForm.searchItem()
            # アイテム
            if dungeonForm.ITEM_GET_FLAG():
                Display.__dispActionButton(screen, imgList, dungeonForm, x, y, posX, posY, ACTION.SEARCH())
            else:
                dungeonForm.updateActionButton(ACTION.SEARCH(), -1, -1)
        else:
            screen.blit(imgList[INDEX.BOARD_S()][1], (posX, posY))
            dungeonForm.updateActionButton(ACTION.GO_UP_THE_STAIRS(), -1, -1)
            dungeonForm.updateActionButton(ACTION.SEARCH(), -1, -1)

    def __dispActionButton(screen, imgList, dungeonForm, x: int, y: int, posX, posY, actionType: int):
        actionIndex = [0, 2]
        # DISP BUTTON
        if hitJudge.hitJudgeSquare(posX+25, posY+45, 150, 60, x, y):
            screen.blit(imgList[INDEX.ACTION()][actionIndex[actionType]+1], (posX+25, posY+45))
        else:
            screen.blit(imgList[INDEX.ACTION()][actionIndex[actionType]], (posX+25, posY+45))
        # UPDATE BUTTON
        dungeonForm.updateActionButton(actionType, posX+25, posY+45)

    def __dispButton(screen, imgList, x: int, y: int, posX: int, posY: int, index: int):
        if hitJudge.hitJudgeSquare(posX, posY, 150, 60, x, y):
            screen.blit(imgList[INDEX.BUTTON()][index+1], (posX, posY))
        else:
            screen.blit(imgList[INDEX.BUTTON()][index], (posX, posY))

    def __dispBox(self, screen, imgList, posX, posY, x, y, dungeonForm):
        textList = ["", "", ""]
        textList[0] = Display.__dispBoxItem(self, screen, imgList, posX, posY, x, y, dungeonForm, 0)
        textList[1] = Display.__dispBoxItem(self, screen, imgList, posX+60, posY, x, y, dungeonForm, 1)
        textList[2] = Display.__dispBoxItem(self, screen, imgList, posX+120, posY, x, y, dungeonForm, 2)
        for text in textList:
            if text != "":
                super().dispText(screen, dungeonForm.ITEM_FONT(), text, x+10, y-10, cmn.Colors.black)


    def __dispBoxItem(self, screen, imgList, posX, posY, x, y, dungeonForm, index):
        itemFont = dungeonForm.ITEM_FONT()
        color = cmn.Colors.black
        text = ""
        (item, itemCount) = dungeonForm.watchBox(index)
        screen.blit(imgList[INDEX.BOX()][0], (posX, posY))
        if not (item == -1):
            screen.blit(imgList[INDEX.ITEM()][item], (posX+5, posY+5))
        if dungeonForm.itemBoxUseFlag(index):
            screen.blit(imgList[INDEX.BOX()][1], (posX, posY))
            super().dispText(screen, itemFont, str(itemCount), posX+2, posY+10, color)
            dungeonForm.itemBoxButtonUpdate(index, -1, -1)
        else:
            if not (item == -1):
                super().dispText(screen, itemFont, str(itemCount), posX+2, posY+10, color)
                dungeonForm.itemBoxButtonUpdate(index, posX, posY+5)
        if hitJudge.hitJudgeSquare(posX, posY, 60, 60, x, y) and not (item == -1):
            text = ITEM.getText(item) + ":" + str(itemCount)
            if not (dungeonForm.itemBoxUseFlag(index)):
                screen.blit(imgList[INDEX.BOX_TAG()][0], (posX, posY-20))
        return text

    def __dispItem(screen, dungeonForm, imgList):
        (item0, itemNum0) = dungeonForm.itemBoxPickUp(0)
        (item1, itemNum1) = dungeonForm.itemBoxPickUp(1)
        (item2, itemNum2) = dungeonForm.itemBoxPickUp(2)
        if item0 == ITEM.COMPASS():
            image = imgList[INDEX.COMPASS()][0]
            imag_rotate = pygame.transform.rotate(image, dungeonForm.createAngle())
            screen.blit(imag_rotate, imag_rotate.get_rect(center=image.get_rect(center=(65, 530)).center))
        if item1 == ITEM.COMPASS():
            image = imgList[INDEX.COMPASS()][0]
            imag_rotate = pygame.transform.rotate(image, dungeonForm.createAngle())
            screen.blit(imag_rotate, imag_rotate.get_rect(center=image.get_rect(center=(65, 530)).center))
        if item2 == ITEM.COMPASS():
            image = imgList[INDEX.COMPASS()][0]
            imag_rotate = pygame.transform.rotate(image, dungeonForm.createAngle())
            screen.blit(imag_rotate, imag_rotate.get_rect(center=image.get_rect(center=(65, 530)).center))

    def __isEnemy(dungeonForm, x: int, y: int):
        for index in range(0, dungeonForm.ENEMY_COUNT(), 1):
            enemyPos = dungeonForm.ENEMIS_POS(index)
            if enemyPos[0] == x and enemyPos[1] == y:
                if dungeonForm.APPEAR_FLAG(index):
                    return 1
                else:
                    return 0
        return 0

    def __getRaderImg(dungeonForm, number):
        situation = dungeonForm.SITUATION()
        imgList = dungeonForm.IMG_LIST()
        wallOrPath = img.Select.WALL_OR_PATH(situation[number][0])
        isEnemy = Display.__isEnemy(dungeonForm, situation[number][1], situation[number][2])
        return imgList[wallOrPath][isEnemy]
