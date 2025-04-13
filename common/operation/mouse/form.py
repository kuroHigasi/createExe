import dataclasses


@dataclasses.dataclass
class Form:
	_mouse_pointer_x: int
	_mouse_pointer_y: int
	_click_r: bool
	_click_l: bool
	_click_r_pos_x: int
	_click_r_pos_y: int
	_click_l_pos_x: int
	_click_l_pos_y: int

	def __init__(self):
		self._mouse_pointer_x = -1
		self._mouse_pointer_y = -1
		self._click_r = False
		self._click_l = False
		self._click_r_pos_x = -1
		self._click_r_pos_y = -1
		self._click_l_pos_x = -1
		self._click_l_pos_y = -1

	@property
	def mouse_pointer_x(self):
		return self._mouse_pointer_x

	@mouse_pointer_x.setter
	def mouse_pointer_x(self, pointer_x):
		if -1 <= pointer_x:
			self._mouse_pointer_x = pointer_x

	@property
	def mouse_pointer_y(self):
		return self._mouse_pointer_y

	@mouse_pointer_y.setter
	def mouse_pointer_y(self, pointer_y):
		if -1 <= pointer_y:
			self._mouse_pointer_y = pointer_y

	def get_mouse_pointer(self):
		return self._mouse_pointer_x, self._mouse_pointer_y

	@property
	def click_r(self):
		return self._click_r

	@click_r.setter
	def click_r(self, click):
		self._click_r = click

	@property
	def click_l(self):
		return self._click_l

	@click_l.setter
	def click_l(self, click):
		self._click_l = click

	@property
	def click_r_pos_x(self):
		return self._click_r_pos_x

	@click_r_pos_x.setter
	def click_r_pos_x(self, pointer_x):
		if -1 <= pointer_x:
			self._click_r_pos_x = pointer_x

	@property
	def click_r_pos_y(self):
		return self._click_r_pos_y

	@click_r_pos_y.setter
	def click_r_pos_y(self, pointer_y):
		if -1 <= pointer_y:
			self._click_r_pos_y = pointer_y

	def get_click_r_pos(self):
		return self._click_r_pos_x, self._click_r_pos_y

	@property
	def click_l_pos_x(self):
		return self._click_l_pos_x

	@click_l_pos_x.setter
	def click_l_pos_x(self, pointer_x):
		if -1 <= pointer_x:
			self._click_l_pos_x = pointer_x

	@property
	def click_l_pos_y(self):
		return self._click_l_pos_y

	@click_l_pos_y.setter
	def click_l_pos_y(self, pointer_y):
		if -1 <= pointer_y:
			self._click_l_pos_y = pointer_y

	def get_click_l_pos(self):
		return self._click_l_pos_x, self._click_l_pos_y

	def reset(self):
		self._click_r = False
		self._click_l = False
		self._click_r_pos_x = -1
		self._click_r_pos_y = -1
		self._click_l_pos_x = -1
		self._click_l_pos_y = -1