import common.common as cmn
import pyd.status as STATUS


class Status:
    @staticmethod
    def execute(status_form, ope_form, home_form):
        next_status = STATUS.HOME()
        left_click = ope_form.is_left_click()
        (x, y) = ope_form.get_mouse()
        (click_x, click_y) = ope_form.left_click_move_mouse()
        (start_x, start_y, start_width, start_height) = home_form.get_start_button()
        (config_x, config_y, config_width, config_height) = home_form.get_config_button()
        (exit_x, exit_y, exit_width, exit_height) = home_form.get_exit_button()
        (load_x, load_y, load_width, load_height) = home_form.get_load_button()
        if cmn.Judge.click(start_x, start_y, start_width, start_height, x, y, click_x, click_y, left_click):
            next_status = STATUS.DUNGEON()
        if cmn.Judge.click(config_x, config_y, config_width, config_height, x, y, click_x, click_y, left_click):
            next_status = STATUS.CONFIG()
        if cmn.Judge.click(exit_x, exit_y, exit_width, exit_height, x, y, click_x, click_y, left_click):
            next_status = STATUS.EXIT()
        if cmn.Judge.click(load_x, load_y, load_width, load_height, x, y, click_x, click_y, left_click):
            next_status = STATUS.SAVE()
        status_form.updateStatus(next_status)
