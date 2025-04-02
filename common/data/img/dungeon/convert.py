import common.debug.debug as dbg


class Convert:
    def createInput(dungeonForm):
        return dungeonForm.CREATE_INPUTDATA()

    def convertOutput(dungeonForm, data: str):
        try:
            dataList = data.split(",")
            dungeonForm.reset(int(dataList[0]))
            dungeonForm.updateTotalCount(int(dataList[1]))
            dungeonForm.itemBoxClear()
            dungeonForm.resetLog()
            if (int(dataList[3]) != -1):
                for i in range(0, int(dataList[4]), 1):
                    dungeonForm.itemSetBox(int(dataList[3]))
            if (int(dataList[5]) != -1):
                for i in range(0, int(dataList[6]), 1):
                    dungeonForm.itemSetBox(int(dataList[5]))
            if (int(dataList[7]) != -1):
                for i in range(0, int(dataList[8]), 1):
                    dungeonForm.itemSetBox(int(dataList[7]))
        except BaseException:
            dbg.ERROR_LOG("[Convert.convertOutput]OUTPUT_DATA不備")
            dungeonForm.reset(1)
            dungeonForm.updateTotalCount(0)
            dungeonForm.resetLog()

    def getFloor(data: str):
        try:
            dataList = data.split(",")
            return int(dataList[0])
        except BaseException:
            dbg.ERROR_LOG("[Convert.getFloor]OUTPUT_DATA不備")
            return 1

    def getDispData(data: str):
        try:
            dataList = data.split(",")
            space = " "
            for count in range(4-len(dataList[1])):
                space += " "
            return str(dataList[0]) + "F ActionCount:" + str(dataList[1]) + space + "ITEM:" + str(dataList[2])
        except BaseException:
            dbg.LOG("[Convert.getDispData]OUTPUT_DATAなし")
            return ""
