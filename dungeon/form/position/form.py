import dataclasses


@dataclasses.dataclass
class Form:
	_x: int
	_y: int

	def __init__(self, x=0, y=0):
		self._x = x
		self._y = y

	@property
	def x(self):
		return self._x

	@x.setter
	def x(self, pos_x):
		if -1 < pos_x:
			self._x = pos_x

	@property
	def y(self):
		return self._y

	@y.setter
	def y(self, pos_y):
		if -1 < pos_y:
			self._y = pos_y

	def __eq__(self, other):
		if other is None or not(isinstance(other, Form)):
			return False
		return self.x == other.x and self.y == other.y
