import common.common as cmn
import common.layer.response.response as response
import common.layer.code.code as code
import common.debug.debug as dbg


class Action:
	def __init__(self, request):
		data_list = request.data
		self._x = data_list[0]
		self._click_x = data_list[1]
		self._click_y = data_list[2]
		self._way_key_type1_click = data_list[3]
		self._way_key_type2_click = data_list[4]
		self._go_key_type1_click = data_list[5]
		self._go_key_type2_click = data_list[6]
		self._step_key_type1_click = data_list[7]
		self._step_key_type2_click = data_list[8]
		self._tab1_click = data_list[9]
		self._tab2_click = data_list[10]
		self._way_key_type = data_list[11]
		self._go_key_type = data_list[12]
		self._tab = data_list[13]

	def select_way_key_type(self):
		if self._way_key_type != 0 and self._way_key_type1_click:
			return response.Response(data=0, result=code.Code.OK)
		elif self._way_key_type != 1 and self._way_key_type2_click:
			return response.Response(data=1, result=code.Code.OK)
		elif self._way_key_type1_click or self._way_key_type2_click:
			dbg.LOG("[ConfigAction._set_way_key_type]" + str(self._way_key_type) + "再設定")
			if self._way_key_type < 0 or 1 < self._way_key_type:
				dbg.ERROR_LOG("[ConfigAction._set_way_key_type]存在しないKeyType")
			return response.Response(data=-1, result=code.Code.ARGUMENT_ERROR)
		return response.Response(data=-1, result=code.Code.DO_NOTHING)

	def select_go_key_type(self):
		if self._go_key_type != 0 and self._go_key_type1_click:
			return response.Response(data=0, result=code.Code.OK)
		elif self._go_key_type != 1 and self._go_key_type2_click:
			return response.Response(data=1, result=code.Code.OK)
		elif self._go_key_type1_click or self._go_key_type2_click:
			dbg.LOG("[ConfigAction._set_go_key_type]" + str(self._go_key_type) + "再設定")
			if self._go_key_type < 0 or 2 < self._go_key_type:
				dbg.ERROR_LOG("[ConfigAction._set_go_key_type]存在しないKeyType")
			return response.Response(data=-1, result=code.Code.ARGUMENT_ERROR)
		return response.Response(data=-1, result=code.Code.DO_NOTHING)

	def select_step_key_type(self):
		if self._go_key_type != 1 and self._step_key_type1_click:
			return response.Response(data=1, result=code.Code.OK)
		elif self._go_key_type != 0 and self._step_key_type2_click:
			return response.Response(data=0, result=code.Code.OK)
		elif self._step_key_type1_click or self._step_key_type2_click:
			dbg.LOG("[ConfigAction._set_step_key_type]" + str(self._go_key_type) + "再設定")
			if self._go_key_type < 0 or 2 < self._go_key_type:
				dbg.ERROR_LOG("[ConfigAction._set_step_key_type]存在しないKeyType")
			return response.Response(data=-1, result=code.Code.ARGUMENT_ERROR)
		return response.Response(data=-1, result=code.Code.DO_NOTHING)

	def select_tab(self):
		if self._tab != 0 and self._tab1_click:
			return response.Response(data=0, result=code.Code.OK)
		elif self._tab != 1 and self._tab2_click:
			return response.Response(data=1, result=code.Code.OK)
		elif self._tab1_click or self._tab2_click:
			dbg.LOG("[ConfigAction._set_tab]" + str(self._tab) + "再設定")
			if self._tab < 0 or 2 < self._tab:
				dbg.ERROR_LOG("[ConfigAction._set_tab]存在しないKeyType")
			return response.Response(data=-1, result=code.Code.ARGUMENT_ERROR)
		return response.Response(data=-1, result=code.Code.DO_NOTHING)

	def select_volume(self):
		if 180 <= self._click_y <= 210 and 50 <= self._click_x <= 450:
			if 50 <= self._x <= 450:
				return response.Response(data=int((self._x - 50) / 4), result=code.Code.OK)
			elif self._x < 50:
				return response.Response(data=0, result=code.Code.OK)
			elif 450 < self._x:
				return response.Response(data=100, result=code.Code.OK)
		return response.Response(data=-1, result=code.Code.DO_NOTHING)
