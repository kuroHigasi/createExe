import common.layer.request.saveActionRequest as saveActionRequest
import common.layer.response.response as response
import common.layer.code.code as code
import common.common as cmn
import pyd.save as save_separator


class Action:
	def __init__(self, request: saveActionRequest):
		self._input_data = request.input_data
		self._save_click_list = [
			request.save1_click,
			request.save2_click,
			request.save3_click]
		self._load_click_list = [
			request.load1_click,
			request.load2_click,
			request.load3_click]
		self._delete_click_list = [
			request.delete1_click,
			request.delete2_click,
			request.delete3_click]

	def save(self, index, convert):
		if self._save_click_list[index]:
			cmn.SaveMethod().save(
				self._input_data,
				save_separator.SAVE_HEAD(index),
				save_separator.SAVE_TAIL(index))
			text_list = Action._create_disp_save_list(self, convert)
			return response.Response(data=text_list, result=code.Code.OK)
		return response.Response(data="", result=code.Code.DO_NOTHING)

	def load(self, index):
		if self._load_click_list[index]:
			text = cmn.SaveMethod().load(
				save_separator.SAVE_HEAD(index),
				save_separator.SAVE_TAIL(index))
			return response.Response(data=text, result=code.Code.OK)
		return response.Response(data="", result=code.Code.DO_NOTHING)

	def delete(self, index, convert):
		if self._delete_click_list[index]:
			cmn.SaveMethod().delete(
				save_separator.SAVE_HEAD(index),
				save_separator.SAVE_TAIL(index))
			text_list = Action._create_disp_save_list(self, convert)
			return response.Response(data=text_list, result=code.Code.OK)
		return response.Response(data="", result=code.Code.DO_NOTHING)

	def _create_disp_save_list(self, convert):
		text_list = []
		for i in (0, 2, 1):
			head = save_separator.SAVE_HEAD(i)
			tail = save_separator.SAVE_TAIL(i)
			text_list.insert(i, convert(cmn.SaveMethod().load(head, tail)))
		return text_list
