import common.layer.request.save.saveStatusRequest as saveStatusRequest
import common.save.service.status as sub_status
import common.abstract.save.abstractStatus as abstractStatus
import common.common as cmn
import common.debug.debug as dbg
import dungeon.convert as convert
import pyd.save as SAVE

class Status(abstractStatus.AbstractStatus):
    @staticmethod
    def execute(status_form, request):
        service = sub_status.Status(request)

        res = service.get_next_status()

        if res.is_ok():
            status_form.update_status(res.data)

    @staticmethod
    def create_request_data(save_form, ope_form):
        left_click = ope_form.is_left_click()
        (x, y) = ope_form.get_mouse()
        (click_x, click_y) = ope_form.left_click_move_mouse()
        (back_x, back_y, back_width, back_height) = save_form.get_back_button()
        (home_x, home_y, home_width, home_height) = save_form.get_home_button()
        cmn.Judge.click(back_x, back_y, back_width, back_height, x, y, click_x, click_y, left_click)
        cmn.Judge.click(home_x, home_y, home_width, home_height, x, y, click_x, click_y, left_click)
        return saveStatusRequest.SaveStatusRequest(
            cmn.Judge.click(back_x, back_y, back_width, back_height, x, y, click_x, click_y, left_click),
            cmn.Judge.click(home_x, home_y, home_width, home_height, x, y, click_x, click_y, left_click),
            save_form.get_pre_status(),
            save_form.OUTPUT_DATA()
        )

    @staticmethod
    def initialize(save_form, pre_status):
        save_form.set_pre_status(pre_status)
        save_form.set_output_data("")
        for i in (0, 2, 1):
            head = SAVE.SAVE_HEAD(i)
            tail = SAVE.SAVE_TAIL(i)
            disp_data = convert.Convert.getDispData(cmn.SaveMethod().load(head, tail))
            save_form.updateSaveDispList(i, disp_data)

    @staticmethod
    def update_input_data(save_form, dungeon_form):
        input_data = convert.Convert.createInput(dungeon_form)
        dbg.LOG("INPUT_DATA SET[" + input_data + "]")
        save_form.set_input_data(input_data)

    @staticmethod
    def reset_input_data(save_form):
        dbg.LOG("INPUT_DATA RESET")
        save_form.set_input_data("")
