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


    def set_ingredients(self, ingredients):
        amount = ""
        unit = ""
        ingredient = ""
        for i in ingredients:
            print(i)
            if len(i.split(';')) >= 3:
                amount = amount + i.split(';')[0] + "\n"
                unit = unit + i.split(';')[1] + "\n"
                ingredient = ingredient + i.split(';')[2] + "\n"
            elif len(i.split()) >= 3:
                amount = amount + i.split()[0] + "\n"
                unit = unit + i.split()[1] + "\n"
                ingredient = ingredient + i.split()[2] + "\n"
        print(amount)
        self.window.mengeLabel.setText(amount)
        print(unit)
        self.window.einheitLabel.setText(unit)
        print(ingredient)
        self.window.zutatLabel.setText(ingredient)


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

        # open recipe view
        self.window.stackedWidget.setCurrentIndex(1)
        print(recipe)


    def open_recipe_list(self):
        self.window.stackedWidget.setCurrentIndex(0)
