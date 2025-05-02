import dungeon.layer.request.dungeonDisplayRequest as dungeonDisplayRequest
import dungeon.service.component.displayRadar as displayRadar
import dungeon.service.component.displayItemBox as displayItemBox
import dungeon.service.component.displayUseItem as displayUseItem
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

	def disp_radar(self):
		img_list = self._img_list
		situation = self._situation
		enemy_pos_list = self._enemy_pos_list
		x = 800
		y = 0
		pos_x = x + 70
		pos_y = y + 40
		self._screen.blit(img_list[INDEX.BOARD_S()][0], (x, y))
		self._screen.blit(img_list[INDEX.TEXT5()][img.Select.TEXT_FLASH(self._text_flash)], (pos_x - 10, pos_y - 20))
		if not self._is_death:
			component_radar = \
				displayRadar.DisplayRadar(self._screen, img_list, situation, enemy_pos_list, self._radar_flash)
			component_radar.execute(pos_x, pos_y)
		return response.Response(data=True, result=code.Code.OK)

	def disp_view(self):
		screen = self._screen
		img_list = self._img_list
		now_view = self._view
		pos_x = 0
		pos_y = 0
		ret_data_list = [None, None]
		if not self._is_death:
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
			# ITEM BOX
			component_disp_box = displayItemBox.DisplayItemBox(
				screen,
				img_list,
				self._box_item_list,
				self._box_num_list,
				self._box_use_list,
				self._box_touch_list,
				self._item_font
			)
			res_box = component_disp_box.execute(pos_x+606, pos_y+526, self._mouse_x, self._mouse_y)
			ret_data_list[0] = res_box.data
			# ITEM USE
			component_disp_use_item = displayUseItem.DisplayUseItem(
				screen,
				img_list,
				self._box_item_list,
				self._box_use_list,
				self._compass_angle
			)
			component_disp_use_item.execute()
		else:
			screen.blit(img_list[INDEX.FLAME()][1], (pos_x, pos_y))
			# RETRY
			self.__disp_button(screen, img_list, 12, self._retry_touch, pos_x+350, pos_y+270)
			ret_data_list[1] = pos_x+350, pos_y+270
		return response.Response(data=ret_data_list, result=code.Code.OK)

	@staticmethod
	def __disp_button(screen, img_list, index, touch, pos_x, pos_y):
		if touch:
			screen.blit(img_list[INDEX.BUTTON()][index+1], (pos_x, pos_y))
		else:
			screen.blit(img_list[INDEX.BUTTON()][index], (pos_x, pos_y))