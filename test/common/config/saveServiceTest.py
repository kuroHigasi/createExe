import unittest
from unittest.mock import MagicMock
import common.save.service.action as service_action
import common.layer.request.save.saveActionRequest as saveRequest

import common.common as cmn


def convert(text):
	return ""

class TestSave(unittest.TestCase):
	def setUp(self):
		self.request = saveRequest.SaveActionRequest(
			True,  # SAVE1 クリック
			False,  # SAVE2 クリック
			False,  # SAVE3 クリック
			False,  # LOAD1 クリック
			False,  # LOAD2 クリック
			False,  # LOAD3 クリック
			False,  # DELETE1 クリック
			False,  # DELETE2 クリック
			False,  # DELETE3 クリック
			"1,2,3"  # INPUT_DATA クリック
		)

	def test_save1(self):
		cmn.SaveMethod.save = MagicMock(return_value=True)
		cmn.SaveMethod.load = MagicMock(return_value="")
		service = service_action.Action(self.request)
		res = service.save(0, convert)
		self.assertEquals(res.is_ok(), True)
		self.assertEquals(res.is_do_nothing(), False)
		self.assertEquals(res.is_not_ok(), True)
		self.assertEquals(res.data, ['', '', ''])


unittest.main(argv=['first-arg-is-ignored'], exit=False)
