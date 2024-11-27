import json
import os
from PySide2.QtWidgets import QDialog, QTableView, QVBoxLayout, QPushButton, QHeaderView, QMessageBox
from PySide2.QtGui import QStandardItemModel, QStandardItem
from interfaces.ui_contraseña import Ui_ventana3

class DialogContraseña(QDialog, Ui_ventana3):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # Crear el modelo para la tabla
        self.model = QStandardItemModel(self)
        self.model.setHorizontalHeaderLabels(["Usuario", "Contraseña", "Referencia"])

        # Configurar el QTableView
        self.tabla.setModel(self.model)

        # Configurar el tamaño de las columnas
        self.tabla.horizontalHeader().setStretchLastSection(True)  # Hace que la última columna ocupe el espacio restante
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)  # Evita que el usuario cambie el tamaño de las columnas

        # Establecer un tamaño fijo para las columnas
        self.tabla.setColumnWidth(0, 150)  # Ancho de la columna "Usuario"
        self.tabla.setColumnWidth(1, 150)  # Ancho de la columna "Contraseña"
        self.tabla.setColumnWidth(2, 200)  # Ancho de la columna "Referencia"

        # Intentar desconectar cualquier conexión previa
        try:
            self.botonok.clicked.disconnect()
        except RuntimeError:
            print("Signal already disconnected or was never connected.")

        # Conectar el botón a la función add_data
        self.botonok.clicked.connect(self.add_data)

        # Conectar el botón de eliminar a la función remove_data
        self.boton_eliminar.clicked.connect(self.remove_data)

        # Cargar datos en la tabla al iniciar el diálogo
        self.cargar_datos_en_tabla()

    def cargar_datos_en_tabla(self):
        # Limpiar el modelo antes de cargar nuevos datos
        self.model.removeRows(0, self.model.rowCount())

        # Ruta al archivo JSON
        json_file_path = os.path.join("datos", "contrasena.json")

        # Leer el contenido existente del archivo JSON
        if os.path.exists(json_file_path):
            with open(json_file_path, "r", encoding="utf-8") as file:
                try:
                    datos_existentes = json.load(file)
                except json.JSONDecodeError:
                    datos_existentes = []  # Si el archivo está vacío o tiene un error
        else:
            datos_existentes = []

        # Agregar los datos al modelo
        for registro in datos_existentes:
            row = [
                QStandardItem(registro["usuario"]),
                QStandardItem(registro["contraseña"]),
                QStandardItem(registro["referencia"])
            ]
            self.model.appendRow(row)  # Agregar la fila al modelo

    def add_data(self):
        # Obtener los datos del formulario
        usuario = self.usuario_line.text()
        contrasena = self.contrasena_line.text()
        referencia = self.referencia_line.text()

        # Crear un nuevo registro
        nuevo_registro = {
            "usuario": usuario,
            "contraseña": contrasena,
            "referencia": referencia
        }

        # Ruta al archivo JSON
        json_file_path = os.path.join("datos", "contrasena.json")

        # Leer el contenido existente del archivo JSON
        if os.path.exists(json_file_path):
            with open(json_file_path, "r", encoding="utf-8") as file:
                try:
                    datos_existentes = json.load(file)
                except json.JSONDecodeError:
                    datos_existentes = []  # Si el archivo está vacío o tiene un error
        else:
            datos_existentes = []

        # Agregar el nuevo registro a los datos existentes
        datos_existentes.append(nuevo_registro)

        # Escribir de nuevo en el archivo JSON
        with open(json_file_path , "w", encoding="utf-8") as file:
            json.dump(datos_existentes, file, ensure_ascii=False, indent=4)

        # Actualizar la tabla
        self.cargar_datos_en_tabla()

    def remove_data(self):
        # Obtener los datos del formulario
        usuario = self.usuario_line.text()
        contrasena = self.contrasena_line.text()
        referencia = self.referencia_line.text()

        # Ruta al archivo JSON
        json_file_path = os.path.join("datos", "contrasena.json")

        # Leer el contenido existente del archivo JSON
        if os.path.exists(json_file_path):
            with open(json_file_path, "r", encoding="utf-8") as file:
                try:
                    datos_existentes = json.load(file)
                except json.JSONDecodeError:
                    datos_existentes = []  # Si el archivo está vacío o tiene un error
        else:
            datos_existentes = []

        # Buscar el registro a eliminar
        for registro in datos_existentes:
            if (registro["usuario"] == usuario and
                registro["contraseña"] == contrasena and
                registro["referencia"] == referencia):
                datos_existentes.remove(registro)  # Eliminar el registro
                break
        else:
            QMessageBox.warning(self, "Error", "No se encontró el registro para eliminar.")

        # Escribir de nuevo en el archivo JSON
        with open(json_file_path, "w", encoding="utf-8") as file:
            json.dump(datos_existentes, file, ensure_ascii=False, indent=4)

        # Actualizar la tabla
        self.cargar_datos_en_tabla()