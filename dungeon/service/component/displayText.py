import common.common as cmn


class DisplayText:
	def __init__(self, screen, img_list, font, color=cmn.Colors.white):
		self._screen = screen
		self._img_list = img_list
		self._font = font
		self._color = color

	def execute(self, text, pos_x, pos_y):
		text_surface = self._font.render(text, True, self._color)
		text_rect = text_surface.get_rect(center=(pos_x+text_surface.get_width() / 2, pos_y))
		self._screen.blit(text_surface, text_rect)
