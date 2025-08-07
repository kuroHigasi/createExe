from abc import ABCMeta, abstractmethod, ABC


class AbstractSound(ABCMeta, ABC):
	@staticmethod
	@abstractmethod
	def execute(request):
		pass

	@staticmethod
	@abstractmethod
	def create_request_data(sound_form, save_form, ope_form, config_form):
		pass
