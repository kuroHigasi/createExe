import dataclasses
import dungeon.form.form as dungeon_form
import common.home.form.form as home_form
import common.config.form.form as ConfigForm
import common.end.form.form as EndForm
import common.save.form.form as SaveForm
import common.sound.form as SoundForm


@dataclasses.dataclass
class Form:
    _flash: list
    _dungeon_form: dungeon_form.Form
    _config_form = ConfigForm.Form()
    _home_form = home_form.Form()
    _end_form = EndForm.Form()
    _save_form = SaveForm.Form()
    _sound_form = SoundForm.Form()

    def __init__(self, flash=[]):
        self._flash = flash
        self._dungeon_form = dungeon_form.Form(1)
        self._config_form = ConfigForm.Form()
        self._home_form = home_form.Form()
        self._end_form = EndForm.Form()
        self._save_form = SaveForm.Form()
        self._sound_form = SoundForm.Form()

    def flash(self, index=0):
        return self._flash[index].flash()

    def countup_flash(self):
        for i in range(0, len(self._flash), 1):
            self._flash[i].countup()

    @property
    def dungeon_form(self):
        return self._dungeon_form

    @property
    def config_form(self):
        return self._config_form

    @property
    def home_form(self):
        return self._home_form

    @property
    def end_form(self):
        return self._end_form

    @property
    def save_form(self):
        return self._save_form

    def sound_form(self):
        return self._sound_form
