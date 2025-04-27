import dataclasses

import common.button.form as button_form


@dataclasses.dataclass
class Form:
	_config_button: button_form.Form
	_start_button: button_form.Form
	_exit_button: button_form.Form
	_load_button: button_form.Form

	def __init__(self):
		self._config_button = button_form.Form(-1, -1,  200, 80)
		self._start_button = button_form.Form(-1, -1,  200, 80)
		self._exit_button = button_form.Form(-1, -1,  200, 80)
		self._load_button = button_form.Form(-1, -1,  200, 80)

	def set_config_button_pos(self, x, y):
		self._config_button.x = x
		self._config_button.y = y

	def get_config_button_pos(self):
		return self._config_button.x, self._config_button.y

	def get_config_button_size(self):
		return self._config_button.width, self._config_button.height

	def set_start_button_pos(self, x, y):
		self._start_button.x = x
		self._start_button.y = y

	def get_start_button_pos(self):
		return self._start_button.x, self._start_button.y

	def get_start_button_size(self):
		return self._start_button.width, self._start_button.height

	def set_exit_button_pos(self, x, y):
		self._exit_button.x = x
		self._exit_button.y = y

	def get_exit_button_pos(self):
		return self._exit_button.x, self._exit_button.y

	def get_exit_button_size(self):
		return self._exit_button.width, self._exit_button.height

	def set_load_button_pos(self, x, y):
		self._load_button.x = x
		self._load_button.y = y

	def get_load_button_pos(self):
		return self._load_button.x, self._load_button.y

	def get_load_button_size(self):
		return self._load_button.width, self._load_button.height
