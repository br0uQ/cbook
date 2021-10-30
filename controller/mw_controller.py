from PyQt5 import QtCore
from PyQt5.QtWidgets import QCheckBox, QVBoxLayout
from controller.rc_controller import RvController
from os.path import split
from view import recipe_button as rb
import os



class MwController:
    label_filter = []
    
    
    def __init__(self, model, window):
        self.model = model
        self.window = window
        self.rv_controller = RvController(model, window)

        self.model.load_recipes()
        self.read_recipes()
        self.create_checkboxes()
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
        self.recipes = self.model.get_recipes()
        self.categories = []
        self.nahrung = []
        self.kohlehydrate = []
        for r in self.recipes:
            rd = self.model.get_recipe_dict(r)
            self.categories = self.categories + self.model.get_kategorien(rd)
            self.nahrung = self.nahrung + self.model.get_nahrung(rd)
            self.kohlehydrate = self.kohlehydrate + self.model.get_kohlehydrat(rd)
            self.window.add_recipe(self.create_recipe_button(r, rd))
        self.categories = sorted(set(self.categories))
        self.nahrung = sorted(set(self.nahrung))
        self.kohlehydrate = sorted(set(self.kohlehydrate))
        self.label_filter = self.categories + self.nahrung + self.kohlehydrate
        print(self.categories)
        print(self.nahrung)
        print(self.kohlehydrate)
        self.window.recipeList.layout().addStretch()


    def reload_recipes(self):
        for r in self.recipes:
            rd = self.model.get_recipe_dict(r)
            labels = self.model.get_kategorien(rd) + self.model.get_nahrung(rd) + self.model.get_kohlehydrat(rd)
            for l in labels:
                if l in self.label_filter:
                    for b in self.window.get_recipe_buttons():
                        print(b.text())


    def filter_label(self, state, label):
        if QtCore.Qt.Checked == state:
            print("Checked")
            print(self.label_filter)
            if label not in self.label_filter:
                self.label_filter.append(label)
            print(self.label_filter)
        else:
            print("Unchecked")
            print(self.label_filter)
            if label in self.label_filter:
                self.label_filter.remove(label)
            print(self.label_filter)
        self.reload_recipes()


    def create_checkboxes(self):
        for c in self.categories:
            cb = QCheckBox(c.split('_')[1])
            cb.categorie = c
            if c in self.label_filter:
                cb.setChecked(True)
            cb.stateChanged.connect(lambda s, l=c: self.filter_label(s, l))
            self.window.kategorieGroupBox.layout().addWidget(cb)
        for n in self.nahrung:
            cb = QCheckBox(n.split('_')[1])
            cb.nahrung = n
            if n in self.label_filter:
                cb.setChecked(True)
            cb.stateChanged.connect(lambda s, l=n: self.filter_label(s, l))
            self.window.nahrungGroupBox.layout().addWidget(cb)
        for k in self.kohlehydrate:
            cb = QCheckBox(k.split('_')[1])
            cb.kohlehydrat = k
            if k in self.label_filter:
                cb.setChecked(True)
            cb.stateChanged.connect(lambda s, l=k: self.filter_label(s, l))
            self.window.kohlehydrateGroupBox.layout().addWidget(cb)


    def get_image_path(self, recipe_path):
        return os.path.dirname(recipe_path) + "/thumb.jpg"


    def open_recipe(self, recipe):
        self.rv_controller.load_recipe(recipe)


    def open_recipe_list(self):
        self.window.stackedWidget.setCurrentIndex(0)
