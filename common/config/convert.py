import common.debug.debug as dbg


class Convert:
    def createInput(config_form):
        return config_form.create_input_data()

    def convertOutput(config_form, data: str):
        try:
            dataList = data.split(",")
            config_form.way_key_type = int(dataList[0])
            config_form.go_key_type = int(dataList[1])
            config_form.volume = int(dataList[2])
            config_form.update_pre_way_key_type()
            config_form.update_pre_go_key_type()
            config_form.update_pre_volume()
        except BaseException:
            dbg.ERROR_LOG("[Convert.convertOutput]OUTPUT_DATA不備")
            config_form.way_key_type = 1
            config_form.go_key_type = 1
            config_form.volume = 30
            config_form.update_pre_way_key_type()
            config_form.update_pre_go_key_type()
            config_form.update_pre_volume()
