import json
import os
import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import QDialog, QMessageBox, QFileDialog
from interfaces.ui_archivos import Ui_Form  # Asegúrate de que la ruta sea correcta
from clases.FileOpener import FileOpener  # Asegúrate de importar la clase FileOpener

class VentanaArchivos(QDialog, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)  # Llama al constructor de QDialog
        self.setupUi(self)  # Configura la interfaz usando el método generado por Qt Designer

        # Instanciar FileOpener
        self.file_opener = FileOpener(self)

        # Conectar los botones a sus funciones
        self.boton_agregar.clicked.connect(self.agregar_archivo)
        self.boton_ir_archivo.clicked.connect(self.ir_archivo)  # Este botón ahora usará FileOpener
        self.boton_seleccionar_archivo.clicked.connect(self.seleccionar_archivo)  # Nuevo botón
        self.boton_eliminar.clicked.connect(self.eliminar_archivo)  # Conectar el botón eliminar

        # Cargar rutas desde el archivo JSON al iniciar
        self.cargar_rutas()

    def agregar_archivo(self):
        ruta = self.line_ruta.text().strip()
        if not ruta:
            QMessageBox.warning(self, "Error", "La ruta no puede estar vacía.")
            return

        # Verifica si la ruta es válida
        if not os.path.isfile(ruta):
            QMessageBox.warning(self, "Error", "La ruta no es un archivo válido.")
            return
        
        # Agregar la ruta al combo box
        self.lista_archivos.addItem(ruta)

        # Guardar la ruta en el archivo JSON
        self.guardar_rutas()

        # Limpiar el QLineEdit
        self.line_ruta.clear()

    def seleccionar_archivo(self):
        # Abre un cuadro de diálogo para seleccionar un archivo
        opciones = QFileDialog.Options()
        archivo, _ = QFileDialog.getOpenFileName(self, "Seleccionar Archivo", "", "Todos los Archivos (*)", options=opciones)
        if archivo:
            # Agregar la ruta seleccionada al combo box
            self.line_ruta.setText(archivo)  # Muestra la ruta en el QLineEdit
            self.agregar_archivo()  # Llama a agregar_archivo para validar y guardar

    def ir_archivo(self):
        ruta = self.lista_archivos.currentText()
        self.file_opener.open_file(ruta)  # Usar el método de FileOpener para abrir el archivo

    def eliminar_archivo(self):
        # Obtener el índice del elemento seleccionado
        indice_seleccionado = self.lista_archivos.currentIndex()
        if indice_seleccionado == -1:
            QMessageBox.warning(self, "Error", "Por favor selecciona un archivo para eliminar.")
            return

        # Eliminar el archivo de la lista usando el índice directamente
        self.lista_archivos.removeItem(indice_seleccionado)
        self.guardar_rutas()  # Guardar los cambios en el archivo JSON

    def cargar_rutas(self):
        # Cargar rutas desde un archivo JSON
        if os.path.exists("rutas.json"):
            with open("rutas.json", "r") as archivo:
                rutas = json.load(archivo)
                for ruta in rutas:
                    self.lista_archivos.addItem(ruta)

    def guardar_rutas(self):
        # Guardar rutas en un archivo JSON
        rutas = [self.lista_archivos.itemText(i) for i in range(self.lista_archivos.count())]
        with open("rutas.json", "w") as archivo:
            json.dump(rutas, archivo)

    def mostrar_error_aplicacion(self):
        QMessageBox.critical(self, "Error", "Ocurrió un error al intentar abrir el archivo.")