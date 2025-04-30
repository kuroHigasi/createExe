import common.common as cmn
import pyd.hitJudge as hitJudge
import dungeon.img as img
import dungeon.data.map.map as map
import pyd.indexDungeon as INDEX
import pyd.typeItem as ITEM
import pyd.typeAction as ACTION
import pygame


class Display():
    def dispView(screen, dungeon_form, ope_form, pos_x: int, pos_y: int):
        (x, y) = ope_form.get_mouse()
        now_view = dungeon_form.NOW_VIEW()
        img_list = dungeon_form.img_list
        if not (dungeon_form.is_death()):
            screen.blit(img_list[INDEX.RIGHT()][INDEX.UP_POS()][img.Select.RU(now_view)], (pos_x + 600, pos_y))
            screen.blit(img_list[INDEX.RIGHT()][INDEX.CENTER_POS()][img.Select.RC(now_view)], (pos_x + 600, pos_y + 150))
            screen.blit(img_list[INDEX.RIGHT()][INDEX.DOWN_POS()][img.Select.RD(now_view)], (pos_x + 600, pos_y + 450))
            screen.blit(img_list[INDEX.CENTER()][INDEX.UP_POS()][img.Select.CU(now_view)], (pos_x + 200, pos_y))
            screen.blit(img_list[INDEX.CENTER()][INDEX.CENTER_POS()][img.Select.CC(now_view)], (pos_x + 200, pos_y + 150))
            screen.blit(img_list[INDEX.CENTER()][INDEX.DOWN_POS()][img.Select.CD(now_view)], (pos_x + 200, pos_y + 450))
            screen.blit(img_list[INDEX.LEFT()][INDEX.UP_POS()][img.Select.LU(now_view)], (pos_x, pos_y))
            screen.blit(img_list[INDEX.LEFT()][INDEX.CENTER_POS()][img.Select.LC(now_view)], (pos_x, pos_y + 150))
            screen.blit(img_list[INDEX.LEFT()][INDEX.DOWN_POS()][img.Select.LD(now_view)], (pos_x, pos_y + 450))
            screen.blit(img_list[INDEX.FLAME()][img.Select.FLAME(now_view)], (pos_x, pos_y))
            # ITEM BOX
            Display.__dispBox(screen, img_list, pos_x+606, pos_y+526, x, y, dungeon_form)
            # USE ITEM
            Display.__dispItem(screen, dungeon_form, img_list)
        else:
            screen.blit(img_list[INDEX.FLAME()][1], (pos_x, pos_y))
            # RETRY
            Display.__dispButton(screen, img_list, x, y, pos_x+350, pos_y+270, 12)
            dungeon_form.set_retry_button(pos_x+350, pos_y+270)

    def dispRader(screen, dungeon_form, flash, x: int, y: int):
        img_list = dungeon_form.img_list
        pos_x = x + 70
        pos_y = y + 40
        screen.blit(img_list[INDEX.BOARD_S()][0], (x, y))
        screen.blit(img_list[INDEX.TEXT5()][img.Select.TEXT_FLASH(flash(1))], (pos_x - 10, pos_y - 20))
        if not (dungeon_form.is_death()):
            # 中心
            screen.blit(Display.__getRaderImg(dungeon_form, 9), (pos_x, pos_y))
            screen.blit(Display.__getRaderImg(dungeon_form, 6), (pos_x, pos_y + 20))
            screen.blit(Display.__getRaderImg(dungeon_form, 1), (pos_x, pos_y + 40))
            screen.blit(Display.__getRaderImg(dungeon_form, 0), (pos_x, pos_y + 60))
            screen.blit(Display.__getRaderImg(dungeon_form, 12), (pos_x, pos_y + 80))
            screen.blit(Display.__getRaderImg(dungeon_form, 15), (pos_x, pos_y + 100))
            screen.blit(Display.__getRaderImg(dungeon_form, 18), (pos_x, pos_y + 120))
            screen.blit(Display.__getRaderImg(dungeon_form, 8), (pos_x + 20, pos_y))
            screen.blit(Display.__getRaderImg(dungeon_form, 5), (pos_x + 20, pos_y + 20))
            screen.blit(Display.__getRaderImg(dungeon_form, 2), (pos_x + 20, pos_y + 40))
            screen.blit(img_list[INDEX.PLAYER()][img.Select.PLAYER(flash(0))], (pos_x + 20, pos_y + 60))
            screen.blit(Display.__getRaderImg(dungeon_form, 11), (pos_x + 20, pos_y + 80))
            screen.blit(Display.__getRaderImg(dungeon_form, 14), (pos_x + 20, pos_y + 100))
            screen.blit(Display.__getRaderImg(dungeon_form, 17), (pos_x + 20, pos_y + 120))
            screen.blit(Display.__getRaderImg(dungeon_form, 10), (pos_x + 40, pos_y))
            screen.blit(Display.__getRaderImg(dungeon_form, 7), (pos_x + 40, pos_y + 20))
            screen.blit(Display.__getRaderImg(dungeon_form, 3), (pos_x + 40, pos_y + 40))
            screen.blit(Display.__getRaderImg(dungeon_form, 4), (pos_x + 40, pos_y + 60))
            screen.blit(Display.__getRaderImg(dungeon_form, 13), (pos_x + 40, pos_y + 80))
            screen.blit(Display.__getRaderImg(dungeon_form, 16), (pos_x + 40, pos_y + 100))
            screen.blit(Display.__getRaderImg(dungeon_form, 19), (pos_x + 40, pos_y + 120))
            screen.blit(Display.__getRaderImg(dungeon_form, 20), (pos_x - 20, pos_y))
            screen.blit(Display.__getRaderImg(dungeon_form, 21), (pos_x - 20, pos_y + 20))
            screen.blit(Display.__getRaderImg(dungeon_form, 22), (pos_x - 20, pos_y + 40))
            screen.blit(Display.__getRaderImg(dungeon_form, 23), (pos_x - 20, pos_y + 60))
            screen.blit(Display.__getRaderImg(dungeon_form, 24), (pos_x - 20, pos_y + 80))
            screen.blit(Display.__getRaderImg(dungeon_form, 25), (pos_x - 20, pos_y + 100))
            screen.blit(Display.__getRaderImg(dungeon_form, 26), (pos_x - 20, pos_y + 120))
            screen.blit(Display.__getRaderImg(dungeon_form, 27), (pos_x + 60, pos_y))
            screen.blit(Display.__getRaderImg(dungeon_form, 28), (pos_x + 60, pos_y + 20))
            screen.blit(Display.__getRaderImg(dungeon_form, 29), (pos_x + 60, pos_y + 40))
            screen.blit(Display.__getRaderImg(dungeon_form, 30), (pos_x + 60, pos_y + 60))
            screen.blit(Display.__getRaderImg(dungeon_form, 31), (pos_x + 60, pos_y + 80))
            screen.blit(Display.__getRaderImg(dungeon_form, 32), (pos_x + 60, pos_y + 100))
            screen.blit(Display.__getRaderImg(dungeon_form, 33), (pos_x + 60, pos_y + 120))
            screen.blit(Display.__getRaderImg(dungeon_form, 34), (pos_x - 40, pos_y))
            screen.blit(Display.__getRaderImg(dungeon_form, 35), (pos_x - 40, pos_y + 20))
            screen.blit(Display.__getRaderImg(dungeon_form, 36), (pos_x - 40, pos_y + 40))
            screen.blit(Display.__getRaderImg(dungeon_form, 37), (pos_x - 40, pos_y + 60))
            screen.blit(Display.__getRaderImg(dungeon_form, 38), (pos_x - 40, pos_y + 80))
            screen.blit(Display.__getRaderImg(dungeon_form, 39), (pos_x - 40, pos_y + 100))
            screen.blit(Display.__getRaderImg(dungeon_form, 40), (pos_x - 40, pos_y + 120))
            screen.blit(Display.__getRaderImg(dungeon_form, 41), (pos_x + 80, pos_y))
            screen.blit(Display.__getRaderImg(dungeon_form, 42), (pos_x + 80, pos_y + 20))
            screen.blit(Display.__getRaderImg(dungeon_form, 43), (pos_x + 80, pos_y + 40))
            screen.blit(Display.__getRaderImg(dungeon_form, 44), (pos_x + 80, pos_y + 60))
            screen.blit(Display.__getRaderImg(dungeon_form, 45), (pos_x + 80, pos_y + 80))
            screen.blit(Display.__getRaderImg(dungeon_form, 46), (pos_x + 80, pos_y + 100))
            screen.blit(Display.__getRaderImg(dungeon_form, 47), (pos_x + 80, pos_y + 120))

    def dispInfo(screen, dungeon_form, flash, pos_x: int, pos_y: int):
        floor = dungeon_form.get_floor()
        font = dungeon_form.font()
        img_list = dungeon_form.img_list
        numberPosX = pos_x+90
        if not (dungeon_form.is_death()):
            screen.blit(img_list[INDEX.BOARD_S()][0], (pos_x, pos_y))
            # FLOOR
            screen.blit(img_list[INDEX.TEXT5()][img.Select.TEXT_FLASH(flash(1)) + 3], (pos_x + 60, pos_y + 20))
            Display.__dispNumber(screen, font, floor, numberPosX, pos_y+60)
            # ACTION COUNT
            screen.blit(img_list[INDEX.TEXT6()][img.Select.TEXT_FLASH(flash(1)) + 3], (pos_x + 27, pos_y + 90))
            screen.blit(img_list[INDEX.TEXT5()][img.Select.TEXT_FLASH(flash(1)) + 6], (pos_x + 103, pos_y + 90))
            Display.__dispNumber(screen, font, dungeon_form.get_count(), numberPosX, pos_y+130)
        else:
            screen.blit(img_list[INDEX.BOARD_S()][1], (pos_x, pos_y))

    def dispConversationText(screen, dungeon_form, x: int, y: int):
        img_list = dungeon_form.img_list
        font = dungeon_form.event_font()
        log = dungeon_form.get_log()
        screen.blit(img_list[INDEX.BOARD_M()][0], (x, y))
        (textX, textY) = (x+20, y+30)
        if dungeon_form.get_log_num() != 0:
            index = 0
            for text in log:
                if index < 7:
                    Display.__dispText(screen, font, text, textX, textY)
                    textY += 23
                index += 1

    def dispSystemButton(screen, dungeon_form, ope_form, flash, pos_x, pos_y):
        (x, y) = ope_form.get_mouse()
        img_list = dungeon_form.img_list
        buttonPosX = pos_x+25
        screen.blit(img_list[INDEX.BOARD_S()][0], (pos_x, pos_y))
        screen.blit(img_list[INDEX.TEXT6()][img.Select.TEXT_FLASH(flash(1))], (pos_x + 60, pos_y + 20))
        # CONFIG BUTTON
        Display.__dispButton(screen, img_list, x, y, buttonPosX, pos_y+45, 10)
        dungeon_form.set_config_button(buttonPosX, pos_y+45)
        # SAVE BUTTON
        Display.__dispButton(screen, img_list, x, y, buttonPosX, pos_y+115, 8)
        dungeon_form.set_save_button(buttonPosX, pos_y+115)

    def dispActionButton(screen, dungeon_form, ope_form, flash, pos_x: int, pos_y: int):
        (x, y) = ope_form.get_mouse()
        img_list = dungeon_form.img_list
        if not (dungeon_form.is_death()):
            screen.blit(img_list[INDEX.BOARD_S()][0], (pos_x, pos_y))
            screen.blit(img_list[INDEX.TEXT6()][img.Select.TEXT_FLASH(flash(1)) + 3], (pos_x + 60, pos_y + 20))
            # 階段
            if map.Judge.isStairs(dungeon_form.get_dungeon_map()[dungeon_form.NOW_POS()[0]][dungeon_form.NOW_POS()[1]]):
                Display.__dispActionButton(screen, img_list, dungeon_form, x, y, pos_x, pos_y, ACTION.GO_UP_THE_STAIRS())
            else:
                dungeon_form.set_action_button(ACTION.GO_UP_THE_STAIRS(), -1, -1)
            dungeon_form.searchItem()
            # アイテム
            if dungeon_form.ITEM_GET_FLAG():
                Display.__dispActionButton(screen, img_list, dungeon_form, x, y, pos_x, pos_y, ACTION.SEARCH())
            else:
                dungeon_form.set_action_button(ACTION.SEARCH(), -1, -1)
        else:
            screen.blit(img_list[INDEX.BOARD_S()][1], (pos_x, pos_y))
            dungeon_form.set_action_button(ACTION.GO_UP_THE_STAIRS(), -1, -1)
            dungeon_form.set_action_button(ACTION.SEARCH(), -1, -1)

    def __dispActionButton(screen, img_list, dungeon_form, x: int, y: int, pos_x, pos_y, actionType: int):
        actionIndex = [0, 2]
        # DISP BUTTON
        if hitJudge.hitJudgeSquare(pos_x+25, pos_y+45, 150, 60, x, y):
            screen.blit(img_list[INDEX.ACTION()][actionIndex[actionType]+1], (pos_x+25, pos_y+45))
        else:
            screen.blit(img_list[INDEX.ACTION()][actionIndex[actionType]], (pos_x+25, pos_y+45))
        # UPDATE BUTTON
        dungeon_form.set_action_button(actionType, pos_x+25, pos_y+45)

    def __dispButton(screen, img_list, x: int, y: int, pos_x: int, pos_y: int, index: int):
        if hitJudge.hitJudgeSquare(pos_x, pos_y, 150, 60, x, y):
            screen.blit(img_list[INDEX.BUTTON()][index+1], (pos_x, pos_y))
        else:
            screen.blit(img_list[INDEX.BUTTON()][index], (pos_x, pos_y))

    def __dispBox(screen, img_list, pos_x, pos_y, x, y, dungeon_form):
        textList = ["", "", ""]
        textList[0] = Display.__dispBoxItem(screen, img_list, pos_x, pos_y, x, y, dungeon_form, 0)
        textList[1] = Display.__dispBoxItem(screen, img_list, pos_x+60, pos_y, x, y, dungeon_form, 1)
        textList[2] = Display.__dispBoxItem(screen, img_list, pos_x+120, pos_y, x, y, dungeon_form, 2)
        for text in textList:
            if text != "":
                Display.__dispText(screen, dungeon_form.item_font(), text, x+10, y-10, cmn.Colors.black)

    def __dispBoxItem(screen, img_list, pos_x, pos_y, x, y, dungeon_form, index):
        itemFont = dungeon_form.item_font()
        color = cmn.Colors.black
        text = ""
        (item, itemCount) = dungeon_form.watchBox(index)
        screen.blit(img_list[INDEX.BOX()][0], (pos_x, pos_y))
        if not (item == -1):
            screen.blit(img_list[INDEX.ITEM()][item], (pos_x+5, pos_y+5))
        if dungeon_form.itemBoxUseFlag(index):
            screen.blit(img_list[INDEX.BOX()][1], (pos_x, pos_y))
            Display.__dispText(screen, itemFont, str(itemCount), pos_x+2, pos_y+10, color)
            dungeon_form.itemBoxButtonUpdate(index, -1, -1)
        else:
            if not (item == -1):
                Display.__dispText(screen, itemFont, str(itemCount), pos_x+2, pos_y+10, color)
                dungeon_form.itemBoxButtonUpdate(index, pos_x, pos_y+5)
        if hitJudge.hitJudgeSquare(pos_x, pos_y, 60, 60, x, y) and not (item == -1):
            text = ITEM.getText(item) + ":" + str(itemCount)
            if not (dungeon_form.itemBoxUseFlag(index)):
                screen.blit(img_list[INDEX.BOX_TAG()][0], (pos_x, pos_y-20))
        return text

    def __dispItem(screen, dungeon_form, img_list):
        (item0, itemNum0) = dungeon_form.itemBoxPickUp(0)
        (item1, itemNum1) = dungeon_form.itemBoxPickUp(1)
        (item2, itemNum2) = dungeon_form.itemBoxPickUp(2)
        if item0 == ITEM.COMPASS():
            image = img_list[INDEX.COMPASS()][0]
            image_rotate = pygame.transform.rotate(image, dungeon_form.create_angle())
            screen.blit(image_rotate, image_rotate.get_rect(center=image.get_rect(center=(65, 530)).center))
        if item1 == ITEM.COMPASS():
            image = img_list[INDEX.COMPASS()][0]
            image_rotate = pygame.transform.rotate(image, dungeon_form.create_angle())
            screen.blit(image_rotate, image_rotate.get_rect(center=image.get_rect(center=(65, 530)).center))
        if item2 == ITEM.COMPASS():
            image = img_list[INDEX.COMPASS()][0]
            image_rotate = pygame.transform.rotate(image, dungeon_form.create_angle())
            screen.blit(image_rotate, image_rotate.get_rect(center=image.get_rect(center=(65, 530)).center))

    def __isEnemy(dungeon_form, x: int, y: int):
        for index in range(0, dungeon_form.ENEMY_COUNT(), 1):
            enemyPos = dungeon_form.ENEMIS_POS(index)
            if enemyPos.x == x and enemyPos.y == y:
                if dungeon_form.APPEAR_FLAG(index):
                    return 1
                else:
                    return 0
        return 0

    @staticmethod
    def __getRaderImg(dungeon_form, number):
        situation = dungeon_form.get_situation()
        img_list = dungeon_form.img_list
        wallOrPath = img.Select.WALL_OR_PATH(situation[number][0])
        isEnemy = Display.__isEnemy(dungeon_form, situation[number][1], situation[number][2])
        return img_list[wallOrPath][isEnemy]

    def __dispText(screen, font, text, x, y, color=cmn.Colors.white):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x+text_surface.get_width() / 2, y))
        screen.blit(text_surface, text_rect)

    def __dispNumber(screen, font, number, x, y, color=cmn.Colors.white):
        text_surface = font.render(str(number), True, color)
        numCount = len(str(number))
        text_rect = text_surface.get_rect(center=(x+text_surface.get_width() / 2 - ((numCount - 1) * 6), y))
        screen.blit(text_surface, text_rect)
