import os


class RvController:
    

    def __init__(self, model, window):
        self.model = model
        self.window = window



    def get_fullimage_path(self, recipe_path):
        return os.path.dirname(recipe_path) + "/full.jpg"


    def load_recipe(self, recipe):
        # fill recipe data
        recipe_dict = self.model.get_recipe_dict(recipe)
        self.window.nameLabel.setText(self.model.get_name(recipe_dict))
        self.window.set_image(self.get_fullimage_path(recipe))

        instructions = self.model.get_instructions(recipe_dict)
        self.window.anleitungLabel.setText(self.get_instructions_string(instructions))
        self.window.beschreibungLabel.setText(self.model.get_description(recipe_dict))
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


    def get_instructions_string(self, instructions):
        instruction_text = ""
        for i in instructions:
            instruction_text = instruction_text + i + "\n\n\n"
        return instruction_text


    def get_label_string(self, labels):
        ret = ""
        for l in labels:
            ret = ret + l.split('_')[1] + ", "
        ret = ret[:-2]
        return ret


    def set_ingredients(self, ingredients):
        ings = self.get_ingredients(ingredients)
        self.window.mengeLabel.setText(ings[0])
        self.window.einheitLabel.setText(ings[1])
        self.window.zutatLabel.setText(ings[2])


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


