import dataclasses


@dataclasses.dataclass
class Form:
	__direction_key: int
	__space: bool
	__enter: bool

	def __init__(self):
		self.__direction_key = 0b0000
		self.__space = False
		self.__enter = False

	@property
	def direction_key(self):
		return self.__direction_key

	@direction_key.setter
	def direction_key(self, key):
		self.__direction_key = key

	@property
	def space(self):
		return self.__space

	@space.setter
	def space(self, click):
		self.__space = click

	@property
	def enter(self):
		return self.__enter

	@enter.setter
	def enter(self, click):
		self.__enter = click
