import dungeon.layer.request.dungeonSoundRequest as dungeonSoundRequest
import common.layer.response.response as response
import common.layer.code.code as code
import common.debug.debug as dbg
import pygame


class Sound:
	def __init__(self, request: dungeonSoundRequest.DungeonSoundRequest):
		self._sound_list = request.sound_list
		self._volume = request.volume
		self._walk_flag = request.walk_flag

	def start(self):
		if self._walk_flag:
			sound_walk = pygame.mixer.Sound(self._sound_list[2])
			chanel = pygame.mixer.Channel(1)
			chanel.set_volume((self._volume/100)*0.8)
			chanel.play(sound_walk, maxtime=1000)
			dbg.LOG("移動開始：")
			return response.Response(data=True, result=code.Code.OK)
		return response.Response(data=True, result=code.Code.DO_NOTHING)
