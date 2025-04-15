import unittest
import common.config.service.action as service_action
import common.layer.request.configActionRequest as configRequest


class TestServiceAction1(unittest.TestCase):
	def setUp(self):
		self.request = configRequest.ConfigActionRequest(
			180,  # マウス位置 X
			-1,  # クリック マウス位置 X
			-1,  # クリック マウス位置 Y
			False,  # 方向キー設定1 選択状態
			False,  # 方向キー設定2 選択状態
			False,  # 直進キー設定1 選択状態
			False,  # 直進キー設定2 選択状態
			False,  # 足踏みキー設定1 選択状態
			False,  # 足踏みキー設定2 選択状態
			False,  # タブ選択1 選択状態
			False,  # タブ選択2 選択状態
			0,  # 方向キー設定 現在状態
			0,  # 直進キー設定 現在状態
			0  # タブ選択 現在状態
		)

	def test_tab(self):
		service = service_action.Action(self.request)
		res = service.select_tab()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_way(self):
		service = service_action.Action(self.request)
		res = service.select_way_key_type()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_go(self):
		service = service_action.Action(self.request)
		res = service.select_go_key_type()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_step(self):
		service = service_action.Action(self.request)
		res = service.select_step_key_type()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_volume(self):
		service = service_action.Action(self.request)
		res = service.select_volume()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)


class TestServiceAction2(unittest.TestCase):
	def setUp(self):
		self.request = configRequest.ConfigActionRequest(
			180,  # マウス位置 X
			-1,  # クリック マウス位置 X
			-1,  # クリック マウス位置 Y
			True,  # 方向キー設定1 選択状態
			False,  # 方向キー設定2 選択状態
			False,  # 直進キー設定1 選択状態
			False,  # 直進キー設定2 選択状態
			False,  # 足踏みキー設定1 選択状態
			False,  # 足踏みキー設定2 選択状態
			False,  # タブ選択1 選択状態
			False,  # タブ選択2 選択状態
			0,  # 方向キー設定 現在状態
			0,  # 直進キー設定 現在状態
			0  # タブ選択 現在状態
		)

	def test_tab(self):
		service = service_action.Action(self.request)
		res = service.select_tab()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_way(self):
		service = service_action.Action(self.request)
		res = service.select_way_key_type()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), False)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_go(self):
		service = service_action.Action(self.request)
		res = service.select_go_key_type()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_step(self):
		service = service_action.Action(self.request)
		res = service.select_step_key_type()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_volume(self):
		service = service_action.Action(self.request)
		res = service.select_volume()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)


class TestServiceAction3(unittest.TestCase):
	def setUp(self):
		self.request = configRequest.ConfigActionRequest(
			180,  # マウス位置 X
			-1,  # クリック マウス位置 X
			-1,  # クリック マウス位置 Y
			False,  # 方向キー設定1 選択状態
			False,  # 方向キー設定2 選択状態
			True,  # 直進キー設定1 選択状態
			False,  # 直進キー設定2 選択状態
			False,  # 足踏みキー設定1 選択状態
			False,  # 足踏みキー設定2 選択状態
			False,  # タブ選択1 選択状態
			False,  # タブ選択2 選択状態
			0,  # 方向キー設定 現在状態
			0,  # 直進キー設定 現在状態
			0  # タブ選択 現在状態
		)

	def test_tab(self):
		service = service_action.Action(self.request)
		res = service.select_tab()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_way(self):
		service = service_action.Action(self.request)
		res = service.select_way_key_type()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_go(self):
		service = service_action.Action(self.request)
		res = service.select_go_key_type()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), False)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_step(self):
		service = service_action.Action(self.request)
		res = service.select_step_key_type()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)

	def test_volume(self):
		service = service_action.Action(self.request)
		res = service.select_volume()
		self.assertEquals(res.is_ok(), False)
		self.assertEquals(res.is_do_nothing(), True)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, -1)


unittest.main(argv=['first-arg-is-ignored'], exit=False)
