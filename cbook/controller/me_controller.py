class MenuEditController:


    def __init__(self, model, window):
        self.model = model
        self.window = window


        self.init_buttons()


    def init_buttons(self):
        self.window.btnMenuEditAbort.clicked.connect(self.open_menu_list)


    def open_menu_list(self):
        self.window.swMenuViews.setCurrentIndex(0)
