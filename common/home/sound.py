import common.common as cmn
import pygame


class Sound:
	@staticmethod
	def start(homeForm, opeForm, config_Form, soundForm):
		sound_list = soundForm.SOUND_LIST()
		(x, y) = opeForm.MOUSE()
		(clickX, clickY) = opeForm.leftClickMoveMouse()
		(startX, startY) = homeForm.START_BUTTON()
		(configX, configY) = homeForm.CONFIG_BUTTON()
		(exitX, exitY) = homeForm.EXIT_BUTTON()
		(loadX, loadY) = homeForm.LOAD_BUTTON()
		if cmn.Judge.click(startX, startY, 200, 80, x, y, clickX, clickY, opeForm.isLeftClick()):
			pygame.mixer.music.load(sound_list[0])
			pygame.mixer.music.set_volume(config_Form.get_volume()/100)
			pygame.mixer.music.play()
		if cmn.Judge.click(configX, configY, 200, 80, x, y, clickX, clickY, opeForm.isLeftClick()):
			pygame.mixer.music.load(sound_list[0])
			pygame.mixer.music.set_volume(config_Form.get_volume()/100)
			pygame.mixer.music.play()
		if cmn.Judge.click(exitX, exitY, 200, 80, x, y, clickX, clickY, opeForm.isLeftClick()):
			pygame.mixer.music.load(sound_list[0])
			pygame.mixer.music.set_volume(config_Form.get_volume()/100)
			pygame.mixer.music.play()
		if cmn.Judge.click(loadX, loadY, 200, 80, x, y, clickX, clickY, opeForm.isLeftClick()):
			pygame.mixer.music.load(sound_list[0])
			pygame.mixer.music.set_volume(config_Form.get_volume()/100)
			pygame.mixer.music.play()
