import dataclasses


@dataclasses.dataclass
class Form:
	_x: int
	_y: int
	_width: int
	_height: int

	def __init__(self, x, y, width, height):
		self._x = x
		self._y = y
		self._width = width
		self._height = height

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, x):
		self._x = x

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, y):
		self._y = y

	@property
	def width(self):
		return self._width

	@property
	def height(self):
		return self._height
