import dataclasses
import common.download as download

@dataclasses.dataclass
class Form:
	soundList: list

	def __init__(self):
		self.soundList = download.Download.sound()

	def SOUND_LIST(self):
		return self.soundList