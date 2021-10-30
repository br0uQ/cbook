from controller.rc_controller import RvController
from os.path import split
from view import recipe_button as rb
import os



class MwController:
    
    
    def __init__(self, model, window):
        self.model = model
        self.window = window
        self.rv_controller = RvController(model, window)

        self.model.load_recipes()
        self.read_recipes()
        self.window.backButton.clicked.connect(self.open_recipe_list)


    def create_recipe_button(self, recipe, recipe_dict):
        name = self.model.get_name(recipe_dict)
        image_path = self.get_image_path(recipe)
        recipe_button = rb.RecipeButton()
        recipe_button.set_name(name)
        recipe_button.set_image(image_path)
        recipe_button.recipe = recipe
        recipe_button.add_cb(self.open_recipe)
        return recipe_button


    def read_recipes(self):
        recipes = self.model.get_recipes()
        self.categories = []
        for r in recipes:
            rd = self.model.get_recipe_dict(r)
            #kategorien = self.model.get_kategorien(rd)
            self.window.add_recipe(self.create_recipe_button(r, rd))
        self.window.recipeList.layout().addStretch()


    def get_image_path(self, recipe_path):
        return os.path.dirname(recipe_path) + "/thumb.jpg"


    def open_recipe(self, recipe):
        self.rv_controller.load_recipe(recipe)


    def open_recipe_list(self):
        self.window.stackedWidget.setCurrentIndex(0)
