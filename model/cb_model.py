from model import recipe_parser as rp


class CbModel:
    mypath = "./data/test-recipes/"

    def load_recipes(self):
        recipes = rp.get_recipes(self.mypath)

        for r in recipes:
            print(r)
            recipe_dict = rp.read_recipe(r)
