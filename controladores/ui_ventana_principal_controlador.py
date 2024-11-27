import sys
import subprocess  # Asegúrate de importar subprocess
from PySide2 import QtWidgets, QtCore
from PySide2.QtWidgets import QMainWindow, QMessageBox
from interfaces.ui_ventana_principal import Ui_MainWindow
from controladores.ui_secundaria_controlador import SecondaryWindow
from clases.RFIDReader import RFIDReader  # Importar la clase RFIDReader

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.ventana2 = SecondaryWindow(self)
        self.boton.clicked.connect(self.apretar)  # Conexión de botón
        self.show()

        # Inicializa el lector RFID
        self.rfid_reader = RFIDReader()
        self.rfid_reader.uid_detected_signal.connect(self.check_uid)

    def check_uid(self, uid):
        correct_uid = "2A 29 F2 81"  # UID correcto
        if uid == correct_uid:
            QMessageBox.information(self, "Éxito", "UID reconocida. Acceso concedido.")
            self.ventana2.show()  # Muestra la ventana secundaria
            self.hide()  # Oculta la ventana principal
        else:
            QMessageBox.warning(self, "Error", "UID no reconocida. Acceso denegado.")

    def apretar(self):
        # Lógica para abrir el enlace
        url = "https://www.canva.com/design/DAGVudm26yo/vr3W3yDhAdWYvBu5ogO68Q/edit?utm_content=DAGVudm26yo&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton"
        try:
            subprocess.run(['powershell.exe', '-Command', f'Start-Process "{url}"'], check=True)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo abrir el enlace: {e}")

    def closeEvent(self, event):
        self.rfid_reader.close()  # Cierra el puerto serial al cerrar la ventana
        event.accept()