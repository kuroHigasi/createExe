from abc import ABCMeta, abstractmethod


class AbstractDisplay(ABCMeta):
	@staticmethod
	@abstractmethod
	def execute(config_form, request):
		pass

	@staticmethod
	@abstractmethod
	def create_request_data(screen, config_form, ope_form):
		pass
