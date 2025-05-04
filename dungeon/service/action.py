import copy

import dungeon.layer.request.dungeonActionRequest as dungeonActionRequest
import dungeon.service.component.actionNextPos as actionNextPos
import dungeon.form.position.form as pos_form
import common.layer.response.response as response
import common.layer.code.code as code


class Action:
	def __init__(self, request: dungeonActionRequest.DungeonActionRequest):
		self._is_death = request.is_death
		self._act_button = [request.act0_click, request.act1_click]
		self._box_button = [request.box0_click, request.box1_click, request.box2_click]
		self._retry_click = request.retry_click
		self._is_go_action_on = request.is_go_action_on
		self._is_step_action_on = request.is_step_action_on
		self._start_pos = pos_form.Form(request.start_pos_x, request.start_pos_y)
		self._now_pos = pos_form.Form(request.now_pos_x, request.now_pos_y)
		self._now_way = request.now_way
		self._dungeon_map = request.dungeon_map
		self._width_max = request.width_max
		self._depth_max = request.depth_max
		self._enemy_count = request.enemy_count
		self._log_flag = request.log_flag
		self._box_flag = request.box_flag

	def action_enemy_move(self):
		if 0 < self._enemy_count:
			return response.Response(data=True, result=code.Code.OK)
		return response.Response(data=False, result=code.Code.DO_NOTHING)

	def action_player_move(self, act_flag):
		now_pos = self._now_pos
		next_pos = copy.deepcopy(self._now_pos)
		reset_flag = False
		next_act_flag = act_flag
		if not self._is_death:  # 死亡時は行動しない
			if self._is_go_action_on:
				reset_flag = True
				# 更新(前進時)
				next_pos, move_flag = \
					actionNextPos.ActionNextPos(
						self._dungeon_map,
						self._width_max,
						self._depth_max
					).execute(now_pos, self._now_way)
				if move_flag and not act_flag: next_act_flag = True
			elif self._is_step_action_on:
				reset_flag = True
				if not act_flag: next_act_flag = True
			else:
				if act_flag: next_act_flag = False
			# 更新(毎ターン)
		return response.Response(data=(next_pos, reset_flag, next_act_flag), result=code.Code.OK)

	def judge_log_flag(self, now_pos, is_diff, is_diff_way, act_flag):
		if not self._log_flag:
			if (is_diff and act_flag) or is_diff_way or self._start_pos == now_pos:
				return response.Response(data=True, result=code.Code.OK)
		return response.Response(data=False, result=code.Code.DO_NOTHING)

	def judge_item_box_flag(self, is_diff):
		if is_diff and self._box_flag:
			if not self._log_flag:
				return response.Response(data=True, result=code.Code.OK)
		elif self._box_flag and not self._log_flag:
			return response.Response(data=True, result=code.Code.OK)
		return response.Response(data=False, result=code.Code.DO_NOTHING)

	def judge_enemy_touch(self, now_pos, pre_pos, enemy_pos_list, pre_enemy_pos_list):
		for index in range(0, self._enemy_count, 1):
			attack_judge_0 = enemy_pos_list[index] == now_pos
			attack_judge_1 = enemy_pos_list[index] == pre_pos
			attack_judge_2 = pre_enemy_pos_list[index] == now_pos
			if attack_judge_0 or (attack_judge_1 and attack_judge_2):
				return response.Response(data=(True, index), result=code.Code.OK)
		return response.Response(data=(False, -1), result=code.Code.DO_NOTHING)

	def action_button_click(self):
		if self._act_button[0]:
			return response.Response(data=(True, False), result=code.Code.OK)
		if self._act_button[1]:
			return response.Response(data=(False, True), result=code.Code.OK)
		return response.Response(data=(False, False), result=code.Code.DO_NOTHING)

	def retry_button_click(self):
		if self._retry_click and self._is_death:
			return response.Response(data=True, result=code.Code.OK)
		return response.Response(data=False, result=code.Code.DO_NOTHING)

	def box_button_click(self):
		for index in range(0, len(self._box_button), 1):
			if self._box_button[index]:
				return response.Response(data=index, result=code.Code.OK)
		return response.Response(data=-1, result=code.Code.DO_NOTHING)
