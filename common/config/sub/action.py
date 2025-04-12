import common.common as cmn
import common.debug.debug as dbg


class Action:
	def __init__(self, config_form, ope_form):
		left_click = ope_form.isLeftClick()
		x, y = ope_form.MOUSE()
		self._x = x
		self._y = y
		click_x, click_y = ope_form.leftClickMoveMouse()
		self._click_x = click_x
		self._click_y = click_y
		way1_x, way1_y, way1_width, way1_height = config_form.get_way_button(0)
		way2_x, way2_y, way2_width, way2_height = config_form.get_way_button(1)
		go1_x, go1_y, go1_width, go1_height = config_form.get_go_button(0)
		go2_x, go2_y, go2_width, go2_height = config_form.get_go_button(1)
		step1_x, step1_y, step1_width, step1_height = config_form.get_step_button(0)
		step2_x, step2_y, step2_width, step2_height = config_form.get_step_button(1)
		tab1_x, tab1_y, tab1_width, tab1_height = config_form.get_tab_button(0)
		tab2_x, tab2_y, tab2_width, tab2_height = config_form.get_tab_button(1)
		self._way_key_type1_click = \
			cmn.Judge.click(way1_x, way1_y, way1_width, way1_height, x, y, click_x, click_y, left_click)
		self._way_key_type2_click = \
			cmn.Judge.click(way2_x, way2_y, way2_width, way2_height, x, y, click_x, click_y, left_click)
		self._go_key_type1_click = \
			cmn.Judge.click(go1_x, go1_y, go1_width, go1_height, x, y, click_x, click_y, left_click)
		self._go_key_type2_click = \
			cmn.Judge.click(go2_x, go2_y, go2_width, go2_height, x, y, click_x, click_y, left_click)
		self._step_key_type1_click = \
			cmn.Judge.click(step1_x, step1_y, step1_width, step1_height, x, y, click_x, click_y, left_click)
		self._step_key_type2_click = \
			cmn.Judge.click(step2_x, step2_y, step2_width, step2_height, x, y, click_x, click_y, left_click)
		self._tab1_click = \
			cmn.Judge.click(tab1_x, tab1_y, tab1_width, tab1_height, x, y, click_x, click_y, left_click)
		self._tab2_click = \
			cmn.Judge.click(tab2_x, tab2_y, tab2_width, tab2_height, x, y, click_x, click_y, left_click)
		self._way_key_type = config_form.get_way_key_type()
		self._go_key_type = config_form.get_go_key_type()
		self._tab = config_form.tab

	def set_way_key_type(self, config_form):
		if self._way_key_type != 0 and self._way_key_type1_click:
			config_form.set_way_key_type(0)
		elif self._way_key_type != 1 and self._way_key_type2_click:
			config_form.set_way_key_type(1)
		elif self._way_key_type1_click or self._way_key_type2_click:
			dbg.LOG("[ConfigAction._set_way_key_type]" + str(self._way_key_type) + "再設定")
			if self._way_key_type < 0 or 1 < self._way_key_type:
				dbg.ERROR_LOG("[ConfigAction._set_way_key_type]存在しないKeyType")

	def set_go_key_type(self, config_form):
		if self._go_key_type != 0 and self._go_key_type1_click:
			config_form.set_go_key_type(0)
		elif self._go_key_type != 1 and self._go_key_type2_click:
			config_form.set_go_key_type(1)
		elif self._go_key_type1_click or self._go_key_type2_click:
			dbg.LOG("[ConfigAction._set_go_key_type]" + str(self._go_key_type) + "再設定")
			if self._go_key_type < 0 or 2 < self._go_key_type:
				dbg.ERROR_LOG("[ConfigAction._set_go_key_type]存在しないKeyType")

	def set_step_key_type(self, config_form):
		if self._go_key_type != 1 and self._step_key_type1_click:
			config_form.set_go_key_type(1)
		elif self._go_key_type != 0 and self._step_key_type2_click:
			config_form.set_go_key_type(0)
		elif self._step_key_type1_click or self._step_key_type2_click:
			dbg.LOG("[ConfigAction._set_step_key_type]" + str(self._go_key_type) + "再設定")
			if self._go_key_type < 0 or 2 < self._go_key_type:
				dbg.ERROR_LOG("[ConfigAction._set_step_key_type]存在しないKeyType")

	def set_tab(self, config_form):
		if self._tab != 0 and self._tab1_click:
			config_form.tab = 0
		elif self._tab != 1 and self._tab2_click:
			config_form.tab = 1
		elif self._tab1_click or self._tab2_click:
			dbg.LOG("[ConfigAction._set_tab]" + str(self._tab) + "再設定")
			if self._tab < 0 or 2 < self._tab:
				dbg.ERROR_LOG("[ConfigAction._set_tab]存在しないKeyType")

	def set_volume(self, config_form):
		if 180 <= self._click_y <= 210 and 50 <= self._click_x <= 450:
			if 50 <= self._x <= 450:
				config_form.set_volume(int((self._x - 50) / 4))
			elif self._x < 50:
				config_form.set_volume(0)
			elif 450 < self._x:
				config_form.set_volume(100)
