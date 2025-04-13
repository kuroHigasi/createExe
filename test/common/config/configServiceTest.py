import unittest
import common.config.service.action as service_action
import common.layer.request.request as request


class TestServiceAction1(unittest.TestCase):
	def setUp(self):
		temp_data_list = []
		temp_data_list.insert(0, 180)  # マウス位置 X
		temp_data_list.insert(1, -1)  # クリック マウス位置 X
		temp_data_list.insert(2, -1)  # クリック マウス位置 Y
		temp_data_list.insert(3, False)  # 方向キー設定1 選択状態
		temp_data_list.insert(4, False)  # 方向キー設定2 選択状態
		temp_data_list.insert(5, False)  # 直進キー設定1 選択状態
		temp_data_list.insert(6, False)  # 直進キー設定2 選択状態
		temp_data_list.insert(7, False)  # 足踏みキー設定1 選択状態
		temp_data_list.insert(8, False)  # 足踏みキー設定2 選択状態
		temp_data_list.insert(9, False)  # タブ選択1 選択状態
		temp_data_list.insert(10, False)  # タブ選択2 選択状態
		temp_data_list.insert(11, 1)  # 方向キー設定 現在状態
		temp_data_list.insert(12, 0)  # 直進キー設定 現在状態
		temp_data_list.insert(13, 0)  # タブ選択 現在状態
		self.data_list = temp_data_list

	def test_tab(self):
		service = service_action.Action(request.Request(data=self.data_list))
		res = service.select_tab()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_way(self):
		service = service_action.Action(request.Request(data=self.data_list))
		res = service.select_way_key_type()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_go(self):
		service = service_action.Action(request.Request(data=self.data_list))
		res = service.select_go_key_type()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_step(self):
		service = service_action.Action(request.Request(data=self.data_list))
		res = service.select_step_key_type()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_volume(self):
		service = service_action.Action(request.Request(data=self.data_list))
		res = service.select_volume()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)


class TestServiceAction2(unittest.TestCase):
	def setUp(self):
		temp_data_list = []
		temp_data_list.insert(0, 180)  # マウス位置 X
		temp_data_list.insert(1, -1)  # クリック マウス位置 X
		temp_data_list.insert(2, -1)  # クリック マウス位置 Y
		temp_data_list.insert(3, False)  # 方向キー設定0 選択状態
		temp_data_list.insert(4, True)  # 方向キー設定1 選択状態
		temp_data_list.insert(5, False)  # 直進キー設定0 選択状態
		temp_data_list.insert(6, True)  # 直進キー設定1 選択状態
		temp_data_list.insert(7, False)  # 足踏みキー設定0 選択状態
		temp_data_list.insert(8, True)  # 足踏みキー設定1 選択状態
		temp_data_list.insert(9, False)  # タブ選択0 選択状態
		temp_data_list.insert(10, True)  # タブ選択1 選択状態
		temp_data_list.insert(11, 0)  # 方向キー設定 現在状態
		temp_data_list.insert(12, 1)  # 直進キー設定 現在状態
		temp_data_list.insert(13, 1)  # タブ選択 現在状態
		self.data_list = temp_data_list

	def test_tab(self):
		service = service_action.Action(request.Request(data=self.data_list))
		res = service.select_tab()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), False)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_way(self):
		service = service_action.Action(request.Request(data=self.data_list))
		res = service.select_way_key_type()
		self.assertEquals(res.is_ok(), True)
		self.assertEquals(res.is_do_nothing(), False)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, 1)

	def test_go(self):
		service = service_action.Action(request.Request(data=self.data_list))
		res = service.select_go_key_type()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), False)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_step(self):
		service = service_action.Action(request.Request(data=self.data_list))
		res = service.select_step_key_type()
		self.assertEquals(res.is_ok(), True)
		self.assertEquals(res.is_do_nothing(), False)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, 0)

	def test_volume(self):
		service = service_action.Action(request.Request(data=self.data_list))
		res = service.select_volume()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)


unittest.main(argv=['first-arg-is-ignored'], exit=False)
