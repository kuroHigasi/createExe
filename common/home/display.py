import pyd.indexHome as index
import pyd.hitJudge as judge


class Display:
    def dispHome(screen, homeFoem, opeForm, posX: int, posY: int):
        img_list = homeFoem.get_img_list()
        screen.blit(img_list[index.HOME()][0], (posX, posY))
        # START
        Display.__dispButton(screen, img_list, opeForm, 2, 50, 300)
        homeFoem.set_start_button(50, 300)
        # LOAD
        Display.__dispButton(screen, img_list, opeForm, 6, 50, 390)
        homeFoem.set_load_button(50, 390)
        # CONFIG
        Display.__dispButton(screen, img_list, opeForm, 10, 50, 580)
        homeFoem.set_config_button(50, 580)
        # EXIT
        Display.__dispButton(screen, img_list, opeForm, 0, 50, 670)
        homeFoem.set_exit_button(50, 670)

    def __dispButton(screen, imgList, opeForm, buttonIndex: int, posX: int, posY: int):
        (x, y) = opeForm.get_mouse()
        if judge.hitJudgeSquare(posX, posY, 200, 80, int(x), int(y)):
            screen.blit(imgList[index.BUTTON()][buttonIndex+1], (posX, posY))
        else:
            screen.blit(imgList[index.BUTTON()][buttonIndex], (posX, posY))
