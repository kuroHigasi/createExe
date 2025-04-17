import dataclasses
import common.download as download
import common.sound.repeat.repeat as repeat


@dataclasses.dataclass
class Form:
	_sound_list: list
	_repeat_save: repeat.Repeat

	def __init__(self):
		self._sound_list = download.Download.sound()
		self._repeat_save = repeat.Repeat(9)

	@property
	def sound_list(self):
		return self._sound_list

	def judge_repeat(self, index, touch):
		if self._repeat_save.get_flag(index) != touch:
			self._repeat_save.set_flag(index, touch)
			return touch
		return False