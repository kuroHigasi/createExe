import common.layer.request.config.configDisplayRequest as configDisplayRequest
from pygame_widgets.slider import Slider
import common.layer.response.response as response
import common.layer.code.code as code
import common.common as cmn
import pyd.indexConfig as Index


class Display:
	def __init__(self, request: configDisplayRequest.ConfigDisplayRequest):
		self._screen = request.screen
		self._font = request.font
		self._img_list = request.img_list
		self._way_touch_list = [request.way1_touch, request.way2_touch]
		self._go_touch_list = [request.go1_touch, request.go2_touch]
		self._step_touch_list = [request.step1_touch, request.step2_touch]
		self._tab_touch_list = [request.tab1_touch, request.tab2_touch]
		self._ok_touch = request.ok_touch
		self._back_touch = request.back_touch
		self._way_type = request.way_key_type
		self._go_type = request.go_key_type
		self._tab = request.tab
		self._volume = request.volume
		self._screen.blit(self._img_list[Index.CONFIG()][0], (0, 0))

	def disp_ok_button(self):
		pos_x = 750
		pos_y = 670
		if self._ok_touch:
			self._screen.blit(self._img_list[Index.SET_BUTTON()][7], (pos_x, pos_y))
		else:
			self._screen.blit(self._img_list[Index.SET_BUTTON()][6], (pos_x, pos_y))
		return response.Response(data=(pos_x, pos_y), result=code.Code.OK)

	def disp_back_button(self):
		pos_x = 540
		pos_y = 670
		if self._back_touch:
			self._screen.blit(self._img_list[Index.BUTTON()][15], (pos_x, pos_y))
		else:
			self._screen.blit(self._img_list[Index.BUTTON()][14], (pos_x, pos_y))
		return response.Response(data=(pos_x, pos_y), result=code.Code.OK)

	def disp_tab(self, index):
		pos_x_list = [50, 300]
		pos_y = 100
		if index < -1 or 1 < index:
			return response.Response(data=-1, result=code.Code.ARGUMENT_ERROR)

		if self._tab_touch_list[index]:
			self._screen.blit(self._img_list[Index.CONFIG_BUTTON()][1], (pos_x_list[index], pos_y))
		else:
			if index == self._tab:
				self._screen.blit(self._img_list[Index.CONFIG_BUTTON()][0], (pos_x_list[index], pos_y))
			else:
				self._screen.blit(self._img_list[Index.CONFIG_BUTTON()][2], (pos_x_list[index], pos_y))
		return response.Response(data=(pos_x_list[index], pos_y), result=code.Code.OK)

	def disp_way_button(self, index):
		type_list = [1, 3]
		pos_x_list = [50, 260]
		pos_y = 180
		way_type_text_list = ["WASD操作", "方向キー操作"]
		if index == 0:
			if self._tab == 0:
				Display.__disp_text(
					self._screen,
					self._font,
					"方向キー入力タイプ…" + way_type_text_list[self._way_type],
					50,
					150)
		elif index > 1:
			return response.Response(data=-1, result=code.Code.ARGUMENT_ERROR)

		if self._tab == 0:
			# WAY BUTTON 表示
			if self._way_touch_list[index]:
				self._screen.blit(self._img_list[Index.SET_BUTTON()][type_list[index]+1], (pos_x_list[index], pos_y))
			else:
				self._screen.blit(self._img_list[Index.SET_BUTTON()][type_list[index]], (pos_x_list[index], pos_y))
			if self._way_type == index:
				self._screen.blit(self._img_list[Index.SET_BUTTON()][0], (pos_x_list[index], pos_y))
			return response.Response(data=(pos_x_list[index], pos_y), result=code.Code.OK)
		else:
			# WAY BUTTON 非表示
			return response.Response(data=(-1, -1), result=code.Code.OK)

	def disp_go_button(self, index):
		type_list = [1, 3]
		pos_x_list = [50, 260]
		pos_y = 320
		go_type_text_list = ["スペース押下", "エンター押下"]
		if index == 0:
			if self._tab == 0:
				Display.__disp_text(
					self._screen,
					self._font,
					"前進入力タイプ…" + go_type_text_list[self._go_type],
					50,
					285)
		elif index > 1:
			return response.Response(data=-1, result=code.Code.ARGUMENT_ERROR)

		if self._tab == 0:
			# GO BUTTON 表示
			if self._go_touch_list[index]:
				self._screen.blit(self._img_list[Index.SET_BUTTON()][type_list[index]+1], (pos_x_list[index], pos_y))
			else:
				self._screen.blit(self._img_list[Index.SET_BUTTON()][type_list[index]], (pos_x_list[index], pos_y))
			if self._go_type == index:
				self._screen.blit(self._img_list[Index.SET_BUTTON()][0], (pos_x_list[index], pos_y))
			return response.Response(data=(pos_x_list[index], pos_y), result=code.Code.OK)
		else:
			# GO BUTTON 非表示
			return response.Response(data=(-1, -1), result=code.Code.OK)

	def disp_step_button(self, index):
		type_list = [3, 1]
		pos_x_list = [50, 260]
		pos_y = 460
		step_type_text_list = ["エンター押下", "スペース押下"]
		if index == 0:
			if self._tab == 0:
				Display.__disp_text(
					self._screen,
					self._font,
					"足踏み入力タイプ…" + step_type_text_list[self._go_type],
					50,
					420)
			step_index = 1
		elif index == 1:
			step_index = 0
		else:
			return response.Response(data=-1, result=code.Code.ARGUMENT_ERROR)

		if self._tab == 0:
			# STEP BUTTON 表示
			if self._step_touch_list[index]:
				self._screen.blit(self._img_list[Index.SET_BUTTON()][type_list[index]+1], (pos_x_list[index], pos_y))
			else:
				self._screen.blit(self._img_list[Index.SET_BUTTON()][type_list[index]], (pos_x_list[index], pos_y))
			if self._go_type == step_index:
				self._screen.blit(self._img_list[Index.SET_BUTTON()][0], (pos_x_list[index], pos_y))
			return response.Response(data=(pos_x_list[index], pos_y), result=code.Code.OK)
		else:
			# STEP BUTTON 非表示
			return response.Response(data=(-1, -1), result=code.Code.OK)

	def disp_volume_slider(self):
		pos_x = 50
		pos_y = 150
		if self._tab == 1:
			# VOLUME SLIDER 表示
			Display.__disp_text(self._screen, self._font, "SE VOLUME", pos_x, pos_y)
			slider = Slider(self._screen, pos_x, pos_y + 45, 400, 10, min=0, max=99, step=1)
			slider.setValue(self._volume)
			slider.draw()
			Display.__disp_text(self._screen, self._font, str(self._volume), pos_x + 425, pos_y + 40)
			return response.Response(data=(50, 180), result=code.Code.OK)
		else:
			# VOLUME SLIDER 非表示
			return response.Response(data=(-1, -1), result=code.Code.OK)

	@staticmethod
	def __disp_text(screen, font, text: str, x: int, y: int):
		text_surface = font.render(text, True, cmn.Colors.black)
		text_rect = text_surface.get_rect(center=(x+text_surface.get_width()/2, y))
		screen.blit(text_surface, text_rect)
