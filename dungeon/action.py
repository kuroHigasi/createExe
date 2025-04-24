import common.common as cmn
import dungeon.abstract.abstractAction as abstractAction
import dungeon.service.action as sub_action
import dungeon.layer.request.dungeonActionRequest as dungeonActionRequest
import dungeon.form.form as main_form
import pyd.typeAction as ACTION
import pyd.typeEnemy as ENEMY_TYPE


class Action(abstractAction.AbstractAction):
    @staticmethod
    def execute(dungeon_form: main_form.Form, ope_form, request: dungeonActionRequest.DungeonActionRequest):
        service = sub_action.Action(request)
        # MOVE
        service.action_move(dungeon_form, ope_form)
        # UPDATE FLAG (LOG FLAG)
        now_pos = dungeon_form.NOW_POS()
        is_diff_way = dungeon_form.existDiffWay()
        is_diff_view = dungeon_form.existDiffView()
        is_diff_pos = dungeon_form.existDiffPos()
        is_diff = (is_diff_way | is_diff_pos | is_diff_view)
        act_flag = dungeon_form.ACTION_FLAG()
        res_log = service.judge_log_flag(now_pos, is_diff, is_diff_way, act_flag)
        if res_log.is_ok() and res_log.data:
            dungeon_form.logFlagOn()
        # UPDATE FLAG (BOX FLAG)
        res_box = service.judge_item_box_flag(is_diff)
        if res_box.is_ok():
            if res_box.data:
                dungeon_form.itemBoxFlagOn()
        # USE ITEM BOX
        res_item = service.box_button_click()
        if res_item.is_ok():
            dungeon_form.itemBoxUse(res_item.data)
        # ENEMY ACTION(MOVE)
        pre_enemy_pos_list = []
        for index in range(0, dungeon_form.ENEMY_COUNT(), 1):
            pre_enemy_pos_list.insert(index, dungeon_form.ENEMIS_POS(index))
        res_enemy_move = service.action_enemy_move()
        if res_enemy_move.is_ok():
            dungeon_form.enemyMove()
        # ENEMY ACTION(TOUCH)
        pre_pos = dungeon_form.PRE_POS()
        enemy_pos_list = []
        for index in range(0, dungeon_form.ENEMY_COUNT(), 1):
            enemy_pos_list.insert(index, dungeon_form.ENEMIS_POS(index))
        res_enemy_touch = service.judge_enemy_touch(now_pos, pre_pos, enemy_pos_list, pre_enemy_pos_list)
        if res_enemy_touch.is_ok():
            index = res_enemy_touch.data
            enemy_type = dungeon_form.ENEMIS_TYPE(index)
            dungeon_form.disappearanceEnemy(index)
            if enemy_type == ENEMY_TYPE.DANGER():
                dungeon_form.death()
        # BUTTON CLICK(ACTION)
        res_act_click = service.action_button_click()
        if res_act_click.is_ok():
            next_flag, search_flag = res_act_click.data
            if next_flag:
                if dungeon_form.reset(dungeon_form.FLOOR()+1):
                    dungeon_form.reset(1)
                    dungeon_form.onEndFlag()
                else:
                    dungeon_form.itemBoxPreUpdate()
                dungeon_form.resetActionButton(ACTION.GO_UP_THE_STAIRS())
            if search_flag:
                if dungeon_form.ITEM_GET_FLAG():
                    if dungeon_form.itemIntoBox():
                        dungeon_form.itemFlagOff()
                        dungeon_form.eventFlagOff()
                dungeon_form.resetActionButton(ACTION.SEARCH())
        # BUTTON CLICK(RETRY)
        res_retry_click = service.retry_button_click()
        if res_retry_click.is_ok():
            dungeon_form.reset(dungeon_form.FLOOR())
            dungeon_form.resetActionButton(ACTION.GO_UP_THE_STAIRS())

    @staticmethod
    def create_request_data(dungeon_form: main_form.Form, ope_form, config_form):
        go_key_type = config_form.get_go_key_type()
        space = ope_form.get_space()
        enter = ope_form.get_enter()
        start_pos = dungeon_form.START_POS()
        (x, y) = ope_form.get_mouse()
        (click_x, click_y) = ope_form.left_click_move_mouse()
        left_click = ope_form.is_left_click()
        (act0_x, act0_y, act0_width, act0_height) = dungeon_form.ACTION_BUTTON(0)
        (act1_x, act1_y, act1_width, act1_height) = dungeon_form.ACTION_BUTTON(1)
        (retry_x, retry_y, retry_width, retry_height) = dungeon_form.RETRY_BUTTON()
        (box0_x, box0_y, box0_width, box0_height) = dungeon_form.BOX_BUTTON(0)
        (box1_x, box1_y, box1_width, box1_height) = dungeon_form.BOX_BUTTON(1)
        (box2_x, box2_y, box2_width, box2_height) = dungeon_form.BOX_BUTTON(2)
        return dungeonActionRequest.DungeonActionRequest(
            dungeon_form.IS_DEATH(),
            (space and go_key_type == 0) or (enter and go_key_type == 1),
            (space and go_key_type == 1) or (enter and go_key_type == 0),
            dungeon_form.UPDATE_LOG_FLAG(),
            dungeon_form.BOX_FLAG(),
            start_pos[0],
            start_pos[1],
            dungeon_form.ENEMY_COUNT(),
            cmn.Judge.click(act0_x, act0_y, act0_width, act0_height, x, y, click_x, click_y, left_click),
            cmn.Judge.click(act1_x, act1_y, act1_width, act1_height, x, y, click_x, click_y, left_click),
            cmn.Judge.click(retry_x, retry_y, retry_width, retry_height, x, y, click_x, click_y, left_click),
            cmn.Judge.click(box0_x, box0_y, box0_width, box0_height, x, y, click_x, click_y, left_click),
            cmn.Judge.click(box1_x, box1_y, box1_width, box1_height, x, y, click_x, click_y, left_click),
            cmn.Judge.click(box2_x, box2_y, box2_width, box2_height, x, y, click_x, click_y, left_click)
        )
