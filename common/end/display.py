import pyd.indexEnd as INDEX
import pyd.hitJudge as judge
import common.common as cmn


class Display:
    @staticmethod
    def endDisplay(screen, end_form, ope_form, pos_x: int, pos_y: int):
        img_list = end_form.get_img_list()
        font = end_form.get_font()
        screen.blit(img_list[INDEX.END()][0], (pos_x, pos_y))
        # TEXT
        Display.__disp_text(screen, font, "総行動数:" + str(end_form.get_count()), 50, 200)
        # HOME
        Display.__disp_button(screen, img_list, ope_form, 4, 50, 670)
        end_form.set_home_button(50, 670)

    @staticmethod
    def __disp_button(screen, img_list, ope_form, index: int, pos_x: int, pos_y: int):
        (x, y) = ope_form.get_mouse()
        if judge.hitJudgeSquare(pos_x, pos_y, 200, 80, int(x), int(y)):
            screen.blit(img_list[INDEX.BUTTON()][index+1], (pos_x, pos_y))
        else:
            screen.blit(img_list[INDEX.BUTTON()][index], (pos_x, pos_y))

    @staticmethod
    def __disp_text(screen, font, text: str, x: int, y: int):
        text_surface = font.render(text, True, cmn.Colors.black)
        text_rect = text_surface.get_rect(center=(x+text_surface.get_width()/2, y))
        screen.blit(text_surface, text_rect)
