#!/bin/env python3
from cbook.controller.controller import Controller
from cbook.view.main_window import MainWindow
from cbook.model import cb_model

# Qt
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

def main():
    app = QApplication(sys.argv)

    m_model = cb_model.CbModel()
    window = MainWindow()

    m_controller = Controller(m_model, window)

    window.show()
    app.exec()


if __name__ == '__main__':
    sys.exit(main())
