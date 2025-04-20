import common.layer.request.save.saveSoundRequest as saveSoundRequest
import pyd.hitJudge as hitJudge
import common.save.service.sound as sub_sound
import common.abstract.save.abstractSound as abstractSound

class Sound(abstractSound.AbstractSound):
	@staticmethod
	def execute(request):
		service = sub_sound.Sound(request)
		service.start()

	@staticmethod
	def create_request_data(sound_form, save_form, ope_form, config_form):
		x, y = ope_form.get_mouse()
		save1_x, save1_y, save1_width, save1_height = save_form.get_save_list(0)
		save2_x, save2_y, save2_width, save2_height = save_form.get_save_list(1)
		save3_x, save3_y, save3_width, save3_height = save_form.get_save_list(2)
		save1_touch = hitJudge.hitJudgeSquare(save1_x, save1_y, save1_width, save1_height, x, y)
		save2_touch = hitJudge.hitJudgeSquare(save2_x, save2_y, save2_width, save2_height, x, y)
		save3_touch = hitJudge.hitJudgeSquare(save3_x, save3_y, save3_width, save3_height, x, y)
		load1_x, load1_y, load1_width, load1_height = save_form.get_load_list(0)
		load2_x, load2_y, load2_width, load2_height = save_form.get_load_list(1)
		load3_x, load3_y, load3_width, load3_height = save_form.get_load_list(2)
		load1_touch = hitJudge.hitJudgeSquare(load1_x, load1_y, load1_width, load1_height, x, y)
		load2_touch = hitJudge.hitJudgeSquare(load2_x, load2_y, load2_width, load2_height, x, y)
		load3_touch = hitJudge.hitJudgeSquare(load3_x, load3_y, load3_width, load3_height, x, y)
		delete1_x, delete1_y, delete1_width, delete1_height = save_form.get_delete_list(0)
		delete2_x, delete2_y, delete2_width, delete2_height = save_form.get_delete_list(1)
		delete3_x, delete3_y, delete3_width, delete3_height = save_form.get_delete_list(2)
		delete1_touch = (
			hitJudge.hitJudgeSquare(delete1_x, delete1_y, delete1_width, delete1_height, x, y))
		delete2_touch = (
			hitJudge.hitJudgeSquare(delete2_x, delete2_y, delete2_width, delete2_height, x, y))
		delete3_touch = (
			hitJudge.hitJudgeSquare(delete3_x, delete3_y, delete3_width, delete3_height, x, y))
		return saveSoundRequest.SaveActionRequest(
			sound_form.judge_repeat(0, save1_touch),
			sound_form.judge_repeat(1, save2_touch),
			sound_form.judge_repeat(2, save3_touch),
			sound_form.judge_repeat(3, load1_touch),
			sound_form.judge_repeat(4, load2_touch),
			sound_form.judge_repeat(5, load3_touch),
			sound_form.judge_repeat(6, delete1_touch),
			sound_form.judge_repeat(7, delete2_touch),
			sound_form.judge_repeat(8, delete3_touch),
			sound_form.sound_list,
			config_form.get_volume()
			)
