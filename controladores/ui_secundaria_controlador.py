from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow
from interfaces.ui_secundaria import Ui_SecondaryWindow
from .iu_contraseña_controlador import DialogContraseña
from .iu_archivos_controlador import VentanaArchivos
from .iu_datos_controlador import VentanaDatos
from .ui_cambiar_contraseña_controlador import VentanaCambioClave

class SecondaryWindow(QMainWindow, Ui_SecondaryWindow):
    def __init__(self, main_window):
        super().__init__()
        self.setupUi(self)
        self.main_window = main_window

        # Conecta los botones
        self.botonVolver.clicked.connect(self.volver_ventana_principal)
        self.botonContra.clicked.connect(self.boton_contrasena)
        self.botonDatos.clicked.connect(self.boton_datos)
        self.boto_cambiar_contra.clicked.connect(self.boton_cambiar_contrasena)


    def boton_contrasena(self):
        dialog = DialogContraseña(self)  # Crea una instancia del diálogo
        dialog.exec_()  # Llama a exec_() en la instancia

    def boton_cambiar_contrasena(self):
        dialog = VentanaCambioClave(self)  # Crea una instancia del diálogo
        dialog.exec_()  # Llama a exec_() en la instancia

    def volver_ventana_principal(self):
        self.hide()
        self.main_window.show()

    def boton_archivos(self):
        dialog = VentanaArchivos(self)  # Crea una instancia del diálogo
        dialog.exec_()  # Llama a exec_() en la instancia

    def boton_datos(self):
        dialog = VentanaDatos(self)  # Crea una instancia del diálogo
        dialog.exec_()  # Llama a exec_() en la instancia