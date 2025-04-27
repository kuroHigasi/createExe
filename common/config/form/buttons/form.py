import dataclasses

import common.button.form as button_form


@dataclasses.dataclass
class Form:
	_ok_button: button_form
	_back_button: button_form
	_way_button_list: list
	_go_button_list: list
	_step_button_list: list
	_tab_list: list
	_volume_slider: button_form
	_test_button: button_form.Form

	def __init__(self):
		# OK BUTTON
		self._ok_button = button_form.Form(-1, -1, 200, 80)
		# BACK BUTTON
		self._back_button = button_form.Form(-1, -1, 200, 80)
		# WAY BUTTON(方向キー入力タイプ選択)
		self._way_button_list = \
			[button_form.Form(-1, -1, 200, 80), button_form.Form(-1, -1, 200, 80)]
		# GO BUTTON(前進キー入力タイプ選択)
		self._go_button_list = \
			[button_form.Form(-1, -1, 200, 80), button_form.Form(-1, -1, 200, 80)]
		# STEP BUTTON(足踏みキー入力タイプ選択)
		self._step_button_list = \
			[button_form.Form(-1, -1, 200, 80), button_form.Form(-1, -1, 200, 80)]
		# TAB
		self._tab_list = \
			[button_form.Form(-1, -1, 250, 25), button_form.Form(-1, -1, 250, 25)]
		# VOLUME_SLIDER
		self._volume_slider = button_form.Form(-1, -1, 400, 30)
		# TEST BUTTON
		self._test_button = button_form.Form(-1, -1, 200, 80)

	def set_ok_button_pos(self, x, y):
		self._ok_button.x = x
		self._ok_button.y = y

	def get_ok_button_pos(self):
		return self._ok_button.x, self._ok_button.y

	def get_ok_button_size(self):
		return self._ok_button.width, self._ok_button.height

	def set_back_button_pos(self, x, y):
		self._back_button.x = x
		self._back_button.y = y

	def get_back_button_pos(self):
		return self._back_button.x, self._back_button.y

	def get_back_button_size(self):
		return self._back_button.width, self._back_button.height

	def set_way_button_pos(self, index, x, y):
		self._way_button_list[index].x = x
		self._way_button_list[index].y = y

	def get_way_button_pos(self, index):
		return self._way_button_list[index].x, self._way_button_list[index].y

	def get_way_button_size(self, index):
		return self._way_button_list[index].width, self._way_button_list[index].height

	def set_go_button_pos(self, index, x, y):
		self._go_button_list[index].x = x
		self._go_button_list[index].y = y

	def get_go_button_pos(self, index):
		return self._go_button_list[index].x, self._go_button_list[index].y

	def get_go_button_size(self, index):
		return self._go_button_list[index].width, self._go_button_list[index].height

	def set_step_button_pos(self, index, x, y):
		self._step_button_list[index].x = x
		self._step_button_list[index].y = y

	def get_step_button_pos(self, index):
		return self._step_button_list[index].x, self._step_button_list[index].y

	def get_step_button_size(self, index):
		return self._step_button_list[index].width, self._step_button_list[index].height

	def set_tab_button_pos(self, index, x, y):
		self._tab_list[index].x = x
		self._tab_list[index].y = y

	def get_tab_button_pos(self, index):
		return self._tab_list[index].x, self._tab_list[index].y

	def get_tab_button_size(self, index):
		return self._tab_list[index].width, self._tab_list[index].height

	def set_volume_slider_pos(self, x, y):
		self._volume_slider.x = x
		self._volume_slider.y = y

	def get_volume_slider_pos(self):
		return self._volume_slider.x, self._volume_slider.y

	def get_volume_slider_size(self):
		return self._volume_slider.width, self._volume_slider.height

	def set_test_button_pos(self, x, y):
		self._test_button.x = x
		self._test_button.y = y

	def get_test_button_pos(self):
		return self._test_button.x, self._test_button.y

	def get_test_button_size(self):
		return self._test_button.width, self._test_button.height
