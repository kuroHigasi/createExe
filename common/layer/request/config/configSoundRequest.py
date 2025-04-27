import dataclasses


@dataclasses.dataclass(frozen=True)
class ConfigSoundRequest:
	_test_playing_flag: bool
	_sound_list: list
	_volume: int
	_chanel: any

	@property
	def test_playing_flag(self):
		return self._test_playing_flag

	@property
	def sound_list(self):
		return self._sound_list

	@property
	def volume(self):
		return self._volume

	@property
	def chanel(self):
		return self._chanel
