import dataclasses


@dataclasses.dataclass
class DungeonSoundRequest:
	_sound_list: list
	_volume: int
	_walk_flag: bool
	__search_flag: bool

	@property
	def sound_list(self):
		return self._sound_list

	@property
	def volume(self):
		return self._volume

	@property
	def walk_flag(self):
		return self._walk_flag

	@property
	def search_flag(self):
		return self.__search_flag
