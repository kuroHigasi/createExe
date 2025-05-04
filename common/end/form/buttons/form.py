import common.button.form as button_form


class Form:
    __home_button: button_form.Form

    def __init__(self):
        self.__home_button = button_form.Form(-1, -1, 200, 80)

    def set_home_button_pos(self, x, y):
        self.__home_button.x = x
        self.__home_button.y = y

    def get_home_button_pos(self):
        return (self.__home_button.x,
                self.__home_button.y)

    def get_home_button_size(self):
        return (self.__home_button.width,
                self.__home_button.height)
