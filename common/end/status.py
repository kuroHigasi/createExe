import common.common as cmn
import pyd.status as STATUS


class Status:
    def nextStatus(statusForm, opeForm, endForm):
        nextStatus = STATUS.END()
        (x, y) = opeForm.get_mouse()
        (clickX, clickY) = opeForm.left_click_move_mouse()
        (homeX, homeY, homeSizeW, homeSizeH) = endForm.HOME_BUTTON()
        if (cmn.Judge.click(homeX, homeY, homeSizeW, homeSizeH, x, y, clickX, clickY, opeForm.is_left_click())):
            nextStatus = STATUS.HOME()
        statusForm.update_status(nextStatus)
