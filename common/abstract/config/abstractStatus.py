from abc import ABCMeta, abstractmethod


class AbstractStatus(ABCMeta):
	@staticmethod
	@abstractmethod
	def execute(status_form, config_form, request):
		pass

	@staticmethod
	@abstractmethod
	def create_request_data(config_form, ope_form):
		pass
