import dataclasses


@dataclasses.dataclass
class EndDisplayRequest:
	_screen: any
	_home_button_touch: bool
	_action_count: int
	_font: any
	_img_list: list

	@property
	def screen(self):
		return self._screen

	@property
	def home_button_touch(self):
		return self._home_button_touch

	@property
	def action_count(self):
		return self._action_count

	@property
	def font(self):
		return self._font

	@property
	def img_list(self):
		return self._img_list
