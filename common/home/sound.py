import common.common as cmn
import pygame


class Sound:
	@staticmethod
	def start(home_form, ope_form, config_form, sound_form):
		sound_list = sound_form.sound_list
		left_click = ope_form.is_left_click()
		(x, y) = ope_form.get_mouse()
		(click_x, click_y) = ope_form.left_click_move_mouse()
		(start_x, start_y, start_width, start_height) = home_form.get_start_button()
		(config_x, config_y, config_width, config_height) = home_form.get_config_button()
		(exit_x, exit_y, exit_width, exit_height) = home_form.get_exit_button()
		(load_x, load_y, load_width, load_height) = home_form.get_load_button()
		if cmn.Judge.click(start_x, start_y, start_width, start_height, x, y, click_x, click_y, left_click):
			pygame.mixer.music.load(sound_list[0])
			pygame.mixer.music.set_volume(config_form.get_volume()/100)
			pygame.mixer.music.play()
		if cmn.Judge.click(config_x, config_y, config_width, config_height, x, y, click_x, click_y, left_click):
			pygame.mixer.music.load(sound_list[0])
			pygame.mixer.music.set_volume(config_form.get_volume()/100)
			pygame.mixer.music.play()
		if cmn.Judge.click(exit_x, exit_y, exit_width, exit_height, x, y, click_x, click_y, left_click):
			pygame.mixer.music.load(sound_list[0])
			pygame.mixer.music.set_volume(config_form.get_volume()/100)
			pygame.mixer.music.play()
		if cmn.Judge.click(load_x, load_y, load_width, load_height, x, y, click_x, click_y, left_click):
			pygame.mixer.music.load(sound_list[0])
			pygame.mixer.music.set_volume(config_form.get_volume()/100)
			pygame.mixer.music.play()
