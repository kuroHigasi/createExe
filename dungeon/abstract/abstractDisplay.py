from abc import ABCMeta, abstractmethod


class AbstractDisplay(ABCMeta):
	@staticmethod
	@abstractmethod
	def execute(dungeon_form, request):
		pass

	@staticmethod
	@abstractmethod
	def create_request_data(screen, dungeon_form, ope_form, system_form):
		pass
