import common.pyd.status as STATUS
import common.debug.debug as dbg
import pygame


class Debug:
    def execute(statusForm, systemForm, key):
        nowStatus = statusForm.NOW_STATUS()
        dungeonForm = systemForm.DUNGEON_FORM()
        if key == pygame.K_c:
            dbg.LOG("KEY_TYPE=" + str(systemForm.CONFIG_FORM().WAY_KEY_TYPE()))
