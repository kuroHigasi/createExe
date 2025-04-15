import common.layer.request.saveActionRequest as saveActionRequest
import common.save.service.action as sub_action
import common.common as cmn
# ゲーム毎
import dungeon.convert as convert_dungeon
# ゲーム毎


class Action:
    @staticmethod
    def execute(save_form, request):
        service = sub_action.Action(request)
        # SAVE
        for index in (0, 2, 1):
            res_save = service.save(index, convert_dungeon.Convert.getDispData)
            if res_save.is_ok():
                save_form.updateSaveDispList(index, res_save.data)
        # LOAD
        for index in (0, 2, 1):
            res_load = service.load(index)
            if res_load.is_ok():
                save_form.updateOutputData(res_load.data)
        # DELETE
        for index in (0, 2, 1):
            res_delete = service.delete(index, convert_dungeon.Convert.getDispData)
            if res_delete.is_ok():
                save_form.updateSaveDispList(index, res_delete.data)

    @staticmethod
    def create_request_data(save_form, ope_form):
        left_click = ope_form.is_left_click()
        x, y = ope_form.get_mouse()
        click_x, click_y = ope_form.left_click_move_mouse()
        save1_x, save1_y, save1_width, save1_height = save_form.get_save_list(0)
        save2_x, save2_y, save2_width, save2_height = save_form.get_save_list(1)
        save3_x, save3_y, save3_width, save3_height = save_form.get_save_list(2)
        save1_click = cmn.Judge.click(save1_x, save1_y, save1_width, save1_height, x, y, click_x, click_y , left_click)
        save2_click = cmn.Judge.click(save2_x, save2_y, save2_width, save2_height, x, y, click_x, click_y , left_click)
        save3_click = cmn.Judge.click(save3_x, save3_y, save3_width, save3_height, x, y, click_x, click_y , left_click)
        load1_x, load1_y, load1_width, load1_height = save_form.get_load_list(0)
        load2_x, load2_y, load2_width, load2_height = save_form.get_load_list(1)
        load3_x, load3_y, load3_width, load3_height = save_form.get_load_list(2)
        load1_click = cmn.Judge.click(load1_x, load1_y, load1_width, load1_height, x, y, click_x, click_y , left_click)
        load2_click = cmn.Judge.click(load2_x, load2_y, load2_width, load2_height, x, y, click_x, click_y , left_click)
        load3_click = cmn.Judge.click(load3_x, load3_y, load3_width, load3_height, x, y, click_x, click_y , left_click)
        delete1_x, delete1_y, delete1_width, delete1_height = save_form.get_delete_list(0)
        delete2_x, delete2_y, delete2_width, delete2_height = save_form.get_delete_list(1)
        delete3_x, delete3_y, delete3_width, delete3_height = save_form.get_delete_list(2)
        delete1_click = (
            cmn.Judge.click(delete1_x, delete1_y, delete1_width, delete1_height, x, y, click_x, click_y , left_click))
        delete2_click = (
            cmn.Judge.click(delete2_x, delete2_y, delete2_width, delete2_height, x, y, click_x, click_y , left_click))
        delete3_click = (
            cmn.Judge.click(delete3_x, delete3_y, delete3_width, delete3_height, x, y, click_x, click_y , left_click))
        input_data = save_form.INPUT_DATA()
        return \
            saveActionRequest.SaveActionRequest(
                save1_click,  # SAVE1 クリック
                save2_click,  # SAVE2 クリック
                save3_click,  # SAVE3 クリック
                load1_click,  # LOAD1 クリック
                load2_click,  # LOAD2 クリック
                load3_click,  # LOAD3 クリック
                delete1_click,  # DELETE1 クリック
                delete2_click,  # DELETE2 クリック
                delete3_click,  # DELETE3 クリック
                input_data  # INPUT_DATA クリック
            )
