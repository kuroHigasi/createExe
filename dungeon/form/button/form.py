import common.debug.debug as dbg
import common.button.form as button_form


ACTION_ERROR_TEXT = "存在しないACTION"


class Form:
    def __init__(self):
        self.__config_button = button_form.Form(-1, -1, 150, 60)
        self.__home_button = button_form.Form(-1, -1, 150, 60)
        self.__exit_button = button_form.Form(-1, -1, 150, 60)
        self.__save_button = button_form.Form(-1, -1, 150, 60)
        self.__retry_button = button_form.Form(-1, -1, 150, 60)
        self.__action_button = \
            [button_form.Form(-1, -1, 150, 60),
             button_form.Form(-1, -1, 150, 60)]
        self._box_button = \
            [button_form.Form(-1, -1, 60, 60),
             button_form.Form(-1, -1, 60, 60),
             button_form.Form(-1, -1, 60, 60)]

    def set_config_button_pos(self, x, y):
        self.__config_button.x = x
        self.__config_button.y = y

    def get_config_button_pos(self):
        return (self.__config_button.x,
                self.__config_button.y)

    def get_config_button_size(self):
        return (self.__config_button.width,
                self.__config_button.height)

    def set_home_button_pos(self, x, y):
        self.__home_button.x = x
        self.__home_button.y = y

    def get_home_button_pos(self):
        return (self.__home_button.x,
                self.__home_button.y)

    def get_home_button_size(self):
        return (self.__home_button.width,
                self.__home_button.height)

    def set_exit_button_pos(self, x, y):
        self.__exit_button.x = x
        self.__exit_button.y = y

    def get_exit_button_pos(self):
        return (self.__exit_button.x,
                self.__exit_button.y)

    def get_exit_button_size(self):
        return (self.__exit_button.width,
                self.__exit_button.height)

    def set_save_button_pos(self, x, y):
        self.__save_button.x = x
        self.__save_button.y = y

    def get_save_button_pos(self):
        return (self.__save_button.x,
                self.__save_button.y)

    def get_save_button_size(self):
        return (self.__save_button.width,
                self.__save_button.height)

    def set_retry_button_pos(self, x, y):
        self.__retry_button.x = x
        self.__retry_button.y = y

    def get_retry_button_pos(self):
        return (self.__retry_button.x,
                self.__retry_button.y)

    def get_retry_button_size(self):
        return (self.__retry_button.width,
                self.__retry_button.height)

    def set_action_button_pos(self, index, x, y):
        if index < len(self.__action_button):
            self.__action_button[index].x = x
            self.__action_button[index].y = y
        else:
            dbg.ERROR_LOG(ACTION_ERROR_TEXT)

    def get_action_button_pos(self, index):
        if index < len(self.__action_button):
            return (self.__action_button[index].x,
                    self.__action_button[index].y)
        else:
            dbg.ERROR_LOG(ACTION_ERROR_TEXT)
            return -1, -1

    def get_action_button_size(self, index):
        if index < len(self.__action_button):
            return (self.__action_button[index].width,
                    self.__action_button[index].height)
        else:
            dbg.ERROR_LOG(ACTION_ERROR_TEXT)
            return 150, 60

    def set_box_button_pos(self, index, x, y):
        if 0 <= index < 3:
            self._box_button[index].x = x
            self._box_button[index].y = y
        else:
            self._box_button[index].x = -1
            self._box_button[index].y = -1

    def get_box_button_pos(self, index):
        if 0 <= index < 3:
            return (self._box_button[index].x,
                    self._box_button[index].y)
        else:
            return -1, -1

    def get_box_button_size(self, index):
        if 0 <= index < 3:
            return (self._box_button[index].width,
                    self._box_button[index].height)
        else:
            return 60, 60
