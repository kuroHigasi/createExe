import dataclasses
import common.common as cmn


@dataclasses.dataclass
class DungeonDisplayRequest:
	_screen: any
	_img_list: list
	_font: any
	_item_font: any
	_event_font: any
	_is_death: bool
	_is_stairs: bool
	_is_item_get: bool
	_view: int
	_situation: list
	_text_flash: any
	_radar_flash: any
	_enemy_pos_list: list
	_enemy_type_list: list
	_enemy_index_list: list
	_log_list: list
	_log_num: int
	_config_touch: bool
	_save_touch: bool
	_retry_touch: bool
	_box0_item: int
	_box0_num: int
	_box0_use: bool
	_box0_touch: bool
	_box1_item: int
	_box1_num: int
	_box1_use: bool
	_box1_touch: bool
	_box2_item: int
	_box2_num: int
	_box2_use: bool
	_box2_touch: bool
	_compass_angle: int
	_floor: int
	_count: int
	_mouse_x: int
	_mouse_y: int

	@property
	def screen(self):
		return self._screen

	@property
	def img_list(self):
		return self._img_list

	@property
	def font(self):
		return self._font

	@property
	def item_font(self):
		return self._item_font

	@property
	def event_font(self):
		return self._event_font

	@property
	def is_death(self):
		return self._is_death

	@property
	def is_stairs(self):
		return self._is_stairs

	@property
	def is_item_get(self):
		return self._is_item_get

	@property
	def view(self):
		return self._view

	@property
	def situation(self):
		return self._situation

	@property
	def text_flash(self):
		return self._text_flash

	@property
	def radar_flash(self):
		return self._radar_flash

	@property
	def enemy_pos_list(self):
		return self._enemy_pos_list

	@property
	def enemy_type_list(self):
		return self._enemy_type_list

	@property
	def enemy_index_list(self):
		return self._enemy_index_list

	@property
	def log_list(self):
		return self._log_list

	@property
	def log_num(self):
		return self._log_num

	@property
	def config_touch(self):
		return self._config_touch

	@property
	def save_touch(self):
		return self._save_touch

	@property
	def retry_touch(self):
		return self._retry_touch

	@property
	def box0_item(self):
		return self._box0_item

	@property
	def box0_num(self):
		return self._box0_num

	@property
	def box0_use(self):
		return self._box0_use

	@property
	def box0_touch(self):
		return self._box0_touch

	@property
	def box1_item(self):
		return self._box1_item

	@property
	def box1_num(self):
		return self._box1_num

	@property
	def box1_use(self):
		return self._box1_use

	@property
	def box1_touch(self):
		return self._box1_touch

	@property
	def box2_item(self):
		return self._box2_item

	@property
	def box2_num(self):
		return self._box2_num

	@property
	def box2_use(self):
		return self._box2_use

	@property
	def box2_touch(self):
		return self._box2_touch

	@property
	def compass_angle(self):
		return self._compass_angle

	@property
	def floor(self):
		return self._floor

	@property
	def count(self):
		return self._count

	@property
	def mouse_x(self):
		return self._mouse_x

	@property
	def mouse_y(self):
		return self._mouse_y
