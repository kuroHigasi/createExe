import dungeon.layer.request.dungeonDisplayRequest as dungeonDisplayRequest
import dungeon.service.display as service_display
import dungeon.form.form as form
import pyd.hitJudge as hitJudge
import dungeon.data.map.map as map
import pyd.typeAction as ACTION
from dungeon.abstract.abstractDisplay import AbstractDisplay


class Display(AbstractDisplay):
    @staticmethod
    def execute(dungeon_form: form.Form, request: dungeonDisplayRequest.DungeonDisplayRequest):
        service = service_display.Display(request)
        service.disp_radar()
        res_view = service.disp_view()
        if res_view.is_ok():
            if not (res_view.data[0] is None):
                for i in range(0, len(res_view.data[0]), 1):
                    (index, pos_x, pos_y) = res_view.data[0][i]
                    dungeon_form.set_box_button(i, pos_x, pos_y)
            if not (res_view.data[1] is None):
                (pos_x, pos_y) = res_view.data[1]
                dungeon_form.set_retry_button(pos_x, pos_y)
            else:
                dungeon_form.set_retry_button(-1, -1)
        service.disp_info()
        service.disp_log()
        res_sys = service.disp_system_button()
        if res_sys.is_ok():
            if not (res_sys.data[0] is None):
                (pos_x, pos_y) = res_sys.data[0]
                dungeon_form.set_config_button(pos_x, pos_y)
            if not (res_sys.data[1] is None):
                (pos_x, pos_y) = res_sys.data[1]
                dungeon_form.set_save_button(pos_x, pos_y)
        res_act = service.disp_action_button()
        if res_act.is_ok():
            if not (res_act.data[0] is None):
                (pos_x, pos_y) = res_act.data[0]
                dungeon_form.set_action_button(ACTION.GO_UP_THE_STAIRS(), pos_x, pos_y)
            if not (res_act.data[1] is None):
                (pos_x, pos_y) = res_act.data[1]
                dungeon_form.set_action_button(ACTION.SEARCH(), pos_x, pos_y)

    @staticmethod
    def create_request_data(screen, dungeon_form: form.Form, ope_form, system_form):
        dungeon_form.search_item()
        (mouse_x, mouse_y) = ope_form.get_mouse()
        dungeon_map = dungeon_form.get_dungeon_map()
        now_pos = dungeon_form.get_now_pos()
        flash = system_form.flash
        enemy_pos_list = []
        enemy_type_list = []
        enemy_index_list = []
        count = 0
        for index in range(0, dungeon_form.ENEMY_COUNT(), 1):
            if dungeon_form.APPEAR_FLAG(index):
                enemy_pos_list.insert(count, dungeon_form.get_enemy_pos(index))
                enemy_type_list.insert(count, dungeon_form.get_enemy_type(index))
                enemy_index_list.insert(count, index)
                count += 1
        (config_x, config_y, config_width, config_height) = dungeon_form.get_config_button()
        (save_x, save_y, save_width, save_height) = dungeon_form.get_save_button()
        (retry_x, retry_y, retry_width, retry_height) = dungeon_form.get_retry_button()
        box0_item, box0_num = dungeon_form.watch_box(0)
        box1_item, box1_num = dungeon_form.watch_box(1)
        box2_item, box2_num = dungeon_form.watch_box(2)
        (box0_x, box0_y, box0_width, box0_height) = dungeon_form.get_box_button(0)
        (box1_x, box1_y, box1_width, box1_height) = dungeon_form.get_box_button(1)
        (box2_x, box2_y, box2_width, box2_height) = dungeon_form.get_box_button(2)
        (act0_x, act0_y, act0_width, act0_height) = dungeon_form.get_action_button(ACTION.GO_UP_THE_STAIRS())
        (act1_x, act1_y, act1_width, act1_height) = dungeon_form.get_action_button(ACTION.SEARCH())
        return dungeonDisplayRequest.DungeonDisplayRequest(
            screen,
            dungeon_form.img_list,
            dungeon_form.font(),
            dungeon_form.item_font(),
            dungeon_form.event_font(),
            dungeon_form.is_death(),
            map.Judge.isStairs(dungeon_map[now_pos.x][now_pos.y]),
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
            dungeon_form.get_floor(),
            dungeon_form.get_count(),
            mouse_x,
            mouse_y,
            hitJudge.hitJudgeSquare(act0_x, act0_y, act0_width, act0_height, mouse_x, mouse_y),
            hitJudge.hitJudgeSquare(act1_x, act1_y, act1_width, act1_height, mouse_x, mouse_y)
        )
