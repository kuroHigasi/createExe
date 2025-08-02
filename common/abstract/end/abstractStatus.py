from abc import ABCMeta, abstractmethod, ABC


class AbstractStatus(ABCMeta, ABC):
	@staticmethod
	@abstractmethod
	def execute(status_form, request):
		pass

	@staticmethod
	@abstractmethod
	def create_request_data(end_form, ope_form):
		pass
