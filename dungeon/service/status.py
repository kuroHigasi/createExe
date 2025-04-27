import dungeon.layer.request.dungeonStatusRequest as dungeonStatusRequest
from common.layer.code import code
from common.layer.response import response
import pyd.status as STATUS


class Status:
	def __init__(self, request: dungeonStatusRequest.DungeonStatusRequest):
		self._request = request

	def get_next_status(self):
		if self._request.end_flag:
			return response.Response(data=STATUS.END(), result=code.Code.OK)

		if self._request.config_button_click:
			return response.Response(data=STATUS.CONFIG(), result=code.Code.OK)

		if self._request.save_button_click:
			return response.Response(data=STATUS.SAVE(), result=code.Code.OK)

		return response.Response(data=STATUS.DUNGEON(), result=code.Code.DO_NOTHING)
