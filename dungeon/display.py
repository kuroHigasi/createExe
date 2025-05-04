import dungeon.layer.request.dungeonDisplayRequest as dungeonDisplayRequest
import dungeon.service.display as service_display
import dungeon.form.form as form
import common.common as cmn
import pyd.hitJudge as hitJudge
import dungeon.img as img
import dungeon.data.map.map as map
import pyd.indexDungeon as INDEX
import pyd.typeItem as ITEM
import pyd.typeAction as ACTION
import pygame

from dungeon.abstract.abstractDisplay import AbstractDisplay


class Display(AbstractDisplay):
    @staticmethod
    def execute(dungeon_form: form.Form, request: dungeonDisplayRequest.DungeonDisplayRequest):
        service = service_display.Display(request)
        service.disp_radar()
        res_view = service.disp_view()
        if res_view.is_ok():
            if not (res_view.data[0] is None):
                (index, pos_x, pos_y) = res_view.data[0]
                dungeon_form.itemBoxButtonUpdate(index, pos_x, pos_y)
            if not (res_view.data[1] is None):
                (pos_x, pos_y) = res_view.data[1]
                dungeon_form.set_retry_button(pos_x, pos_y)
            else:
                dungeon_form.set_retry_button(-1, -1)

    @staticmethod
    def create_request_data(screen, dungeon_form: form.Form, ope_form, system_form):
        (mouse_x, mouse_y) = ope_form.get_mouse()
        dungeon_map = dungeon_form.get_dungeon_map()
        now_pos = dungeon_form.get_now_pos()
        flash = system_form.FLASH
        enemy_pos_list = []
        enemy_type_list = []
        enemy_index_list = []
        count = 0
        for index in range(0, dungeon_form.ENEMY_COUNT(), 1):
            if dungeon_form.APPEAR_FLAG(index):
                enemy_pos_list.insert(count, dungeon_form.ENEMIS_POS(index))
                enemy_type_list.insert(count, dungeon_form.ENEMIS_TYPE(index))
                enemy_index_list.insert(count, index)
                count += 1
        (config_x, config_y, config_width, config_height) = dungeon_form.get_config_button()
        (save_x, save_y, save_width, save_height) = dungeon_form.get_save_button()
        (retry_x, retry_y, retry_width, retry_height) = dungeon_form.get_retry_button()
        box0_item, box0_num = dungeon_form.watchBox(0)
        box1_item, box1_num = dungeon_form.watchBox(1)
        box2_item, box2_num = dungeon_form.watchBox(2)
        (box0_x, box0_y, box0_width, box0_height) = dungeon_form.BOX_BUTTON(0)
        (box1_x, box1_y, box1_width, box1_height) = dungeon_form.BOX_BUTTON(1)
        (box2_x, box2_y, box2_width, box2_height) = dungeon_form.BOX_BUTTON(2)
        return dungeonDisplayRequest.DungeonDisplayRequest(
            screen,
            dungeon_form.img_list,
            dungeon_form.font(),
            dungeon_form.item_font(),
            dungeon_form.event_font(),
            dungeon_form.is_death(),
            map.Judge.isStairs(dungeon_map[now_pos[0]][now_pos[1]]),
            dungeon_form.ITEM_GET_FLAG(),
            dungeon_form.get_now_view(),
            dungeon_form.get_situation(),
            flash(1),
            flash(0),
            enemy_pos_list,
            enemy_type_list,
            enemy_index_list,
            dungeon_form.get_log(),
            dungeon_form.get_log_num(),
            hitJudge.hitJudgeSquare(config_x, config_y, config_width, config_height, mouse_x, mouse_y),
            hitJudge.hitJudgeSquare(save_x, save_y, save_width, save_height, mouse_x, mouse_y),
            hitJudge.hitJudgeSquare(retry_x, retry_y, retry_width, retry_height, mouse_x, mouse_y),
            box0_item,
            box0_num,
            dungeon_form.itemBoxUseFlag(0),
            hitJudge.hitJudgeSquare(box0_x, box0_y, box0_width, box0_height, mouse_x, mouse_y),
            box1_item,
            box1_num,
            dungeon_form.itemBoxUseFlag(1),
            hitJudge.hitJudgeSquare(box1_x, box1_y, box1_width, box1_height, mouse_x, mouse_y),
            box2_item,
            box2_num,
            dungeon_form.itemBoxUseFlag(2),
            hitJudge.hitJudgeSquare(box2_x, box2_y, box2_width, box2_height, mouse_x, mouse_y),
            dungeon_form.create_angle(),
            mouse_x,
            mouse_y
        )

    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def dispActionButton(screen, dungeon_form, ope_form, flash, pos_x: int, pos_y: int):
        (x, y) = ope_form.get_mouse()
        img_list = dungeon_form.img_list
        if not (dungeon_form.is_death()):
            screen.blit(img_list[INDEX.BOARD_S()][0], (pos_x, pos_y))
            screen.blit(img_list[INDEX.TEXT6()][img.Select.TEXT_FLASH(flash(1)) + 3], (pos_x + 60, pos_y + 20))
            # 階段
            if map.Judge.isStairs(dungeon_form.get_dungeon_map()[dungeon_form.get_now_pos()[0]][dungeon_form.get_now_pos()[1]]):
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

    def __dispText(screen, font, text, x, y, color=cmn.Colors.white):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x+text_surface.get_width() / 2, y))
        screen.blit(text_surface, text_rect)

    def __dispNumber(screen, font, number, x, y, color=cmn.Colors.white):
        text_surface = font.render(str(number), True, color)
        numCount = len(str(number))
        text_rect = text_surface.get_rect(center=(x+text_surface.get_width() / 2 - ((numCount - 1) * 6), y))
        screen.blit(text_surface, text_rect)
