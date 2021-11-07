#!/bin/env python3
from cookbook.view.main_window import MainWindow
from cookbook.model import cb_model
from cookbook.controller import mw_controller as mwc

# Qt
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

def main():
    app = QApplication(sys.argv)

    m_model = cb_model.CbModel()
    window = MainWindow()

    m_mwc = mwc.MwController(m_model, window)

    window.show()
    app.exec()


if __name__ == '__main__':
    sys.exit(main())
