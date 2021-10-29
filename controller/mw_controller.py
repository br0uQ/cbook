from view import recipe_button as rb
import os



class MwController():
    
    
    def __init__(self, model, window):
        self.model = model
        self.window = window

        self.model.load_recipes()
        self.read_recipes()


    def read_recipes(self):
        recipes = self.model.get_recipes()
        for r in recipes:
            name = self.model.get_name(r)
            print(name)
            image_path = self.get_image_path(r)
            print(image_path)
            recipe_button = rb.RecipeButton()
            recipe_button.set_name(name)
            recipe_button.set_image(image_path)
            recipe_button.recipe = r
            recipe_button.add_cb(self.open_recipe)
            self.window.add_recipe(recipe_button)
            #self.window.add_recipe(name)
            #self.window.add_recipe(name)
            #self.window.add_recipe(name)
            #self.window.add_recipe(name)
        self.window.recipeList.layout().addStretch()

    def get_image_path(self, recipe_path):
        return os.path.dirname(recipe_path) + "/thumb.jpg"


    def open_recipe(self, recipe):
        print(recipe)
