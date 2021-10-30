from os.path import split
from view import recipe_button as rb
import os



class MwController():
    
    
    def __init__(self, model, window):
        self.model = model
        self.window = window

        self.model.load_recipes()
        self.read_recipes()
        self.window.backButton.clicked.connect(self.open_recipe_list)


    def read_recipes(self):
        recipes = self.model.get_recipes()
        for r in recipes:
            rd = self.model.get_recipe_dict(r)
            name = self.model.get_name(rd)
            image_path = self.get_image_path(r)
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


    def get_fullimage_path(self, recipe_path):
        return os.path.dirname(recipe_path) + "/full.jpg"


    def get_label_string(self, labels):
        ret = ""
        for l in labels:
            ret = ret + l + ", "
        return ret


    def get_instructions_string(self, instructions):
        instruction_text = ""
        for i in instructions:
            instruction_text = instruction_text + i + "\n\n\n"
        return instruction_text


    def get_ingredients(self, ingredients):
        amount = ""
        unit = ""
        ingredient = ""
        for i in ingredients:
            if len(i.split(';')) >= 3:
                amount = amount + i.split(';')[0] + "\n"
                unit = unit + i.split(';')[1] + "\n"
                ingredient = ingredient + i.split(';')[2] + "\n"
            elif len(i.split()) >= 3:
                amount = amount + i.split()[0] + "\n"
                unit = unit + i.split()[1] + "\n"
                ing = ""
                for e in i.split()[2:]:
                    ing = ing + e + " "
                ingredient = ingredient + ing + "\n"
        amount = amount.replace(",", ".")
        return [amount, unit, ingredient]


    def set_ingredients(self, ingredients):
        ings = self.get_ingredients(ingredients)
        self.window.mengeLabel.setText(ings[0])
        self.window.einheitLabel.setText(ings[1])
        self.window.zutatLabel.setText(ings[2])


    def open_recipe(self, recipe):
        # fill recipe data
        recipe_dict = self.model.get_recipe_dict(recipe)
        self.window.nameLabel.setText(self.model.get_name(recipe_dict))
        self.window.set_image(self.get_fullimage_path(recipe))

        instructions = self.model.get_instructions(recipe_dict)
        self.window.anleitungLabel.setText(self.get_instructions_string(instructions))
        self.window.portionenSpinBox.setValue(self.model.get_servings(recipe_dict))

        # kategorien
        k = self.model.get_kategorien(recipe_dict)
        self.window.kategorieLabel.setText(self.get_label_string(k))

        n = self.model.get_nahrung(recipe_dict)
        self.window.nahrungstypLabel.setText(self.get_label_string(n))

        kh = self.model.get_kohlehydrat(recipe_dict)
        self.window.kohlenhydrateLabel.setText(self.get_label_string(kh))
        self.set_ingredients(self.model.get_ingredients(recipe_dict))

        self.window.portionenSpinBox.valueChanged.connect(lambda: self.change_servings(recipe_dict))

        # open recipe view
        self.window.stackedWidget.setCurrentIndex(1)
        print(recipe)


    def open_recipe_list(self):
        self.window.stackedWidget.setCurrentIndex(0)


    def change_servings(self, recipe_dict):
        default_servings = self.model.get_servings(recipe_dict)
        new_servings = self.window.portionenSpinBox.value()
        ings = self.get_ingredients(self.model.get_ingredients(recipe_dict))
        amounts = ings[0].split('\n')
        new_amounts = ""
        for a in amounts:
            if a != '':

                convert = "%g" % (float(a) * new_servings / default_servings)
                new_amounts = new_amounts + convert + "\n"
        self.window.mengeLabel.setText(new_amounts)
        
