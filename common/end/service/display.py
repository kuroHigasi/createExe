import common.layer.request.end.endDisplayRequest as endDisplayRequest
import common.layer.response.response as response
import common.layer.code.code as code
import common.common as cmn
import pyd.indexEnd as INDEX


class Display:
	def __init__(self, request: endDisplayRequest.EndDisplayRequest):
		self._home_touch = request.home_button_touch
		self._screen = request.screen
		self._action_count = request.action_count
		self._font = request.font
		self._img_list = request.img_list
		self._screen.blit(self._img_list[INDEX.END()][0], (0, 0))

	def disp_result(self):
		pos_x = 50
		pos_y = 200
		Display.__disp_text(self._screen, self._font, "総行動数:" + str(self._action_count), pos_x, pos_y)
		return response.Response(data=True, result=code.Code.OK)

	def disp_home_button(self):
		pos_x = 50
		pos_y = 670
		if self._home_touch:
			self._screen.blit(self._img_list[INDEX.BUTTON()][5], (pos_x, pos_y))
		else:
			self._screen.blit(self._img_list[INDEX.BUTTON()][4], (pos_x, pos_y))
		return response.Response(data=(pos_x, pos_y), result=code.Code.OK)

	@staticmethod
	def __disp_text(screen, font, text: str, x: int, y: int):
		text_surface = font.render(text, True, cmn.Colors.black)
		text_rect = text_surface.get_rect(center=(x+text_surface.get_width()/2, y))
		screen.blit(text_surface, text_rect)
