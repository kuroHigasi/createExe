from abc import ABCMeta, abstractmethod

class AbstractDisplay(ABCMeta):
	@staticmethod
	@abstractmethod
	def execute(save_form, request):
		pass

	@staticmethod
	@abstractmethod
	def create_request_data(screen, save_form, ope_form):
		pass