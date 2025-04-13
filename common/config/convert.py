import common.debug.debug as dbg


class Convert:
    @staticmethod
    def create_input(config_form):
        return config_form.create_input_data()

    @staticmethod
    def convert_output(config_form, data: str):
        try:
            data_list = data.split(",")
            config_form.set_way_key_type(int(data_list[0]))
            config_form.set_go_key_type(int(data_list[1]))
            config_form.set_volume(int(data_list[2]))
            config_form.update_pre_way_key_type()
            config_form.update_pre_go_key_type()
            config_form.update_pre_volume()
        except ValueError:
            dbg.ERROR_LOG("[Convert.convertOutput]OUTPUT_DATA不備")
            config_form.set_way_key_type(0)
            config_form.set_go_key_type(0)
            config_form.set_volume(30)
            config_form.update_pre_way_key_type()
            config_form.update_pre_go_key_type()
            config_form.update_pre_volume()
            pass
