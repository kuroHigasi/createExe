import common.debug.debug as dbg


class Convert:
    def createInput(configForm):
        return configForm.CREATE_INPUTDATA()

    def convertOutput(configForm, data: str):
        try:
            dataList = data.split(",")
            configForm.updateNowWayKeyType(int(dataList[0]))
            configForm.updateNowGoKeyType(int(dataList[1]))
            configForm.updatePreWayKeyType()
            configForm.updatePreGoKeyType()
        except BaseException:
            dbg.ERROR_LOG("[Convert.convertOutput]OUTPUT_DATA不備")
            configForm.updateNowWayKeyType(1)
            configForm.updateNowGoKeyType(1)
            configForm.updatePreWayKeyType()
            configForm.updatePreGoKeyType()
