# SySTEM
from system.debug import Debug
from system.display import Display
from system.action import Action
from system.status import Status
from system.sound import Sound
# FORM
import common.operation.form as operation_form
import system.form as system_form
import common.status.form as status_form
# DEFINE
import pyd.status as STATUS
# 共通処理
import common.debug.debug as dbg
import common.common as cmn
import pygame


class Main:
	def __init__(self):
		# FORM
		self.__OperationForm = operation_form.OperationForm()
		self.__SystemForm = system_form.Form([cmn.Flash(5, 2), cmn.Flash(15, 3)])
		self.__StatusForm = status_form.Form(STATUS.HOME())

	def DISP(self, screen):
		Display.execute(screen, self.__StatusForm, self.__SystemForm, self.__OperationForm)

	def MOUSE(self, x, y):
		self.__OperationForm.set_mouse(x, y)

	def EXIT_CHECK(self):
		return self.__StatusForm.now_status != STATUS.EXIT()

	def EXIT_SET(self):
		self.__StatusForm.update_status(STATUS.EXIT())

	def KEYBOAD(self, key):
		config_form = self.__SystemForm.config_form
		if config_form.get_way_key_type() == 1:
			if key == pygame.K_LEFT:
				self.__OperationForm.left_on()
			if key == pygame.K_RIGHT:
				self.__OperationForm.right_on()
			if key == pygame.K_UP:
				self.__OperationForm.up_on()
			if key == pygame.K_DOWN:
				self.__OperationForm.down_on()
		elif config_form.get_way_key_type() == 0:
			if key == pygame.K_a:
				self.__OperationForm.left_on()
			if key == pygame.K_d:
				self.__OperationForm.right_on()
			if key == pygame.K_w:
				self.__OperationForm.up_on()
			if key == pygame.K_s:
				self.__OperationForm.down_on()
		else:
			dbg.ERROR_LOG("[main.KEYBOAD]存在しないKEY_TYPE" + str(self.__SystemForm.config_form().way_key_type()))
		# 前進ボタン
		if key == pygame.K_SPACE:
			self.__OperationForm.space_pn()
		if key == pygame.K_RETURN:
			self.__OperationForm.enter_on()

	def CLICK(self, left_click: bool, right_click: bool):
		if left_click:
			self.__OperationForm.left_click_on()
		else:
			self.__OperationForm.left_click_off()
		if right_click:
			self.__OperationForm.right_click_on()
		else:
			self.__OperationForm.right_click_off()

	def RESET(self):
		self.__OperationForm.reset()
		Status.init(self.__StatusForm, self.__SystemForm, self.__OperationForm)

	def COUNT(self):
		self.__SystemForm.countup_flash()

	def DEBUG(self, key):
		Debug.execute(self.__StatusForm, self.__SystemForm, key)

	def ACTION(self):
		Action.execute(self.__StatusForm, self.__SystemForm, self.__OperationForm)

	def STATUS(self):
		Status.execute(self.__StatusForm, self.__SystemForm, self.__OperationForm)

	def SOUND(self):
		Sound.execute(self.__StatusForm, self.__SystemForm, self.__OperationForm)