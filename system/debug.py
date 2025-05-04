import pyd.status as STATUS
import common.debug.debug as dbg
import dungeon.debug as dun_dbg
import common.status.form as status_form_
import system.form as system_form_
import pygame


class Debug:
    @staticmethod
    def execute(status_form: status_form_.Form, system_form: system_form_, key):
        nowStatus = status_form.now_status
        homeForm = system_form.HOME_FORM()
        dungeon_form = system_form.DUNGEON_FORM()
        if key == pygame.K_x:
            if nowStatus == STATUS.DUNGEON():
                dun_dbg.Debug.show_situation(dungeon_form)
        elif key == pygame.K_c:
            sound_list = homeForm.sound_list
            dbg.ERROR_LOG(str(list[0]))
            pygame.mixer.music.load(sound_list[0])
            pygame.mixer.music.play()
        else:
            if nowStatus == STATUS.DUNGEON():
                dun_dbg.Debug.show_position(dungeon_form)
                dun_dbg.Debug.show_way(dungeon_form)
                dun_dbg.Debug.show_view(dungeon_form)
                dun_dbg.Debug.show_situation(dungeon_form)
