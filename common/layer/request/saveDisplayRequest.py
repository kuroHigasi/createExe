import dataclasses


@dataclasses.dataclass(frozen=True)
class SaveDisplayRequest:
	_screen: any
	_font: any
	_img_list: list
	_mouse_pos_x: int
	_mouse_pos_y: int
	_input_data: str
	_save_disp_list: str
	_back_button_width: int
	_back_button_height: int
	_home_button_width: int
	_home_button_height: int
	_list_width: int
	_list_height: int
	_mini_button_width: int
	_mini_button_height: int

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
	def mouse_pos_x(self):
		return self._mouse_pos_x

	@property
	def mouse_pos_y(self):
		return self._mouse_pos_y

	@property
	def input_data(self):
		return self._input_data

	@property
	def save_disp_list(self):
		return self._save_disp_list

	@property
	def back_button_width(self):
		return self._back_button_width

	@property
	def back_button_height(self):
		return self._back_button_height

	@property
	def home_button_width(self):
		return self._home_button_width

	@property
	def home_button_height(self):
		return self._home_button_height

	@property
	def list_width(self):
		return self._list_width

	@property
	def list_height(self):
		return self._list_height

	@property
	def mini_button_width(self):
		return self._mini_button_width

	@property
	def mini_button_height(self):
		return self._mini_button_height
