import common.layer.request.config.configSoundRequest as configSoundRequest
import common.layer.response.response as response
import common.layer.code.code as code
import common.debug.debug as dbg
import pygame


class Sound:
	def __init__(self, request: configSoundRequest.ConfigSoundRequest):
		self._test_playing_flag = request.test_playing_flag
		self._sound_list = request.sound_list
		self._volume = request.volume
		self._chanel = request.chanel

	def start(self):
		if self._test_playing_flag:
			sound = pygame.mixer.Sound(self._sound_list[1])
			chanel = pygame.mixer.Channel(0)
			chanel.set_volume(self._volume/100)
			chanel.play(sound)
			dbg.LOG("音量再生開始：")
			return response.Response(data=(True, True, chanel), result=code.Code.OK)
		else:
			if self._chanel is None:
				return response.Response(data=(False, False, None), result=code.Code.OK)
			else:
				return response.Response(data=(False, self._chanel.get_busy(), self._chanel), result=code.Code.OK)

