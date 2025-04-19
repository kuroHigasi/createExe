import dataclasses
import common.layer.code.code as code


@dataclasses.dataclass
class Response:
	_data: any
	_result: code.Code

	def __init__(self, data, result):
		self._data = data
		self._result = result

	@property
	def data(self):
		return self._data

	def is_ok(self):
		return self._result == code.Code.OK

	def is_do_nothing(self):
		return self._result == code.Code.DO_NOTHING

	def is_not_ok(self):
		return \
			not (self._result == code.Code.OK) and \
			not (self._result == code.Code.DO_NOTHING)
