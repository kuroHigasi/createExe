import common.common as cmn
import pygame


class Sound:
	@staticmethod
	def start(homeForm, opeForm, soundForm):
		soundList = soundForm.SOUND_LIST()
		(x, y) = opeForm.MOUSE()
		(clickX, clickY) = opeForm.leftClickMoveMouse()
		(startX, startY) = homeForm.START_BUTTON()
		(configX, configY) = homeForm.CONFIG_BUTTON()
		(exitX, exitY) = homeForm.EXIT_BUTTON()
		(loadX, loadY) = homeForm.LOAD_BUTTON()
		if not (startX == -1 and startY == -1):
			if cmn.Judge.click(startX, startY, 200, 80, x, y, clickX, clickY, opeForm.isLeftClick()):
				pygame.mixer.music.load(soundList[0])
				pygame.mixer.music.set_volume(1.0)
				pygame.mixer.music.play()
		if not (configX == -1 and configY == -1):
			if cmn.Judge.click(configX, configY, 200, 80, x, y, clickX, clickY, opeForm.isLeftClick()):
				pygame.mixer.music.load(soundList[0])
				pygame.mixer.music.set_volume(1.0)
				pygame.mixer.music.play()
		if not (exitX == -1 and exitY == -1):
			if cmn.Judge.click(exitX, exitY, 200, 80, x, y, clickX, clickY, opeForm.isLeftClick()):
				pygame.mixer.music.load(soundList[0])
				pygame.mixer.music.set_volume(1.0)
				pygame.mixer.music.play()
		if not (loadX == -1 and loadY == -1):
			if cmn.Judge.click(loadX, loadY, 200, 80, x, y, clickX, clickY, opeForm.isLeftClick()):
				pygame.mixer.music.load(soundList[0])
				pygame.mixer.music.set_volume(1.0)
				pygame.mixer.music.play()
