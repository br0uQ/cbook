from model import helper
from model.recipe_parser import get_ingredients
from os.path import split
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap


class ReController:
    default_image = "view/knife_and_fork.svg"
    image = ""


    def __init__(self, model, window):
        self.model = model
        self.window = window

        self.window.buttonAddIngredient.clicked.connect(self.add_ingredient_row)
        self.window.buttonDeleteIngredient.clicked.connect(self.delete_ingredient_row)
        self.window.loadImageButton.clicked.connect(self.open_select_image)
        self.window.deleteImageButton.clicked.connect(self.delete_image)
        self.window.comboBoxKategorien.activated.connect(self.activated_kategorien)
        self.window.comboBoxNahrung.activated.connect(self.activated_nahrung)
        self.window.comboBoxKohlenhydrate.activated.connect(self.activated_kohlenhydrate)
        self.window.buttonClearKategorien.clicked.connect(self.clear_categories)
        self.window.buttonClearNahrung.clicked.connect(self.clear_nahrung)
        self.window.buttonClearKohlenhydrate.clicked.connect(self.clear_kohlenhydrate)
        self.window.buttonSave.clicked.connect(self.save_recipe)


    def set_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.window.imageLabelEdit.setPixmap(pixmap)


    def remove_prefix(self, labels):
        ret = []
        for l in labels:
            ret.append(l.split('_')[1])
        return ret


    def prepare_new(self, categories, nahrungs, kohlehydrate):
        categories = self.remove_prefix(categories)
        nahrungs = self.remove_prefix(nahrungs)
        kohlehydrate = self.remove_prefix(kohlehydrate)
        self.window.nameLineEdit.setText("")
        self.window.zutatenTableWidget.setRowCount(1)
        self.window.zutatenTableWidget.clearContents()
        self.set_image(self.default_image)
        self.window.spinBoxPortionenEdit.setValue(4)
        self.window.comboBoxKategorien.clear()
        self.window.comboBoxKategorien.addItems(categories)
        self.window.comboBoxNahrung.clear()
        self.window.comboBoxNahrung.addItems(nahrungs)
        self.window.comboBoxKohlenhydrate.clear()
        self.window.comboBoxKohlenhydrate.addItems(kohlehydrate)
        self.clear_categories()
        self.clear_kohlenhydrate()
        self.clear_nahrung()
        self.window.buttonReload.setHidden(True)
        self.window.buttonDeleteRecipe.setHidden(True)


    def add_ingredient_row(self):
        tableWidget = self.window.zutatenTableWidget
        tableWidget.insertRow(tableWidget.rowCount())


    def delete_ingredient_row(self):
        tableWidget = self.window.zutatenTableWidget
        tableWidget.removeRow(tableWidget.rowCount()-1)


    def open_select_image(self):
        fname, _ = QtWidgets.QFileDialog.getOpenFileName(self.window, 
                'Öffne Bild', 
                '',
                "Image files (*.jpg *.gif *.png *.jpeg *.svg)")
        if fname:
            self.image = fname
            self.set_image(fname)


    def delete_image(self):
        self.image = ""
        self.set_image(self.default_image)


    def activated_kategorien(self):
        selected = self.window.comboBoxKategorien.currentText()
        # add to list
        text = self.window.labelKategorienEdit.text()
        if selected not in text.split(', '):
            if text != "":
                text = text + ", "
            self.window.labelKategorienEdit.setText(text + selected)
            # clear comboBox
            self.window.comboBoxKategorien.clearEditText()
        print(selected)


    def activated_nahrung(self):
        selected = self.window.comboBoxNahrung.currentText()
        # add to list
        text = self.window.labelNahrungEdit.text()
        if selected not in text.split(', '):
            if text != "":
                text = text + ", "
            self.window.labelNahrungEdit.setText(text + selected)
            # clear comboBox
            self.window.comboBoxNahrung.clearEditText()
        print(selected)


    def activated_kohlenhydrate(self):
        selected = self.window.comboBoxKohlenhydrate.currentText()
        # add to list
        text = self.window.labelKohlenhydrateEdit.text()
        if selected not in text.split(', '):
            if text != "":
                text = text + ", "
            self.window.labelKohlenhydrateEdit.setText(text + selected)
            # clear comboBox
            self.window.comboBoxKohlenhydrate.clearEditText()
        print(selected)


    def clear_categories(self):
        self.window.labelKategorienEdit.setText("")


    def clear_nahrung(self):
        self.window.labelNahrungEdit.setText("")


    def clear_kohlenhydrate(self):
        self.window.labelKohlenhydrateEdit.setText("")


    def get_ingredients(self):
        ingredients = []
        model = self.window.zutatenTableWidget.model()
        for r in range(0,self.window.zutatenTableWidget.rowCount()):
            ingredient = []
            menge = model.data(model.index(r, 0))
            einheit = model.data(model.index(r, 1))
            zutat = model.data(model.index(r, 2))
            if menge or einheit or zutat:
                if menge:
                    try:
                        menge = helper.string_to_float(menge)
                    except:
                        QtWidgets.QMessageBox.critical(self.window, "Ungültige Mengenangabe",
                                "Ungültige Mengeneingabe '" + menge + "'.\n" +
                                "Entweder als Dezimalzahl (z.B. '1.5')\n" +
                                "oder als Bruch (z.B. '1 1/2' oder '3/5') eingeben!")
                        return None
                else:
                    menge = ""
                if not einheit:
                    einheit = ""
                if not zutat:
                    QtWidgets.QMessageBox.critical(self.window, "Ungültige Zutatenangabe",
                            "Leeres Zutatenfeld!")
                    return None

                ingredients.append(str(menge) + " " + str(einheit) + " " + str(zutat))
            else:
                print("Skipped empty ingredient row")
        if not ingredients:
            QtWidgets.QMessageBox.critical(self.window, "Ungültige Zutaten",
                    "Keine Zutaten angegeben!")
        return ingredients


    def save_recipe(self):
        name = self.window.nameLineEdit.text()
        if self.model.check_name(name):
            ingredients = self.get_ingredients()
            if ingredients:
                # read recipe data and save recipe
                portionen = self.window.spinBoxPortionenEdit.value()
                anleitung = self.window.textEditAnleitung.toPlainText()
                beschreibung = self.window.textEditBeschreibung.toPlainText()
                kategorien = self.window.labelKategorienEdit.text().split(', ')
                nahrung = self.window.labelNahrungEdit.text().split(', ')
                kohlenhydrate = self.window.labelKohlenhydrateEdit.text().split(', ')
                
                print("====== Recipe Data ======")
                print(name)
                print(self.image)
                print(ingredients)
                print(portionen)
                print(beschreibung)
                print(anleitung)
                print(kategorien)
                print(nahrung)
                print(kohlenhydrate)
                print("====== Recipe Data end ======")

                self.model.save_recipe(name, self.image, ingredients, portionen,
                        beschreibung, anleitung, kategorien, nahrung, kohlenhydrate)

        else:
            QtWidgets.QMessageBox.critical(self.window, "Ungültiger Rezeptname",
                    "Ein Rezept mit diesem Namen ist bereits vorhanden.\n" +
                    "Bitte wähle einen anderen Namen!")
