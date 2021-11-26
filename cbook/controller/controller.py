from cbook.controller.menu_controller import MenuController
from cbook.controller.recipes_controller import RecipesController


class Controller:


    def __init__(self, model, window):
        self.rc = RecipesController(model, window)
        self.mc = MenuController(model, window)
