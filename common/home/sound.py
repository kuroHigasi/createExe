import common.common as cmn
import common.abstract.home.abstractSound as abstractSound
import common.layer.request.home.homeSoundRequest as homeSoundRequest
import common.home.service.sound as sub_sound
import pygame


class Sound(abstractSound.AbstractSound):
	@staticmethod
	def execute(request: homeSoundRequest.HomeSoundRequest):
		service = sub_sound.Sound(request)
		service.start()

	@staticmethod
	def create_request_data(sound_form, home_form, ope_form, config_form):
		left_click = ope_form.is_left_click()
		(x, y) = ope_form.get_mouse()
		(click_x, click_y) = ope_form.left_click_move_mouse()
		(start_x, start_y, start_width, start_height) = home_form.get_start_button()
		(config_x, config_y, config_width, config_height) = home_form.get_config_button()
		(exit_x, exit_y, exit_width, exit_height) = home_form.get_exit_button()
		(load_x, load_y, load_width, load_height) = home_form.get_load_button()
		return homeSoundRequest.HomeSoundRequest(
			cmn.Judge.click(start_x, start_y, start_width, start_height, x, y, click_x, click_y, left_click),
			cmn.Judge.click(config_x, config_y, config_width, config_height, x, y, click_x, click_y, left_click),
			cmn.Judge.click(exit_x, exit_y, exit_width, exit_height, x, y, click_x, click_y, left_click),
			cmn.Judge.click(load_x, load_y, load_width, load_height, x, y, click_x, click_y, left_click),
			sound_form.sound_list,
			config_form.get_volume()
		)
