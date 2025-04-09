import pyd.status as STATUS
import common.home.sound as soundHome

class Sound:
	def execute(statusForm, systemForm, opeForm):
		homeForm = systemForm.HOME_FORM()
		soundForm = systemForm.SOUND_FORM()
		nowStatus = statusForm.NOW_STATUS()
		# ステータス毎 処理分岐
		if nowStatus is STATUS.HOME():
			soundHome.Sound.start(homeForm, opeForm, soundForm)
