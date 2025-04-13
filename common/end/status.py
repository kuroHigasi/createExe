import common.common as cmn
import pyd.status as STATUS


class Status:
    def nextStatus(statusForm, opeForm, endForm):
        nextStatus = STATUS.END()
        (x, y) = opeForm.MOUSE()
        (clickX, clickY) = opeForm.leftClickMoveMouse()
        (homeX, homeY, homeSizeW, homeSizeH) = endForm.HOME_BUTTON()
        if (cmn.Judge.click(homeX, homeY, homeSizeW, homeSizeH, x, y, clickX, clickY, opeForm.isLeftClick())):
            nextStatus = STATUS.HOME()
        statusForm.updateStatus(nextStatus)
