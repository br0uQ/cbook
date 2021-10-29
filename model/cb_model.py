from model import recipe_parser as rp


class CbModel:
    mypath = "./data/test-recipes/"
    recipes = []

    def load_recipes(self):
        self.recipes = rp.get_recipes(self.mypath)


    def get_recipes(self):
        return self.recipes


    def get_name(self, recipe):
        recipe_dict = rp.read_recipe(recipe)
        return rp.get_name(recipe_dict)
