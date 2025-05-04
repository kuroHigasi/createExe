import common.common as cmn

class DisplayNumber:
	def __init__(self, screen, img_list, font, color=cmn.Colors.white):
		self._screen = screen
		self._img_list = img_list
		self._font = font
		self._color = color

	def execute(self, number: int, pos_x: int, pos_y: int):
		text_surface = self._font.render(str(number), True, self._color)
		number_len = len(str(number))
		text_rect = text_surface.get_rect(center=(pos_x+text_surface.get_width() / 2 - ((number_len - 1) * 6), pos_y))
		self._screen.blit(text_surface, text_rect)
