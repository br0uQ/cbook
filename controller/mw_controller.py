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
        self.window.recipeList.layout().addStretch()


    def show_button(self, recipe_dict):
        show = False
        for c in self.model.get_kategorien(recipe_dict):
            if c in self.label_filter:
                show = True
        if show:
            show = False
            for n in self.model.get_nahrung(recipe_dict):
                if n in self.label_filter:
                    show = True
        if show:
            show = False
            for kh in self.model.get_kohlehydrat(recipe_dict):
                if kh in self.label_filter:
                    show = True
        return show


    def reload_recipes(self):
        buttons = self.window.get_recipe_buttons()
        for b in buttons:
            rd = self.model.get_recipe_dict(b.recipe)
            b.setHidden(not self.show_button(rd))


    def filter_label(self, state, label):
        if QtCore.Qt.Checked == state:
            if label not in self.label_filter:
                self.label_filter.append(label)
        else:
            if label in self.label_filter:
                self.label_filter.remove(label)
        self.reload_recipes()


    def create_checkbox(self, label):
        cb = QCheckBox(label.split('_')[1])
        cb.categorie = label
        if label in self.label_filter:
            cb.setChecked(True)
        cb.stateChanged.connect(lambda s, l=label: self.filter_label(s, l))
        return cb


    def create_checkboxes(self):
        for c in self.categories:
            self.window.kategorieGroupBox.layout().addWidget(self.create_checkbox(c))
        for n in self.nahrung:
            self.window.nahrungGroupBox.layout().addWidget(self.create_checkbox(n))
        for k in self.kohlehydrate:
            self.window.kohlehydrateGroupBox.layout().addWidget(self.create_checkbox(k))


    def get_image_path(self, recipe_path):
        return os.path.dirname(recipe_path) + "/thumb.jpg"


    def open_recipe(self, recipe):
        self.rv_controller.load_recipe(recipe)


    def open_recipe_list(self):
        self.window.stackedWidget.setCurrentIndex(0)
