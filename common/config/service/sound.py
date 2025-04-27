import common.layer.request.config.configSoundRequest as configSoundRequest
import common.layer.response.response as response
import common.layer.code.code as code
import pygame


class Sound:
	def __init__(self, request: configSoundRequest.ConfigSoundRequest):
		self._test_playing_flag = request.test_playing_flag
		self._sound_list = request.sound_list
		self._volume = request.volume

	def start(self):
		if self._test_playing_flag:
			pygame.mixer.music.load(self._sound_list[0])
			pygame.mixer.music.set_volume(self._volume/100)
			pygame.mixer.music.play()
			return response.Response(data=(False, False), result=code.Code.OK)
		else:
			return response.Response(data=(False, pygame.mixer.get_busy()), result=code.Code.OK)

