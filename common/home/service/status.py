import common.layer.request.home.homeStatusRequest as homeStatusRequest
import common.layer.response.response as response
import common.layer.code.code as code
import pyd.status as STATUS


class Status:
	def __init__(self, request: homeStatusRequest.HomeStatusRequest):
		self._request = request

	def get_next_status(self):
		if self._request.start_click:
			return response.Response(data=STATUS.DUNGEON(), result=code.Code.OK)
		if self._request.config_click:
			return response.Response(data=STATUS.CONFIG(), result=code.Code.OK)
		if self._request.exit_click:
			return response.Response(data=STATUS.EXIT(), result=code.Code.OK)
		if self._request.load_click:
			return response.Response(data=STATUS.SAVE(), result=code.Code.OK)
		return response.Response(data=STATUS.HOME(), result=code.Code.DO_NOTHING)
