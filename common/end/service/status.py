import common.layer.request.end.endStatusRequest as endStatusRequest
import common.layer.response.response as response
import common.layer.code.code as code
import pyd.status as STATUS


class Status:
	def __init__(self, request: endStatusRequest.EndStatusRequest):
		self._home_click = request.home_button_click

	def get_next_status(self):
		if self._home_click:
			return response.Response(data=STATUS.HOME(), result=code.Code.OK)
		return response.Response(data=STATUS.END(), result=code.Code.DO_NOTHING)
