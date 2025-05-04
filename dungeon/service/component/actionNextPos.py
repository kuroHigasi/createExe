import dungeon.form.position.form as pos_form
import dungeon.common as cmn_dungeon
import common.debug.debug as dbg
import pyd.way as WAY


class ActionNextPos:
	def __init__(self, dungeon_map, width_max, depth_max):
		self._dungeon_map = dungeon_map
		self._width_max = width_max
		self._depth_max = depth_max

	def execute(self, now_pos: pos_form.Form, way: int):
		depth = now_pos.x
		width = now_pos.y
		next_pos = now_pos
		flag = False
		if way == WAY.UP():
			if cmn_dungeon.Common.isPosPath(self._dungeon_map, depth-1, width, self._width_max, self._depth_max):
				next_pos.x = depth-1
				next_pos.y = width
				flag = True
			else:
				next_pos.x = depth
				next_pos.y = width
		elif way == WAY.RIGHT():
			if cmn_dungeon.Common.isPosPath(self._dungeon_map, depth, width+1, self._width_max, self._depth_max):
				next_pos.x = depth
				next_pos.y = width+1
				flag = True
			else:
				next_pos.x = depth
				next_pos.y = width
		elif way == WAY.LEFT():
			if cmn_dungeon.Common.isPosPath(self._dungeon_map, depth, width-1, self._width_max, self._depth_max):
				next_pos.x = depth
				next_pos.y = width-1
				flag = True
			else:
				next_pos.x = depth
				next_pos.y = width
		elif way == WAY.DOWN():
			if cmn_dungeon.Common.isPosPath(self._dungeon_map, depth+1, width, self._width_max, self._depth_max):
				next_pos.x = depth+1
				next_pos.y = width
				flag = True
			else:
				next_pos.x = depth
				next_pos.y = width
		else:
			dbg.ERROR_LOG("[action.go]存在しないWAY")
		return next_pos, flag
