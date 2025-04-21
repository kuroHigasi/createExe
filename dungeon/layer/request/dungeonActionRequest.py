import dataclasses


@dataclasses.dataclass
class DungeonStatusRequest:
	_is_death: bool
	_is_go_action_on: bool
	_is_step_action_on: bool
	_action_flag: bool
	_box_flag: bool
	_log_flag: bool
	_start_pos_x: int
	_start_pos_y: int
	_enemy_count: int
	_enemy_pos: list
	_act0_click: bool
	_act1_click: bool
	_retry_click: bool
	_box0_click: bool
	_box1_click: bool
	_box2_click: bool
