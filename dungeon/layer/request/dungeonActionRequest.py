import dataclasses


@dataclasses.dataclass
class DungeonActionRequest:
	_is_death: bool
	_is_go_action_on: bool
	_is_step_action_on: bool
	_log_flag: bool
	_box_flag: bool
	_start_pos_x: int
	_start_pos_y: int
	_now_pos_x: int
	_now_pos_y: int
	_now_way: int
	_width_max: int
	_depth_max: int
	_dungeon_map: list
	_enemy_count: int
	_act0_click: bool
	_act1_click: bool
	_retry_click: bool
	_box0_click: bool
	_box1_click: bool
	_box2_click: bool

	@property
	def is_death(self):
		return self._is_death

	@property
	def is_go_action_on(self):
		return self._is_go_action_on

	@property
	def is_step_action_on(self):
		return self._is_step_action_on

	@property
	def log_flag(self):
		return self._log_flag

	@property
	def box_flag(self):
		return self._box_flag

	@property
	def start_pos_x(self):
		return self._start_pos_x

	@property
	def start_pos_y(self):
		return self._start_pos_y

	@property
	def now_pos_x(self):
		return self._now_pos_x

	@property
	def now_pos_y(self):
		return self._now_pos_y

	@property
	def now_way(self):
		return self._now_way

	@property
	def width_max(self):
		return self._width_max

	@property
	def depth_max(self):
		return self._depth_max

	@property
	def dungeon_map(self):
		return self._dungeon_map

	@property
	def enemy_count(self):
		return self._enemy_count

	@property
	def act0_click(self):
		return self._act0_click

	@property
	def act1_click(self):
		return self._act1_click

	@property
	def retry_click(self):
		return self._retry_click

	@property
	def box0_click(self):
		return self._box0_click

	@property
	def box1_click(self):
		return self._box1_click

	@property
	def box2_click(self):
		return self._box2_click
