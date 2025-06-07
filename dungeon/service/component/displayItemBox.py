import pyd.indexDungeon as INDEX
import common.layer.response.response as response
import common.layer.code.code as code
import common.common as cmn
import pyd.typeItem as ITEM


class DisplayItemBox:
	def __init__(self, screen, img_list, item_list, num_list, use_list, touch_list, item_font):
		self._screen = screen
		self._img_list = img_list
		self._box_item_list = item_list
		self._box_num_list = num_list
		self._box_use_list = use_list
		self._box_touch_list = touch_list
		self._box_num = len(item_list)
		self._item_font = item_font

	def execute(self, pos_x, pos_y, mouse_x, mouse_y):
		screen = self._screen
		item_font = self._item_font
		color_ = cmn.Colors.black
		pos_x_list = [pos_x, pos_x+60, pos_x+120]
		img_list = self._img_list
		ret_data = (-1, -1, -1)
		disp_item_name_flag = False
		for index in range(0, self._box_num, 1):
			item = self._box_item_list[index]
			item_num = self._box_num_list[index]
			text = ""
			screen.blit(img_list[INDEX.BOX()][0], (pos_x_list[index], pos_y))
			if item != -1:
				screen.blit(img_list[INDEX.ITEM()][item], (pos_x_list[index]+5, pos_y+5))
			if self._box_use_list[index]:
				screen.blit(img_list[INDEX.BOX()][1], (pos_x_list[index], pos_y))
				ret_data = (index, -1, -1)
			else:
				if item != -1:
					self.__disp_text(screen, item_font, str(item_num), pos_x_list[index]+2, pos_y+10, color_)
					ret_data = (index, pos_x_list[index], pos_y)
			if self._box_touch_list[index]:
				text = ITEM.getText(item) + ":" + str(item_num)
				if not self._box_use_list[index]:
					screen.blit(img_list[INDEX.BOX_TAG()][0], (pos_x_list[index], pos_y-20))
			if text != "":
				disp_item_name_flag = True
				disp_item_name = text
		# アイテム名 表示
		if disp_item_name_flag:
			self.__disp_text(screen, item_font, disp_item_name, mouse_x+10, mouse_y-10, color_)
		return response.Response(data=ret_data, result=code.Code.OK)

	@staticmethod
	def __disp_text(screen, font, text, x, y, color=cmn.Colors.white):
		text_surface = font.render(text, True, color)
		text_rect = text_surface.get_rect(center=(x+text_surface.get_width() / 2, y))
		screen.blit(text_surface, text_rect)
