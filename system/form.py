import dungeon.form as DungeonForm
import common.home.form as HomeForm
import common.config.form as ConfigForm
import common.end.form as EndForm
import common.save.form as SaveForm
import common.sound.form as SoundForm


class SystemForm:
    def __init__(self, flash=[]):
        self.__flash = flash
        self.__DungeonForm = DungeonForm.Form(1)
        self.__ConfigForm = ConfigForm.Form()
        self.__HomeForm = HomeForm.Form()
        self.__EndForm = EndForm.Form()
        self.__SaveForm = SaveForm.Form()
        self.__SoundForm = SoundForm.Form()

    def FLASH(self, index=0):
        return self.__flash[index].flash()

    def countupFlash(self):
        for i in range(0, len(self.__flash), 1):
            self.__flash[i].countup()

    def DUNGEON_FORM(self):
        return self.__DungeonForm

    def CONFIG_FORM(self):
        return self.__ConfigForm

    def HOME_FORM(self):
        return self.__HomeForm

    def END_FORM(self):
        return self.__EndForm

    def SAVE_FORM(self):
        return self.__SaveForm

    def SOUND_FORM(self):
        return self.__SoundForm
