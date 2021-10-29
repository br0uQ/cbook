#!/bin/env python3
import model.cb_model as model
from model import cb_model
from controller import mw_controller as mwc

# Qt
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic


app = QApplication(sys.argv)

m_model = cb_model.CbModel()
window = uic.loadUi("view/main_window.ui")

m_mwc = mwc.MwController(m_model, window)

window.show()
app.exec()
