import sys
import json
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget, QWidget
from PySide2.QtCore import Slot

from PySide2.QtGui import QPixmap, QIcon
import subprocess

from controladores.ui_ventana_principal_controlador import MainWindow



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())