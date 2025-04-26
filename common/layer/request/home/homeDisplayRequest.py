import dataclasses


@dataclasses.dataclass
class HomeSoundRequest:
	_start_touch: bool
	_config_touch: bool
	_exit_touch: bool
	_load_touch: bool
	_img_list: list
	_screen: any

	@property
	def start_touch(self):
		return self._start_touch

	@property
	def config_touch(self):
		return self._config_touch

	@property
	def exit_touch(self):
		return self._exit_touch

	@property
	def load_touch(self):
		return self._load_touch

	@property
	def img_list(self):
		return self._img_list

	@property
	def screen(self):
		return self._screen
