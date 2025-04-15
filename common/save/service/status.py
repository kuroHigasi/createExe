import pyd.status as STATUS
import common.layer.response.response as reponse
import common.layer.code.code as code

class Status:
	def __init__(self, request):
		self._request = request

	def get_next_status(self):
		next_status = STATUS.SAVE()
		if self._request.back_button_click:
			next_status = self._request.pre_status
		if self._request.home_button_click:
			next_status = STATUS.HOME()
		if self._request.output_data != "":
			next_status = STATUS.DUNGEON()
		return reponse.Response(data=next_status, result=code.Code.OK)
