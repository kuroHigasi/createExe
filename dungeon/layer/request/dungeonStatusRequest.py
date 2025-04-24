import dataclasses


@dataclasses.dataclass
class DungeonStatusRequest:
	_config_button_click: bool
	_save_button_click: bool
	_end_flag: bool

	@property
	def config_button_click(self):
		return self._config_button_click

	@property
	def save_button_click(self):
		return self._save_button_click

	@property
	def end_flag(self):
		return self._end_flag
