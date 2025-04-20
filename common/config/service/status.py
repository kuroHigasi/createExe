import common.layer.request.config.configStatusRequest as configStatusRequest
import common.layer.response.response as response
import common.common as cmn
import pyd.status as status
import pyd.save as save
from common.layer.code import code


class Status:
	def __init__(self, request: configStatusRequest.ConfigDisplayRequest):
		self._request = request

	def get_next_status(self):
		if self._request.ok_click:
			cmn.SaveMethod().save(self._request.input_data, save.CONF_HEAD(), save.CONF_TAIL())
			return response.Response(data=(False, self._request.pre_status), result=code.Code.OK)
		if self._request.back_click:
			return response.Response(data=(True, self._request.pre_status), result=code.Code.OK)
		return response.Response(data=(False, status.CONFIG()), result=code.Code.DO_NOTHING)
