import dungeon.img as img
import pyd.indexDungeon as INDEX


class DisplayView:
	def __init__(self, screen, img_list, now_view):
		self._screen = screen
		self._img_list = img_list
		self._now_view = now_view

	def execute(self, pos_x, pos_y):
		now_view = self._now_view
		screen = self._screen
		img_list = self._img_list
		screen.blit(img_list[INDEX.RIGHT()][INDEX.UP_POS()][img.Select.RU(now_view)], (pos_x + 600, pos_y))
		screen.blit(img_list[INDEX.RIGHT()][INDEX.CENTER_POS()][img.Select.RC(now_view)], (pos_x + 600, pos_y + 150))
		screen.blit(img_list[INDEX.RIGHT()][INDEX.DOWN_POS()][img.Select.RD(now_view)], (pos_x + 600, pos_y + 450))
		screen.blit(img_list[INDEX.CENTER()][INDEX.UP_POS()][img.Select.CU(now_view)], (pos_x + 200, pos_y))
		screen.blit(img_list[INDEX.CENTER()][INDEX.CENTER_POS()][img.Select.CC(now_view)], (pos_x + 200, pos_y + 150))
		screen.blit(img_list[INDEX.CENTER()][INDEX.DOWN_POS()][img.Select.CD(now_view)], (pos_x + 200, pos_y + 450))
		screen.blit(img_list[INDEX.LEFT()][INDEX.UP_POS()][img.Select.LU(now_view)], (pos_x, pos_y))
		screen.blit(img_list[INDEX.LEFT()][INDEX.CENTER_POS()][img.Select.LC(now_view)], (pos_x, pos_y + 150))
		screen.blit(img_list[INDEX.LEFT()][INDEX.DOWN_POS()][img.Select.LD(now_view)], (pos_x, pos_y + 450))
		screen.blit(img_list[INDEX.FLAME()][img.Select.FLAME(now_view)], (pos_x, pos_y))

