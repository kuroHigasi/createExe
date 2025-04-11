import common.button.form as button_form


class Form:
	def __init__(self):
		# OK BUTTON
		self._ok_button = button_form.Form(-1, -1, 200, 80)
		# BACK BUTTON
		self._back_button = button_form.Form(-1, -1, 200, 80)
		# WAY BUTTON(方向キー入力タイプ選択)
		self._way_button_list = \
			[button_form.Form(-1, -1, 200, 80), button_form.Form(-1, -1, 200, 80)]
		# GO BUTTON(前進キー入力タイプ選択)
		self._go_button_list = \
			[button_form.Form(-1, -1, 200, 80), button_form.Form(-1, -1, 200, 80)]
		# STEP BUTTON(足踏みキー入力タイプ選択)
		self._step_button_list = \
			[button_form.Form(-1, -1, 200, 80), button_form.Form(-1, -1, 200, 80)]
		# TAB
		self._tab_list = \
			[button_form.Form(-1, -1, 200, 25), button_form.Form(-1, -1, 200, 25)]

	def set_ok_button_pos(self, x, y):
		self._ok_button.x = x
		self._ok_button.y = y

	def hidden_ok_button(self):
		self._ok_button.x= -1
		self._ok_button.y= -1

	def get_ok_button(self):
		return \
			self._ok_button.x, \
			self._ok_button.y, \
			self._ok_button.width, \
			self._ok_button.height

	def set_back_button_pos(self, x, y):
		self._back_button.x = x
		self._back_button.y = y

	def hidden_back_button(self):
		self._back_button.x = -1
		self._back_button.y = -1

	def get_back_button(self):
		return \
			self._back_button.x, \
			self._back_button.y, \
			self._back_button.width, \
			self._back_button.height

	def set_way_button_pos(self, index, x, y):
		self._way_button_list[index].x = x
		self._way_button_list[index].y = y

	def hidden_way_button(self, index):
		self._way_button_list[index].x = -1
		self._way_button_list[index].y = -1

	def get_way_button(self, index):
		return \
			self._way_button_list[index].x, \
			self._way_button_list[index].y, \
			self._way_button_list[index].width, \
			self._way_button_list[index].height

	def set_go_button_pos(self, index, x, y):
		self._go_button_list[index].x = x
		self._go_button_list[index].y = y

	def hidden_go_button(self, index):
		self._go_button_list[index].x = -1
		self._go_button_list[index].y = -1

	def get_go_button(self, index):
		return \
			self._go_button_list[index].x, \
			self._go_button_list[index].y, \
			self._go_button_list[index].width, \
			self._go_button_list[index].height

	def set_step_button_pos(self, index, x, y):
		self._step_button_list[index].x = x
		self._step_button_list[index].y = y

	def hidden_step_button(self, index):
		self._step_button_list[index].x = -1
		self._step_button_list[index].y = -1

	def get_step_button(self, index):
		return \
			self._step_button_list[index].x, \
			self._step_button_list[index].y, \
			self._step_button_list[index].width, \
			self._step_button_list[index].height

	def set_tab_button_pos(self, index, x, y):
		self._tab_list[index].x = x
		self._tab_list[index].y = y

	def hidden_tab_button(self, index):
		self._tab_list[index].x = -1
		self._tab_list[index].y = -1

	def get_tab_button(self, index):
		return \
			self._tab_list[index].x, \
			self._tab_list[index].y, \
			self._tab_list[index].width, \
			self._tab_list[index].height
