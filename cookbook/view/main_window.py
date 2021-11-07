from cookbook.model import helper
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QMainWindow
import os, sys


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)



class MainWindow(QMainWindow):
    recipe_buttons = []


    def __init__(self):
        super(MainWindow, self).__init__()
        ui_file = resource_path("main_window.ui")
        uic.loadUi(ui_file, self)


    def add_recipe(self, recipe_button):
        self.recipe_buttons.append(recipe_button)
        layout = self.recipeList.layout()
        layout.insertWidget(layout.count()-1,recipe_button)


    def get_recipe_buttons(self):
        return self.recipe_buttons


    def delete_recipe_buttons(self):
        layout = self.recipeList.layout()
        helper.clear_layout(layout)
        self.recipe_buttons.clear()


    def set_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.imageLabel.setPixmap(pixmap)

        self.imageLabel.resize(pixmap.width(),pixmap.height())
