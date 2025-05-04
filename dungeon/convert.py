import common.debug.debug as dbg
import dungeon.form.form as form


class Convert:
    @staticmethod
    def createInput(dungeon_form):
        return dungeon_form.create_input_data()

    @staticmethod
    def convertOutput(dungeon_form: form.Form, data: str):
        try:
            data_list = data.split(",")
            dungeon_form.reset(int(data_list[0]))
            dungeon_form.set_total_count(int(data_list[1]))
            dungeon_form.itemBoxClear()
            dungeon_form.log_reset()
            if int(data_list[3]) != -1:
                for i in range(0, int(data_list[4]), 1):
                    dungeon_form.item_set_box(item=int(data_list[3]), load_flag=True)
            if int(data_list[5]) != -1:
                for i in range(0, int(data_list[6]), 1):
                    dungeon_form.item_set_box(item=int(data_list[5]), load_flag=True)
            if int(data_list[7]) != -1:
                for i in range(0, int(data_list[8]), 1):
                    dungeon_form.item_set_box(item=int(data_list[7]), load_flag=True)
        except BaseException:
            dbg.ERROR_LOG("[Convert.convertOutput]OUTPUT_DATA不備")
            dungeon_form.reset(1)
            dungeon_form.set_total_count(0)
            dungeon_form.log_reset()

    def getFloor(data: str):
        try:
            data_list = data.split(",")
            return int(data_list[0])
        except BaseException:
            dbg.ERROR_LOG("[Convert.getFloor]OUTPUT_DATA不備")
            return 1

    def getDispData(data: str):
        try:
            data_list = data.split(",")
            space = " "
            for count in range(4-len(data_list[1])):
                space += " "
            return str(data_list[0]) + "F ActionCount:" + str(data_list[1]) + space + "ITEM:" + str(data_list[2])
        except BaseException:
            dbg.LOG("[Convert.getDispData]OUTPUT_DATAなし")
            return ""
