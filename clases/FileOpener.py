import subprocess
import os
from PySide2.QtWidgets import QMessageBox

class FileOpener:
    def __init__(self, parent=None):
        self.parent = parent  # Guarda una referencia al widget padre

    def open_file(self, file_path):
        if not file_path:
            QMessageBox.warning(self.parent, "Error", "Por favor selecciona un archivo.")
            return

        # Verificar si el archivo existe
        if not os.path.isfile(file_path):
            QMessageBox.warning(self.parent, "Error", "La ruta no es un archivo válido.")
            return

        # Abrir el archivo con la aplicación predeterminada
        try:
            print(f"Abriendo archivo: {file_path}")  # Mensaje de depuración
            subprocess.run(['start', '', file_path], shell=True)
        except Exception as e:
            self.show_error_application()

    def show_error_application(self):
        QMessageBox.critical(self.parent, "Error", "Ocurrió un error al intentar abrir el archivo.")