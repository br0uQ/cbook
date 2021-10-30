from model import recipe_parser as rp


class CbModel:
    mypath = "./data/test-recipes/"
    recipes = []

    def load_recipes(self):
        self.recipes = rp.get_recipes(self.mypath)


    def get_recipes(self):
        return self.recipes


    def get_recipe_dict(self, recipe):
        return rp.read_recipe(recipe)


    def get_name(self, recipe):
        return rp.get_name(recipe)


    def get_instructions(self, recipe):
        return rp.get_instructions(recipe)
    

    def get_servings(self, recipe):
        return rp.get_servings(recipe)


    def get_label_list(self, recipe, label):
        keywords = rp.get_keywords(recipe).split(',')
        ret = []
        for k in keywords:
            if len(k) > len(label) and k[0:len(label)] == label:
                print("Keyword rightig: " + k)
                ret.append(k)
        return ret


    def get_kategorien(self, recipe):
        return self.get_label_list(recipe, 'k_')


    def get_nahrung(self, recipe):
        return self.get_label_list(recipe, 'n_')


    def get_kohlehydrat(self, recipe):
        return self.get_label_list(recipe, 'kh_')


    def get_ingredients(self, recipe):
        return rp.get_ingredients(recipe)
