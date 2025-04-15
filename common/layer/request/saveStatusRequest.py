import dataclasses


@dataclasses.dataclass
class SaveStatusRequest:
	_back_button_click: bool
	_home_button_click: bool
	_pre_status: int
	_output_data: str

	@property
	def back_button_click(self):
		return self._back_button_click

	@property
	def home_button_click(self):
		return self._home_button_click

	@property
	def pre_status(self):
		return self._pre_status

	@property
	def output_data(self):
		return self._output_data
