import json
import os
import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QDialog, QMessageBox
from interfaces.ui_cambiar_contraseña import Ui_Form

class VentanaCambioClave(QDialog):  # Asegúrate de heredar de QDialog
    def __init__(self, parent=None):
        super().__init__(parent)  # Llama al constructor de QDialog
        self.setupUi()  # Llama a tu método de configuración de la interfaz

    def setupUi(self):
        # Aquí va tu código para configurar la interfaz
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Conectar señales y slots, etc.
        self.ui.boton_cambiar_contra.clicked.connect(self.cambiar_contrasena)

    def cambiar_contrasena(self):
        # Obtener la contraseña actual y la nueva contraseña del campo de texto
        contrasena_actual = self.ui.line_contra.text()
        nueva_contrasena = self.ui.line_contranueva.text()

        if not nueva_contrasena:
            QMessageBox.warning(self, "Advertencia", "El campo de nueva contraseña debe ser completado.")
            return

        # Ruta del archivo donde se guardará la contraseña
        ruta_archivo = os.path.join("datos", "clave.json")

        # Cargar datos existentes del archivo JSON
        try:
            if os.path.exists(ruta_archivo):
                with open(ruta_archivo, 'r') as f:
                    datos = json.load(f)
            else:
                datos = {}

            # Si hay una contraseña guardada, validar la contraseña actual
            if 'contraseña' in datos:
                if datos['contraseña'] != contrasena_actual:
                    QMessageBox.warning(self, "Error", "La contraseña actual es incorrecta.")
                    return

            # Guardar la nueva contraseña en el archivo JSON
            datos['contraseña'] = nueva_contrasena

            with open(ruta_archivo, 'w') as f:
                json.dump(datos, f, indent=4)

            QMessageBox.information(self, "Éxito", "Contraseña cambiada y guardada correctamente.")
            self.accept()  # Cierra el diálogo

        except Exception as e:
            QMessageBox.critical(self, "Error", f"No se pudo guardar la contraseña: {e}")

