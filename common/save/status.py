import common.layer.request.saveStatusRequest as saveStatusRequest
import common.save.service.status as sub_status
import common.common as cmn
import dungeon.convert as convert
import pyd.save as SAVE

class Status:
    @staticmethod
    def execute(status_form, request):
        service = sub_status.Status(request)

        res = service.get_next_status()

        if res.is_ok():
            status_form.updateStatus(res.data)

    @staticmethod
    def create_request_data(ope_form, save_form):
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
    def updatePreStatus(save_form, status):
        save_form.set_pre_status(status)

    @staticmethod
    def updateInputData(save_form, data):
        save_form.set_input_data(data)

    @staticmethod
    def resetInputData(save_form):
        save_form.set_input_data("")

    @staticmethod
    def resetOutputData(save_form):
        save_form.set_output_data("")

    @staticmethod
    def updateDispSaveList(save_form):
        for i in (0, 2, 1):
            head = SAVE.SAVE_HEAD(i)
            tail = SAVE.SAVE_TAIL(i)
            dispData = convert.Convert.getDispData(cmn.SaveMethod().load(head, tail))
            save_form.updateSaveDispList(i, dispData)
