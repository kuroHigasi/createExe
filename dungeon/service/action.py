import dungeon.layer.request.dungeonActionRequest as dungeonActionRequest
import common.layer.response.response as response
import common.layer.code.code as code


class Action:
	def __init__(self, request: dungeonActionRequest.DungeonActionRequest):
		self._request = request
		self._is_death = request.is_death
		self._act_button = [request.act0_click, request.act1_click]
		self._box_button = [request.box0_click, request.box1_click, request.box2_click]
		self._retry_click = request.retry_click
		self.is_go_action_on = request.is_go_action_on
		self.is_step_action_on = request.is_step_action_on

	def action_enemy_move(self):
		if 0 < self._request.enemy_count:
			return response.Response(data=True, result=code.Code.OK)
		return response.Response(data=False, result=code.Code.DO_NOTHING)

	def action_move(self, dungeon_form, ope_form):
		if not self._is_death:  # 死亡時は行動しない
			if self.is_go_action_on:
				ope_form.space_off()  # 処理が連続で判定されないように実施
				ope_form.enter_off()  # 処理が連続で判定されないように実施
				# 更新(前進時)
				dungeon_form.player_move()
				if not (dungeon_form.existDiffPos()) and not (dungeon_form.ACTION_FLAG()):
					dungeon_form.actionFlagOn()
			elif self.is_step_action_on:
				ope_form.space_off()  # 処理が連続で判定されないように実施
				ope_form.enter_off()  # 処理が連続で判定されないように実施
				if not (dungeon_form.ACTION_FLAG()):
					dungeon_form.actionFlagOn()
			else:
				if dungeon_form.ACTION_FLAG():
					dungeon_form.actionFlagOff()
			# 更新(毎ターン)
			dungeon_form.update_way(ope_form)
			dungeon_form.update_situation()
			dungeon_form.update_view()

	def judge_log_flag(self, now_pos, is_diff, is_diff_way, act_flag):
		if not self._request.log_flag:
			if (is_diff and act_flag) or is_diff_way or \
					self._request.start_pos_x == now_pos[0] and self._request.start_pos_y == now_pos[1]:
				return response.Response(data=True, result=code.Code.OK)
		return response.Response(data=False, result=code.Code.DO_NOTHING)

	def judge_item_box_flag(self, is_diff):
		if is_diff and self._request.box_flag:
			if not self._request.log_flag:
				return response.Response(data=True, result=code.Code.OK)
		elif self._request.box_flag and not self._request.log_flag:
			return response.Response(data=True, result=code.Code.OK)
		return response.Response(data=False, result=code.Code.DO_NOTHING)

	def judge_enemy_touch(self, now_pos, pre_pos, enemy_pos_list, pre_enemy_pos_list):
		for index in range(0, self._request.enemy_count, 1):
			attack_judge_0 = enemy_pos_list[index][0] == now_pos[0] and enemy_pos_list[index][1] == now_pos[1]
			attack_judge_1 = enemy_pos_list[index][0] == pre_pos[0] and enemy_pos_list[index][1] == pre_pos[1]
			attack_judge_2 = pre_enemy_pos_list[index][0] == now_pos[0] and pre_enemy_pos_list[index][1] == now_pos[1]
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
