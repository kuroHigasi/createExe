import dungeon.abstract.abstractStatus as abstractStatus
import dungeon.layer.request.dungeonStatusRequest as dungeonStatusRequest
import dungeon.service.status as sub_status
import common.common as cmn
import dungeon.convert as convert


class Status(abstractStatus.AbstractStatus):
    @staticmethod
    def execute(status_form, request):
        service = sub_status.Status(request)

        res_status = service.get_next_status()
        if res_status.is_ok() or res_status.is_do_nothing():
            next_status = res_status.data
            status_form.update_status(next_status)


    @staticmethod
    def create_request_data(dungeon_form, ope_form):
        left_click = ope_form.is_left_click()
        (x, y) = ope_form.get_mouse()
        (clickX, clickY) = ope_form.left_click_move_mouse()
        (configX, configY, configSizeW, configSizeH) = dungeon_form.CONFIG_BUTTON()
        (saveX, saveY, saveSizeW, saveSizeH) = dungeon_form.SAVE_BUTTON()
        return dungeonStatusRequest.DungeonStatusRequest(
            cmn.Judge.click(configX, configY, configSizeW, configSizeH, x, y, clickX, clickY, left_click),
            cmn.Judge.click(saveX, saveY, saveSizeW, saveSizeH, x, y, clickX, clickY, left_click),
            dungeon_form.END_FLAG()
        )

    def updateLog(dungeonForm):
        if dungeonForm.UPDATE_LOG_FLAG():
            dungeonForm.updateLog()
            dungeonForm.logFlagOff()

    def fromHomeReset(dungeonForm):
        dungeonForm.reset(1)
        dungeonForm.updateTotalCount(0)
        dungeonForm.resetLog()
        dungeonForm.itemBoxClear()

    def fromSaveConvert(dungeonForm, data: str):
        if (data != ""):
            convert.Convert.convertOutput(dungeonForm, data)
