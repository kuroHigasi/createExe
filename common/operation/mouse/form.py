import dataclasses


@dataclasses.dataclass
class Form:
	_x: int
	_y: int
	_click_r: bool
	_click_l: bool
	_click_pos_x: int
	_click_pos_y: int

	def __init__(self):
		self._x = -1
		self._y = -1
		self._click_r = False
		self._click_l = False
		self._click_pos_x = -1
		self._click_pos_y = -1