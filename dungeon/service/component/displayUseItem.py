import pyd.typeItem as ITEM
import pyd.indexDungeon as INDEX
import pygame


class DisplayUseItem:
	def __init__(self, screen, img_list, item_list, use_list, compass_angle):
		self._screen = screen
		self._img_list = img_list
		self._item_list = item_list
		self._use_list = use_list
		self._compass_angle = compass_angle

	def execute(self):
		for index in range(0, len(self._item_list), 1):
			item = self._item_list[index]
			use = self._use_list[index]
			if not use:
				break
			if item == ITEM.COMPASS():
				image = self._img_list[INDEX.COMPASS()][0]
				image_rotate = pygame.transform.rotate(image, self._compass_angle)
				self._screen.blit(image_rotate, image_rotate.get_rect(center=image.get_rect(center=(65, 530)).center))
