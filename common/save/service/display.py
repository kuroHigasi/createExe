import common.layer.request.saveDisplayRequest as saveDisplayRequest
import common.layer.response.response as response
import common.layer.code.code as code
import pyd.hitJudge as hitJudge
import pyd.indexSave as INDEX
import common.common as cmn

class Display:
	def __init__(self, request: saveDisplayRequest):
		self._screen = request.screen
		self._font = request.font
		self._img_list = request.img_list
		self._x = request.mouse_pos_x
		self._y = request.mouse_pos_y
		self._input_data = request.input_data
		self._disp_list = request.save_disp_list
		self._back_button_width = request.back_button_width
		self._back_button_height = request.back_button_height
		self._home_button_width = request.home_button_width
		self._home_button_height = request.home_button_height
		self._list_width = request.list_width
		self._list_height = request.list_height
		self._mini_width = request.mini_button_width
		self._mini_height = request.mini_button_height

	def disp_back_button(self):
		pos_x = 750
		pos_y = 670
		if hitJudge.hitJudgeSquare(pos_x, pos_y, self._back_button_width, self._back_button_height, self._x, self._x):
			self._screen.blit(self._img_list[INDEX.BUTTON()][15], (pos_x, pos_y))
		else:
			self._screen.blit(self._img_list[INDEX.BUTTON()][14], (pos_x, pos_y))
		response.Response(data=(pos_x, pos_y), result=code.Code.OK)

	def disp_home_button(self):
		pos_x = 540
		pos_y = 670
		if hitJudge.hitJudgeSquare(pos_x, pos_y, self._home_button_width, self._home_button_height, self._x, self._x):
			self._screen.blit(self._img_list[INDEX.BUTTON()][4], (pos_x, pos_y))
		else:
			self._screen.blit(self._img_list[INDEX.BUTTON()][5], (pos_x, pos_y))
		response.Response(data=(pos_x, pos_y), result=code.Code.OK)

	def disp_list(self, index):
		pos_x = 150
		pos_y_list = [150, 310, 470]
		self._screen.blit(self._img_list[INDEX.LIST()][0], (pos_x, pos_y_list[index]))
		response.Response(data=True, result=code.Code.OK)

	def disp_list_text(self, index):
		flag, text = self._disp_list[index]
		pos_x = 190
		pos_y_list = [225, 385, 545]
		if flag:  # TEXT
			disp_text = text
		else:
			disp_text = "セーブなし"
		text_surface = self._font.render(disp_text, True, cmn.Colors.black)
		text_rect = text_surface.get_rect(center=(pos_x+text_surface.get_width()/2, pos_y_list[index]))
		self._screen.blit(text_surface, text_rect)
		response.Response(data=disp_text, result=code.Code.OK)

	def valid_save_button(self, index):
		pos_x = 740
		pos_y_list = [162, 322, 482]
		if not (self._input_data == ""):  # SAVE BUTTON
			if hitJudge.hitJudgeSquare(pos_x, pos_y_list[index], self._mini_width, self._mini_height, self._x, self._y):
				self._screen.blit(self._img_list[INDEX.SAVE_BUTTON()][1], (pos_x, pos_y_list[index]))
			else:
				self._screen.blit(self._img_list[INDEX.SAVE_BUTTON()][0], (pos_x, pos_y_list[index]))
			response.Response(data=(pos_x, pos_y_list[index]), result=code.Code.OK)
		else:
			self._screen.blit(self._img_list[INDEX.SAVE_BUTTON()][2], (pos_x, pos_y_list[index]))
			response.Response(data=(-1, -1), result=code.Code.OK)

	def valid_load_button(self, index):
		flag, text = self._disp_list[index]
		pos_x = 740
		pos_y_list = [202, 365, 525]
		if flag:  # LOAD BUTTON
			if hitJudge.hitJudgeSquare(pos_x, pos_y_list[index], self._mini_width, self._mini_height, self._x, self._y):
				self._screen.blit(self._img_list[INDEX.SAVE_BUTTON()][4], (pos_x, pos_y_list[index]))
			else:
				self._screen.blit(self._img_list[INDEX.SAVE_BUTTON()][3], (pos_x, pos_y_list[index]))
			response.Response(data=(pos_x, pos_y_list[index]), result=code.Code.OK)
		else:
			self._screen.blit(self._img_list[INDEX.SAVE_BUTTON()][5], (pos_x, pos_y_list[index]))
			response.Response(data=(-1, -1), result=code.Code.OK)

	def valid_delete_button(self, index):
		flag, text = self._disp_list[index]
		pos_x = 740
		pos_y_list = [248, 408, 568]
		if flag:  # DELETE BUTTON
			if hitJudge.hitJudgeSquare(pos_x, pos_y_list[index], self._mini_width, self._mini_height, self._x, self._y):
				self._screen.blit(self._img_list[INDEX.SAVE_BUTTON()][7], (pos_x, pos_y_list[index]))
			else:
				self._screen.blit(self._img_list[INDEX.SAVE_BUTTON()][6], (pos_x, pos_y_list[index]))
			response.Response(data=(pos_x, pos_y_list[index]), result=code.Code.OK)
		else:
			self._screen.blit(self._img_list[INDEX.SAVE_BUTTON()][8], (pos_x, pos_y_list[index]))
			response.Response(data=(-1, -1), result=code.Code.OK)

