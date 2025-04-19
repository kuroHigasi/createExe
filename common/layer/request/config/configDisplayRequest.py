import dataclasses


@dataclasses.dataclass(frozen=True)
class ConfigDisplayRequest:
	_screen: any  # screen
	_font: any  # font
	_img_list: list  # LIST
	_way1_touch: bool  # 方向キー設定0 選択状態
	_way2_touch: bool  # 方向キー設定1 選択状態
	_go1_touch: bool  # 直進キー設定0 選択状態
	_go2_touch: bool  # 直進キー設定1 選択状態
	_step1_touch: bool  # 足踏みキー設定0 選択状態
	_step2_touch: bool  # 足踏みキー設定1 選択状態
	_tab1_touch: bool  # タブ選択0 選択状態
	_tab2_touch: bool  # タブ選択1 選択状態
	_ok_touch: bool  # OK 選択状態
	_back_touch: bool  # BACK 選択状態
	_way_key_type: int  # 方向キー設定 現在状態
	_go_key_type: int  # 直進キー設定 現在状態
	_tab: int  # タブ選択 現在状態
	_volume: int  # ボリューム

	@property
	def screen(self):
		return self._screen

	@property
	def font(self):
		return self._font

	@property
	def img_list(self):
		return self._img_list

	@property
	def way1_touch(self):
		return self._way1_touch

	@property
	def way2_touch(self):
		return self._way2_touch

	@property
	def go1_touch(self):
		return self._go1_touch

	@property
	def go2_touch(self):
		return self._go2_touch

	@property
	def step1_touch(self):
		return self._step1_touch

	@property
	def step2_touch(self):
		return self._step2_touch

	@property
	def tab1_touch(self):
		return self._tab1_touch

	@property
	def tab2_touch(self):
		return self._tab2_touch

	@property
	def ok_touch(self):
		return self._ok_touch

	@property
	def back_touch(self):
		return self._back_touch

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
	def volume(self):
		return self._volume
