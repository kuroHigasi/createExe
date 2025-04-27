import common.layer.request.home.homeSoundRequest as homeSoundRequest
import common.layer.response.response as response
import common.layer.code.code as code
import pygame


class Sound:
	def __init__(self, request: homeSoundRequest.HomeSoundRequest):
		self._request = request

	def start(self):
		if self._request.start_click or \
			self._request.config_click or\
			self._request.exit_click or \
			self._request.load_click:
			pygame.mixer.music.load(self._request.sound_list[0])
			pygame.mixer.music.set_volume(self._request.volume/100)
			pygame.mixer.music.play()
			return response.Response(data=True, result=code.Code.OK)
		return response.Response(data=False, result=code.Code.OK)
