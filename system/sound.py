import pyd.status as STATUS
import common.home.sound as soundHome
import common.config.sound as sound_config
import common.save.sound as sound_save

class Sound:
	def execute(statusForm, systemForm, ope_form):
		home_form = systemForm.HOME_FORM()
		sound_form = systemForm.SOUND_FORM()
		config_form = systemForm.CONFIG_FORM()
		save_form = systemForm.SAVE_FORM()
		now_status = statusForm.now_status
		# ステータス毎 処理分岐
		if now_status is STATUS.HOME():
			request_home = soundHome.Sound.create_request_data(sound_form, home_form, ope_form, config_form)
			soundHome.Sound.execute(request_home)
		elif now_status is STATUS.CONFIG():
			request_config = sound_config.Sound.create_request_data(sound_form, config_form, ope_form)
			sound_config.Sound.execute(config_form, request_config)
		elif now_status is STATUS.SAVE():
			request_save = sound_save.Sound.create_request_data(sound_form, save_form, ope_form, config_form)
			sound_save.Sound.execute(request_save)
