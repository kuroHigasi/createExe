import common.layer.request.config.configActionRequest as configActionRequest
import common.layer.response.response as response
import common.layer.code.code as code
import common.debug.debug as dbg


class Action:
	def __init__(self, request: configActionRequest):
		self._request = request

	def select_way_key_type(self):
		if self._request.way_key_type != 0 and self._request.way1_click:
			return response.Response(data=0, result=code.Code.OK)
		elif self._request.way_key_type != 1 and self._request.way2_click:
			return response.Response(data=1, result=code.Code.OK)
		elif self._request.way1_click or self._request.way2_click:
			dbg.LOG("[ConfigAction._set_way_key_type]" + str(self._request.way_key_type) + "再設定")
			if self._request.way_key_type < 0 or 1 < self._request.way_key_type:
				dbg.ERROR_LOG("[ConfigAction._set_way_key_type]存在しないKeyType")
			return response.Response(data=-1, result=code.Code.ARGUMENT_ERROR)
		return response.Response(data=-1, result=code.Code.DO_NOTHING)

	def select_go_key_type(self):
		if self._request.go_key_type != 0 and self._request.go1_click:
			return response.Response(data=0, result=code.Code.OK)
		elif self._request.go_key_type != 1 and self._request.go2_click:
			return response.Response(data=1, result=code.Code.OK)
		elif self._request.go1_click or self._request.go2_click:
			dbg.LOG("[ConfigAction._set_go_key_type]" + str(self._request.go_key_type) + "再設定")
			if self._request.go_key_type < 0 or 2 < self._request.go_key_type:
				dbg.ERROR_LOG("[ConfigAction._set_go_key_type]存在しないKeyType")
			return response.Response(data=-1, result=code.Code.ARGUMENT_ERROR)
		return response.Response(data=-1, result=code.Code.DO_NOTHING)

	def select_step_key_type(self):
		if self._request.go_key_type != 1 and self._request.step1_click:
			return response.Response(data=1, result=code.Code.OK)
		elif self._request.go_key_type != 0 and self._request.step2_click:
			return response.Response(data=0, result=code.Code.OK)
		elif self._request.step1_click or self._request.step2_click:
			dbg.LOG("[ConfigAction._set_step_key_type]" + str(self._request.go_key_type) + "再設定")
			if self._request.go_key_type < 0 or 2 < self._request.go_key_type:
				dbg.ERROR_LOG("[ConfigAction._set_step_key_type]存在しないKeyType")
			return response.Response(data=-1, result=code.Code.ARGUMENT_ERROR)
		return response.Response(data=-1, result=code.Code.DO_NOTHING)

	def select_tab(self):
		if self._request.tab != 0 and self._request.tab1_click:
			return response.Response(data=0, result=code.Code.OK)
		elif self._request.tab != 1 and self._request.tab2_click:
			return response.Response(data=1, result=code.Code.OK)
		elif self._request.tab1_click or self._request.tab2_click:
			dbg.LOG("[ConfigAction._set_tab]" + str(self._request.tab) + "再設定")
			if self._request.tab < 0 or 2 < self._request.tab:
				dbg.ERROR_LOG("[ConfigAction._set_tab]存在しないKeyType")
			return response.Response(data=-1, result=code.Code.ARGUMENT_ERROR)
		return response.Response(data=-1, result=code.Code.DO_NOTHING)

	def select_volume(self):
		if self._request.slider_click:
			if 50 <= self._request.click_pos_x <= 450:
				return response.Response(data=int((self._request.click_pos_x - 50) / 4), result=code.Code.OK)
			elif self._request.click_pos_x < 50:
				return response.Response(data=0, result=code.Code.OK)
			elif 450 < self._request.click_pos_x:
				return response.Response(data=100, result=code.Code.OK)
		return response.Response(data=-1, result=code.Code.DO_NOTHING)
