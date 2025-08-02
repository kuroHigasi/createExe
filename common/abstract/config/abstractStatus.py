from abc import ABCMeta, abstractmethod, ABC


class AbstractStatus(ABCMeta, ABC):
	@staticmethod
	@abstractmethod
	def execute(status_form, config_form, request):
		pass

	@staticmethod
	@abstractmethod
	def create_request_data(config_form, ope_form):
		pass
