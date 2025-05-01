import dungeon.form.position.form as pos_form
import dungeon.common as cmn_dungeon
import common.debug.debug as dbg
import pyd.way as WAY


class Action:
	@staticmethod
	def get_player_next_pos(now_pos: pos_form.Form, way, dungeon_map, width_max, depth_max):
		depth = now_pos.x
		width = now_pos.y
		next_pos = now_pos
		flag = False
		if way == WAY.UP():
			if cmn_dungeon.Common.isPosPath(dungeon_map, depth-1, width, width_max, depth_max):
				next_pos.x = depth-1
				next_pos.y = width
				flag = True
			else:
				next_pos.x = depth
				next_pos.y = width
		elif way == WAY.RIGHT():
			if cmn_dungeon.Common.isPosPath(dungeon_map, depth, width+1, width_max, depth_max):
				next_pos.x = depth
				next_pos.y = width+1
				flag = True
			else:
				next_pos.x = depth
				next_pos.y = width
		elif way == WAY.LEFT():
			if cmn_dungeon.Common.isPosPath(dungeon_map, depth, width-1, width_max, depth_max):
				next_pos.x = depth
				next_pos.y = width-1
				flag = True
			else:
				next_pos.x = depth
				next_pos.y = width
		elif way == WAY.DOWN():
			if cmn_dungeon.Common.isPosPath(dungeon_map, depth+1, width, width_max, depth_max):
				next_pos.x = depth+1
				next_pos.y = width
				flag = True
			else:
				next_pos.x = depth
				next_pos.y = width
		else:
			dbg.ERROR_LOG("[action.go]存在しないWAY")
		return next_pos, flag