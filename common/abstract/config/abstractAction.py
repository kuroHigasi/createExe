from abc import ABCMeta, abstractmethod, ABC


class AbstractAction(ABCMeta, ABC):
	@staticmethod
	@abstractmethod
	def execute(config_form, request):
		pass

	@staticmethod
	@abstractmethod
	def create_request_data(config_form, ope_form):
		pass