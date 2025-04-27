import dataclasses


@dataclasses.dataclass(frozen=True)
class ConfigActionRequest:
	_click_pos_x: int  # マウス位置 X
	_click_l_pos_x: int  # クリック マウス位置 X
	_click_l_pos_y: int  # クリック マウス位置 Y
	_way1_click: bool  # 方向キー設定0 選択状態
	_way2_click: bool  # 方向キー設定1 選択状態
	_go1_click: bool  # 直進キー設定0 選択状態
	_go2_click: bool  # 直進キー設定1 選択状態
	_step1_click: bool  # 足踏みキー設定0 選択状態
	_step2_click: bool  # 足踏みキー設定1 選択状態
	_tab1_click: bool  # タブ選択0 選択状態
	_tab2_click: bool  # タブ選択1 選択状態
	_test_click: bool  # テスト選択 選択状態
	_way_key_type: int  # 方向キー設定 現在状態
	_go_key_type: int  # 直進キー設定 現在状態
	_tab: int  # タブ選択 現在状態
	_slider_click: bool  # タブ選択 現在状態

	@property
	def click_pos_x(self):
		return self._click_pos_x

	@property
	def click_l_pos_x(self):
		return self._click_l_pos_x

	@property
	def click_l_pos_y(self):
		return self._click_l_pos_y

	@property
	def way1_click(self):
		return self._way1_click

	@property
	def way2_click(self):
		return self._way2_click

	@property
	def go1_click(self):
		return self._go1_click

	@property
	def go2_click(self):
		return self._go2_click

	@property
	def step1_click(self):
		return self._step1_click

	@property
	def step2_click(self):
		return self._step2_click

	@property
	def tab1_click(self):
		return self._tab1_click

	@property
	def tab2_click(self):
		return self._tab2_click

	@property
	def test_click(self):
		return self._test_click

	@property
	def way_key_type(self):
		return self._way_key_type

	@property
	def go_key_type(self):
		return self._go_key_type

	@property
	def tab(self):
		return self._tab

	@property
	def slider_click(self):
		return self._slider_click
