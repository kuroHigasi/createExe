import pyd.indexDungeon as INDEX


class DisplayButton:
	def __init__(self, screen, img_list):
		self._screen = screen
		self._img_list = img_list

	def execute(self, index, touch, pos_x, pos_y):
		if touch:
			self._screen.blit(self._img_list[INDEX.ACTION()][index+1], (pos_x, pos_y))
		else:
			self._screen.blit(self._img_list[INDEX.ACTION()][index], (pos_x, pos_y))
