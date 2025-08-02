from abc import ABCMeta, abstractmethod, ABC


class AbstractAction(ABCMeta, ABC):
	@staticmethod
	@abstractmethod
	def execute(save_form, request):
		pass

	@staticmethod
	@abstractmethod
	def create_request_data(save_form, ope_form):
		pass
