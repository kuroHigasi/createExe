import dataclasses


@dataclasses.dataclass(frozen=True)
class ConfigDisplayRequest:
	_ok_click: bool  # OK 選択状態
	_back_click: bool  # BACK 選択状態
	_input_data: str  # INPUT DATA
	_pre_status: int  # 前ステータス

	@property
	def ok_click(self):
		return self._ok_click

	@property
	def back_click(self):
		return self._back_click

	@property
	def input_data(self):
		return self._input_data

	@property
	def pre_status(self):
		return self._pre_status
