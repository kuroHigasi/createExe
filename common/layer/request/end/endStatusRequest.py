import dataclasses


@dataclasses.dataclass
class EndStatusRequest:
	_home_button_click: bool

	@property
	def home_button_click(self):
		return self._home_button_click
