import dataclasses


@dataclasses.dataclass
class Form:
	_volume: int = 30
	_volume_pre: int = 30
	_way_key_type: int = 0
	_way_key_type_pre: int = 0
	_go_key_type: int = 0
	_go_key_type_pre: int = 0

	@property
	def volume(self):
		return self._volume

	@volume.setter
	def volume(self, volume):
		if 0 <= volume <= 100:
			self._volume = volume

	@property
	def volume_pre(self):
		return self._volume_pre

	@volume_pre.setter
	def volume_pre(self, volume):
		if 0 <= volume <= 100:
			self._volume_pre = volume

	@property
	def way_key_type(self):
		return self._way_key_type

	@way_key_type.setter
	def way_key_type(self, key_type):
		if 0 <= key_type < 2:
			self._way_key_type = key_type

	@property
	def way_key_type_pre(self):
		return self._way_key_type_pre

	@way_key_type_pre.setter
	def way_key_type_pre(self, key_type):
		if 0 <= key_type < 2:
			self._way_key_type_pre = key_type

	@property
	def go_key_type(self):
		return self._go_key_type

	@go_key_type.setter
	def go_key_type(self, key_type):
		if 0 <= key_type < 2:
			self._go_key_type = key_type

	@property
	def go_key_type_pre(self):
		return self._go_key_type_pre

	@go_key_type_pre.setter
	def go_key_type_pre(self, key_type):
		if 0 <= key_type < 2:
			self._go_key_type_pre = key_type
