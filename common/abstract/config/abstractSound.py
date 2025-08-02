from abc import ABCMeta, abstractmethod, ABC


class AbstractSound(ABCMeta, ABC):
	@staticmethod
	@abstractmethod
	def execute(sound_form, config_form, request):
		pass

	@staticmethod
	@abstractmethod
	def create_request_data(sound_form, config_form, ope_form):
		pass
