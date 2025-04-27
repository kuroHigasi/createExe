import common.config.form.form as form
import common.abstract.config.abstractSound as abstractSound
import common.layer.request.config.configSoundRequest as configSoundRequest
import common.config.service.sound as sub_sound



class Sound(abstractSound.AbstractSound):
	@staticmethod
	def execute(config_form, request: configSoundRequest.ConfigSoundRequest):
		service = sub_sound.Sound(request)
		res_sound = service.start()
		if res_sound.is_ok():
			act_flag, busy_flag = res_sound.data
			if not act_flag:
				config_form.test_playing_flag_off()
			if busy_flag:
				config_form.test_busy_flag_on()
			else:
				config_form.test_busy_flag_off()

	@staticmethod
	def create_request_data(sound_form, config_form: form.Form, ope_form):

		return configSoundRequest.ConfigSoundRequest(
			config_form.get_test_playing_flag(),
			sound_form.sound_list,
			config_form.get_volume()
		)
