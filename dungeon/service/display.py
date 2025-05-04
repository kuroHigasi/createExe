import dungeon.layer.request.dungeonDisplayRequest as dungeonDisplayRequest
import dungeon.service.component.displayView as dispView
import dungeon.service.component.displayRadar as displayRadar
import dungeon.service.component.displayItemBox as displayItemBox
import dungeon.service.component.displayUseItem as displayUseItem
import dungeon.service.component.displayButton as displayButton
import dungeon.service.component.displayNumber as displayNumber
import dungeon.service.component.displayText as displayText
import common.layer.response.response as response
import common.layer.code.code as code
import pyd.indexDungeon as INDEX
import pyd.typeItem as ITEM
import pyd.typeAction as ACTION
import dungeon.img as img


class Display:
	def __init__(self, request: dungeonDisplayRequest.DungeonDisplayRequest):
		self._request = request
		self._item_font = request.item_font
		self._event_font = request.event_font
		self._font = request.font
		self._screen = request.screen
		self._img_list = request.img_list
		self._is_death = request.is_death
		self._radar_flash = request.radar_flash
		self._text_flash = request.text_flash
		self._situation = request.situation
		self._view = request.view
		self._enemy_pos_list = request.enemy_pos_list
		self._box_item_list = [
			request.box0_item, request.box1_item, request.box2_item
		]
		self._box_num_list = [
			request.box0_num, request.box1_num, request.box2_num
		]
		self._box_use_list = [
			request.box0_use, request.box1_use, request.box2_use
		]
		self._box_touch_list = [
			request.box0_touch, request.box1_touch, request.box2_touch
		]
		self._mouse_x = request.mouse_x
		self._mouse_y = request.mouse_y
		self._compass_angle = request.compass_angle
		self._retry_touch = request.retry_touch
		self._floor = request.floor
		self._count = request.count
		self._log_num = request.log_num
		self._log_list = request.log_list

	def disp_radar(self):
		x = 800
		y = 0
		pos_x = x + 70
		pos_y = y + 40
		self._screen.blit(self._img_list[INDEX.BOARD_S()][0], (x, y))
		self._screen.blit(self._img_list[INDEX.TEXT5()][img.Select.TEXT_FLASH(self._text_flash)], (pos_x - 10, pos_y - 20))
		if not self._is_death:
			displayRadar.DisplayRadar(
				self._screen,
				self._img_list,
				self._situation,
				self._enemy_pos_list,
				self._radar_flash
			).execute(pos_x, pos_y)
		return response.Response(data=True, result=code.Code.OK)

	def disp_view(self):
		pos_x = 0
		pos_y = 0
		ret_data_list = [None, None]
		if not self._is_death:
			# VIEW
			dispView.DisplayView(
				self._screen,
				self._img_list,
				self._view
			).execute(pos_x, pos_y)
			# ITEM BOX
			res_box = displayItemBox.DisplayItemBox(
				self._screen,
				self._img_list,
				self._box_item_list,
				self._box_num_list,
				self._box_use_list,
				self._box_touch_list,
				self._item_font
			).execute(pos_x+606, pos_y+526, self._mouse_x, self._mouse_y)
			ret_data_list[0] = res_box.data
			# ITEM USE
			displayUseItem.DisplayUseItem(
				self._screen,
				self._img_list,
				self._box_item_list,
				self._box_use_list,
				self._compass_angle
			).execute()
		else:
			self._screen.blit(self._img_list[INDEX.FLAME()][1], (pos_x, pos_y))
			# RETRY
			displayButton.DisplayButton(
				self._screen,
				self._img_list
			).execute(12, self._retry_touch, pos_x+350, pos_y+270)
			ret_data_list[1] = pos_x+350, pos_y+270
		return response.Response(data=ret_data_list, result=code.Code.OK)

	def disp_info(self):
		pos_x = 800
		pos_y = 200
		if self._is_death:
			self._screen(self._img_list[INDEX.BOARD_S()][1], (pos_x, pos_y))
		else:
			component_display_number = displayNumber.DisplayNumber(
				self._screen,
				self._img_list,
				self._font
			)
			self._screen.blit(self._img_list[INDEX.BOARD_S()][0], (pos_x, pos_y))
			# FLOOR
			self._screen.blit(self._img_list[INDEX.TEXT5()][img.Select.TEXT_FLASH(self._text_flash) + 3], (pos_x + 60, pos_y + 20))
			component_display_number.execute(self._floor, pos_x + 90, pos_y+60)
			# ACTION COUNT
			self._screen.blit(self._img_list[INDEX.TEXT6()][img.Select.TEXT_FLASH(self._text_flash) + 3], (pos_x + 27, pos_y + 90))
			self._screen.blit(self._img_list[INDEX.TEXT5()][img.Select.TEXT_FLASH(self._text_flash) + 6], (pos_x + 103, pos_y + 90))
			component_display_number.execute(self._count, pos_x + 90, pos_y+130)
		return response.Response(data=True, result=code.Code.OK)

	def disp_log(self):
		pos_x = 0
		pos_y = 600
		component_disp_text = displayText.DisplayText(
			self._screen,
			self._img_list,
			self._event_font
		)
		self._screen.blit(self._img_list[INDEX.BOARD_M()][0], (pos_x, pos_y))
		text_x = pos_x + 20
		text_y = pos_y + 30
		if self._log_num != 0:
			index = 0
			for log in self._log_list:
				if index < 7:
					component_disp_text.execute(log, text_x, text_y)
					text_y += 23
				index += 1
