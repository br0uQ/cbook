from PyQt5 import uic
from PyQt5.QtWidgets import QLabel, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("view/main_window.ui", self)


    def add_recipe(self, recipe_button):
        self.recipeList.layout().addWidget(recipe_button)
