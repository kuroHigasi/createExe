from abc import ABCMeta, abstractmethod


class AbstractSound(ABCMeta):
	@staticmethod
	@abstractmethod
	def execute(sound_form, config_form, request):
		pass

	@staticmethod
	@abstractmethod
	def create_request_data(sound_form, config_form, ope_form):
		pass
