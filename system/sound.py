import pyd.status as STATUS
import common.home.sound as sound_home
import common.config.sound as sound_config
import common.save.sound as sound_save
import dungeon.sound as sound_dungeon


class Sound:
	@staticmethod
	def execute(status_form, system_form, ope_form):
		home_form = system_form.HOME_FORM()
		sound_form = system_form.SOUND_FORM()
		config_form = system_form.CONFIG_FORM()
		save_form = system_form.SAVE_FORM()
		dungeon_form = system_form.DUNGEON_FORM()
		now_status = status_form.now_status
		# ステータス毎 処理分岐
		if now_status is STATUS.HOME():
			request_home = sound_home.Sound.create_request_data(sound_form, home_form, ope_form, config_form)
			sound_home.Sound.execute(request_home)
		elif now_status is STATUS.CONFIG():
			request_config = sound_config.Sound.create_request_data(sound_form, config_form, ope_form)
			sound_config.Sound.execute(sound_form, config_form, request_config)
		elif now_status is STATUS.DUNGEON():
			request_dungeon = sound_dungeon.Sound.create_request_data(sound_form, dungeon_form, ope_form, config_form)
			sound_dungeon.Sound.execute(dungeon_form, request_dungeon)
		elif now_status is STATUS.SAVE():
			request_save = sound_save.Sound.create_request_data(sound_form, save_form, ope_form, config_form)
			sound_save.Sound.execute(request_save)
