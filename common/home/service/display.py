import common.layer.request.home.homeDisplayRequest as homeDisplayRequest
import common.layer.response.response as response
import common.layer.code.code as code
import pyd.indexHome as index


class Display:
	def __init__(self, request: homeDisplayRequest.HomeSoundRequest):
		self._touch_list = \
			[request.start_touch,
			request.load_touch,
			request.config_touch,
			request.exit_touch]
		self._img_list = request.img_list
		self._screen = request.screen
		self._screen.blit(self._img_list[index.HOME()][0], (0, 0))

	def disp_start_button(self):
		pos_x = 50
		pos_y = 300
		if self._touch_list[0]:
			self._screen.blit(self._img_list[index.BUTTON()][3], (pos_x, pos_y))
		else:
			self._screen.blit(self._img_list[index.BUTTON()][2], (pos_x, pos_y))
		return response.Response(data=(pos_x, pos_y), result=code.Code.OK)

	def disp_load_button(self):
		pos_x = 50
		pos_y = 390
		if self._touch_list[1]:
			self._screen.blit(self._img_list[index.BUTTON()][7], (pos_x, pos_y))
		else:
			self._screen.blit(self._img_list[index.BUTTON()][6], (pos_x, pos_y))
		return response.Response(data=(pos_x, pos_y), result=code.Code.OK)

	def disp_config_button(self):
		pos_x = 50
		pos_y = 580
		if self._touch_list[2]:
			self._screen.blit(self._img_list[index.BUTTON()][11], (pos_x, pos_y))
		else:
			self._screen.blit(self._img_list[index.BUTTON()][10], (pos_x, pos_y))
		return response.Response(data=(pos_x, pos_y), result=code.Code.OK)

	def disp_exit_button(self):
		pos_x = 50
		pos_y = 670
		if self._touch_list[3]:
			self._screen.blit(self._img_list[index.BUTTON()][1], (pos_x, pos_y))
		else:
			self._screen.blit(self._img_list[index.BUTTON()][0], (pos_x, pos_y))
		return response.Response(data=(pos_x, pos_y), result=code.Code.OK)
