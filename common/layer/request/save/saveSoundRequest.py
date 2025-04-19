import dataclasses


@dataclasses.dataclass(frozen=True)
class SaveActionRequest:
	_save1_touch: bool
	_save2_touch: bool
	_save3_touch: bool
	_load1_touch: bool
	_load2_touch: bool
	_load3_touch: bool
	_delete1_touch: bool
	_delete2_touch: bool
	_delete3_touch: bool
	_sound_list: list
	_volume: int

	@property
	def save1_touch(self):
		return self._save1_touch

	@property
	def save2_touch(self):
		return self._save2_touch

	@property
	def save3_touch(self):
		return self._save3_touch

	@property
	def load1_touch(self):
		return self._load1_touch

	@property
	def load2_touch(self):
		return self._load2_touch

	@property
	def load3_touch(self):
		return self._load3_touch

	@property
	def delete1_touch(self):
		return self._delete1_touch

	@property
	def delete2_touch(self):
		return self._delete2_touch

	@property
	def delete3_touch(self):
		return self._delete3_touch

	@property
	def sound_list(self):
		return self._sound_list

	@property
	def volume(self):
		return self._volume
