import common.save.service.display as sub_display
import common.layer.request.saveDisplayRequest as saveDisplayRequest
import common.save.form.form as form


class Display:
    @staticmethod
    def execute(save_form, request):
        service = sub_display.Display(request)
        res_back = service.disp_back_button()
        if res_back.is_ok():
            x, y = res_back.data
            save_form.set_back_button(x, y)

        res_home = service.disp_home_button()
        if res_home.is_ok():
            x, y = res_home.data
            save_form.set_home_button(x, y)


        for index in (0, 2, 1):
            service.disp_list(index)
            res_save = service.valid_save_button(index)
            res_load = service.valid_load_button(index)
            res_delete = service.valid_delete_button(index)
            service.disp_list_text(index)

            if res_save.is_ok():
                x, y = res_save.data
                save_form.set_save_list(index, x, y)

            if res_load.is_ok():
                x, y = res_load.data
                save_form.set_load_list(index, x, y)

            if res_delete.is_ok():
                x, y = res_delete.data
                save_form.set_delete_list(index, x, y)

    @staticmethod
    def create_request_data(screen, save_form, ope_form):
        x, y = ope_form.get_mouse()
        disp_list = [save_form.DISP_SAVE_LIST(0),
                     save_form.DISP_SAVE_LIST(1),
                     save_form.DISP_SAVE_LIST(2)]
        return saveDisplayRequest.SaveDisplayRequest(
            screen,
            save_form.font(),
            save_form.img_list(),
            x,
            y,
            save_form.get_input_data(),
            disp_list,
            save_form.get_back_button_width(),
            save_form.get_back_button_height(),
            save_form.get_home_button_width(),
            save_form.get_home_button_height(),
            700,
            150,
            save_form.get_save_list_width(0),
            save_form.get_save_list_height(0)
        )

