from cbook.controller.me_controller import MenuEditController
from cbook.controller.ml_controller import MenuListController


class MenuController:
    

    def __init__(self, model, window):
        self.model = model
        self.window = window

        self.mlc = MenuListController(model, window)
        self.mec = MenuEditController(model, window)

        self.init_buttons()


    def init_buttons(self):
        self.window.btnMenuNew.clicked.connect(self.open_menu_edit)


    def open_menu_edit(self):
        self.window.swMenuViews.setCurrentIndex(1)
