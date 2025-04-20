import pygame


class Sound:
	def __init__(self, request):
		self._touch_list = [
			request.save1_touch,
			request.save2_touch,
			request.save3_touch,
			request.load1_touch,
			request.load2_touch,
			request.load3_touch,
			request.delete1_touch,
			request.delete2_touch,
			request.delete3_touch]
		self._sound_list = request.sound_list
		self._volume = float(request.volume)

	def start(self):
		for touch in self._touch_list:
			if touch:
				pygame.mixer.music.load(self._sound_list[0])
				pygame.mixer.music.set_volume(self._volume / 100.0)
				pygame.mixer.music.play()