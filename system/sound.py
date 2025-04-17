import pyd.status as STATUS
import common.home.sound as soundHome
import common.save.sound as sound_save

class Sound:
	def execute(statusForm, systemForm, opeForm):
		homeForm = systemForm.HOME_FORM()
		soundForm = systemForm.SOUND_FORM()
		config_form = systemForm.CONFIG_FORM()
		save_form = systemForm.SAVE_FORM()
		nowStatus = statusForm.NOW_STATUS()
		# ステータス毎 処理分岐
		if nowStatus is STATUS.HOME():
			soundHome.Sound.start(homeForm, opeForm, config_form, soundForm)
		elif nowStatus is STATUS.SAVE():
			sound_save.Sound.execute(sound_save.Sound.create_request_data(soundForm, save_form, opeForm, config_form))
