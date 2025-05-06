import dungeon.abstract.abstractSound as abstractSound
import dungeon.layer.request.dungeonSoundRequest as dungeonSoundRequest
import dungeon.service.sound as service_sound
import dungeon.form.form as main_form


class Sound(abstractSound.AbstractSound):
	@staticmethod
	def execute(dungeon_form, request):
		service = service_sound.Sound(request)
		res = service.start()
		if res.is_ok():
			dungeon_form.walk_flag = False

	@staticmethod
	def create_request_data(sound_form, dungeon_form: main_form.Form, ope_form, config_form):
		return dungeonSoundRequest.DungeonSoundRequest(
			sound_form.sound_list,
			config_form.get_volume(),
			dungeon_form.walk_flag
		)
