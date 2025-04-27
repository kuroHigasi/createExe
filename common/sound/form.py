import dataclasses
import common.download as download
import common.sound.repeat.repeat as repeat


@dataclasses.dataclass
class Form:
	_sound_list: list
	_chanel_list: list
	_chanel_num: int
	_chanel_max: int
	_repeat_save: repeat.Repeat

	def __init__(self):
		self._sound_list = download.Download.sound()
		self._repeat_save = repeat.Repeat(9)
		self._chanel_list = [None, None, None]
		self._chanel_max = len(self._chanel_list)
		self._chanel_num = 0

	@property
	def sound_list(self):
		return self._sound_list

	def judge_repeat(self, index, touch):
		if self._repeat_save.get_flag(index) != touch:
			self._repeat_save.set_flag(index, touch)
			return touch
		return False

	def set_chanel(self, chanel):
		if self._chanel_num < self._chanel_max:
			self._chanel_list[self._chanel_num] = chanel
			self._chanel_num += 1
			return self._chanel_num -1
		else:
			return -1

	def release_chanel(self, index):
		if -1 < index < self._chanel_num:
			self._chanel_list[index] = None
			self._chanel_num -= 1
			return False
		else:
			return True

	def get_chanel(self, index):
		if -1 < index < self._chanel_num:
			return self._chanel_list[index]
		else:
			return None
