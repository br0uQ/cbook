from model import helper
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QMainWindow


class MainWindow(QMainWindow):
    recipe_buttons = []


    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("view/main_window.ui", self)


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
