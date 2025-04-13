import pyd.status as STATUS
import common.debug.debug as dbg
import dungeon.debug as dunDbg
import pygame


class Debug:
    def execute(statusForm, systemForm, key):
        nowStatus = statusForm.NOW_STATUS()
        dungeonForm = systemForm.DUNGEON_FORM()
        homeForm = systemForm.HOME_FORM()
        if key == pygame.K_x:
            if (nowStatus == STATUS.DUNGEON()):
                dunDbg.Debug.showSituation(systemForm.DUNGEON_FORM().SITUATION())
        elif key == pygame.K_c:
            list = homeForm.SOUND_LIST()
            dbg.ERROR_LOG(str(list[0]))
            pygame.mixer.music.load(list[0])
            pygame.mixer.music.play()
        else:
            if (nowStatus == STATUS.DUNGEON()):
                dunDbg.Debug.showPos(dungeonForm)
                dunDbg.Debug.showWay(dungeonForm)
                dunDbg.Debug.showView(dungeonForm)
                dunDbg.Debug.showSituation(dungeonForm.SITUATION())
