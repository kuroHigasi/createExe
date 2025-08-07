import pygame.locals
import pygame_widgets
# 共通処理
import common.debug.debug as dbg
import common.common as cmn
import system.main as main


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

main = main.Main()

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
