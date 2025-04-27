from abc import ABCMeta, abstractmethod


class AbstractAction(ABCMeta):
	@staticmethod
	@abstractmethod
	def execute(dungeon_form, ope_form, request):
		pass

	@staticmethod
	@abstractmethod
	def create_request_data(dungeon_form, ope_form, config_form):
		pass
