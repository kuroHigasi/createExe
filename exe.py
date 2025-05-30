import pygame
import pygame.locals
import pygame_widgets

# 共通処理
import common.debug.debug as dbg
import common.common as cmn
# SySTEM
from system.debug import Debug
from system.display import Display
from system.action import Action
from system.status import Status
from system.sound import Sound
# FORM
import common.operation.form as OperationForm
import system.form as SystemForm
import common.status.form as StatusForm
# DEFINE
import pyd.status as STATUS

# Initialize Pygame
pygame.init()
dbg.init()
screen = pygame.display.set_mode(cmn.TEST_SIZE)
pygame.display.set_caption("game")
pygame.mixer.init()
screen.fill(cmn.Colors.black)
# Game variables
clock = pygame.time.Clock()

# マウスカーソル表示
pygame.mouse.set_visible(True)

# マウスカーソル初期位置
# 変数初期化
pygame.mouse.set_pos(800/2, 600/2)


class Main:
    def __init__(self):
        # FORM
        self.__OperationForm = OperationForm.OperationForm()
        self.__SystemForm = SystemForm.SystemForm([cmn.Flash(5, 2), cmn.Flash(15, 3)])
        self.__StatusForm = StatusForm.Form(STATUS.HOME())

    def DISP(self, screen):
        Display.execute(screen, self.__StatusForm, self.__SystemForm, self.__OperationForm)

    def MOUSE(self, x, y):
        self.__OperationForm.set_mouse(x, y)

    def EXIT_CHECK(self):
        return self.__StatusForm.now_status != STATUS.EXIT()

    def EXIT_SET(self):
        self.__StatusForm.update_status(STATUS.EXIT())

    def KEYBOAD(self, key):
        if self.__SystemForm.CONFIG_FORM().get_way_key_type() == 1:
            if key == pygame.K_LEFT:
                self.__OperationForm.left_on()
            if key == pygame.K_RIGHT:
                self.__OperationForm.right_on()
            if key == pygame.K_UP:
                self.__OperationForm.up_on()
            if key == pygame.K_DOWN:
                self.__OperationForm.down_on()
        elif self.__SystemForm.CONFIG_FORM().get_way_key_type() == 0:
            if key == pygame.K_a:
                self.__OperationForm.left_on()
            if key == pygame.K_d:
                self.__OperationForm.right_on()
            if key == pygame.K_w:
                self.__OperationForm.up_on()
            if key == pygame.K_s:
                self.__OperationForm.down_on()
        else:
            dbg.ERROR_LOG("[main.KEYBOAD]存在しないKEY_TYPE" + str(self.__SystemForm.CONFIG_FORM().way_key_type()))
        # 前進ボタン
        if key == pygame.K_SPACE:
            self.__OperationForm.space_pn()
        if key == pygame.K_RETURN:
            self.__OperationForm.enter_on()

    def CLICK(self, left, right):
        if left:
            self.__OperationForm.left_click_on()
        else:
            self.__OperationForm.left_click_off()
        if right:
            self.__OperationForm.right_click_on()
        else:
            self.__OperationForm.right_click_off()

    def RESET(self):
        self.__OperationForm.reset()
        Status.init(self.__StatusForm, self.__SystemForm, self.__OperationForm)

    def COUNT(self):
        self.__SystemForm.countupFlash()

    def DEBUG(self, key):
        Debug.execute(self.__StatusForm, self.__SystemForm, key)

    def ACTION(self):
        Action.execute(self.__StatusForm, self.__SystemForm, self.__OperationForm)

    def STATUS(self):
        Status.execute(self.__StatusForm, self.__SystemForm, self.__OperationForm)

    def SOUND(self):
        Sound.execute(self.__StatusForm, self.__SystemForm, self.__OperationForm)


main = Main()

# Game loop
while main.EXIT_CHECK():
    main.RESET()
    for event in pygame.event.get():
        main.RESET()
        if event.type == pygame.MOUSEMOTION:
            (x, y) = event.pos
            main.MOUSE(x, y)
        if event.type == pygame.QUIT:
            main.EXIT_SET()
        if event.type == pygame.locals.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main.EXIT_SET()
            main.KEYBOAD(event.key)
            main.DEBUG(event.key)
        main.ACTION()
        pygame_widgets.update(event)
    (left, middle, right) = pygame.mouse.get_pressed()
    main.CLICK(left, right)
    main.SOUND()
    main.STATUS()
    main.COUNT()
    main.DISP(screen)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
