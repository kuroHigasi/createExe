from abc import ABCMeta, abstractmethod


class AbstractDisplay(ABCMeta):
	@staticmethod
	@abstractmethod
	def execute(home_form, request):
		pass

	@staticmethod
	@abstractmethod
	def create_request_data(screen, home_form, ope_form):
		pass
