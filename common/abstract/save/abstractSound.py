from abc import ABCMeta, abstractmethod


class AbstractSound(ABCMeta):
	@staticmethod
	@abstractmethod
	def execute(request):
		pass

	@staticmethod
	@abstractmethod
	def create_request_data(sound_form, save_form, ope_form, config_form):
		pass
