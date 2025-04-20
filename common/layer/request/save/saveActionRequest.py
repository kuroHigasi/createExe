import dataclasses


@dataclasses.dataclass(frozen=True)
class SaveActionRequest:
	_save1_click: bool
	_save2_click: bool
	_save3_click: bool
	_load1_click: bool
	_load2_click: bool
	_load3_click: bool
	_delete1_click: bool
	_delete2_click: bool
	_delete3_click: bool
	_input_data: str

	@property
	def save1_click(self):
		return self._save1_click

	@property
	def save2_click(self):
		return self._save2_click

	@property
	def save3_click(self):
		return self._save3_click

	@property
	def load1_click(self):
		return self._load1_click

	@property
	def load2_click(self):
		return self._load2_click

	@property
	def load3_click(self):
		return self._load3_click

	@property
	def delete1_click(self):
		return self._delete1_click

	@property
	def delete2_click(self):
		return self._delete2_click

	@property
	def delete3_click(self):
		return self._delete3_click

	@property
	def input_data(self):
		return self._input_data
