import dataclasses


@dataclasses.dataclass
class Repeat:
	_flag_list: list
	_num: int

	def __init__(self, num):
		self._flag_list = []
		for index in range(num):
			self._flag_list.insert(index, False)
		self._num = num

	def set_flag(self, index, flag):
		if -1 < index < self._num:
			self._flag_list[index] = flag

	def get_flag(self, index):
		if -1 < index < self._num:
			return self._flag_list[index]
