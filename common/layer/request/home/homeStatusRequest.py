import dataclasses


@dataclasses.dataclass
class HomeStatusRequest:
	_start_click: bool
	_config_click: bool
	_exit_click: bool
	_load_click: bool

	@property
	def start_click(self):
		return self._start_click

	@property
	def config_click(self):
		return self._config_click

	@property
	def exit_click(self):
		return self._exit_click

	@property
	def load_click(self):
		return self._load_click
