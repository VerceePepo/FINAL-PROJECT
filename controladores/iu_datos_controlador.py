# -*- coding: utf-8 -*-
import json
import os
from PySide2 import QtCore, QtWidgets
from PySide2.QtGui import QStandardItem, QStandardItemModel
from PySide2.QtWidgets import QHeaderView
from interfaces.ui_datos import Ui_Form  # Asegúrate de que esto funcione

class VentanaDatos(QtWidgets.QDialog, Ui_Form):
    def __init__(self, parent=None):
        super(VentanaDatos, self).__init__(parent)
        self.setupUi(self)
        self.boton_eliminar.clicked.connect(self.eliminar_datos)

        self.model = QStandardItemModel(self)
        self.model.setHorizontalHeaderLabels(["Referencia", "URL", "Contraseña"])

        # Configurar el QTableView
        self.tabla.setModel(self.model)

        # Configurar el tamaño de las columnas
        self.tabla.horizontalHeader().setStretchLastSection(True)
        self.tabla.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)

        # Establecer un tamaño fijo para las columnas
        self.tabla.setColumnWidth(0, 150)
        self.tabla.setColumnWidth(1, 150)
        self.tabla.setColumnWidth(2, 200)

        # Ocultar la tabla al inicio
        self.tabla.setVisible(False)

        # Intentar desconectar cualquier conexión previa
       

        # Conectar el botón OK a la función que agrega datos
        self.boton_ok.clicked.connect(self.agregar_datos)

        # Cargar datos existentes desde el archivo JSON al iniciar
        self.cargar_datos()

        # Conectar el botón de ver contraseña
        self.boton_ok_2.clicked.connect(self.ver_contrasena)

    def agregar_datos(self):
        # Obtener datos de los campos de entrada
        referencia = self.line_referencia.text().strip()
        url = self.line_url.text().strip()
        contrasena = self.line_contrasena.text().strip()

        # Validar que todos los campos tengan datos
        if not referencia or not url or not contrasena:
            QtWidgets.QMessageBox.warning(self, "Error", "Todos los campos deben ser llenados.")
            return

        # Agregar datos al modelo
        row = [
            self.create_centered_item(referencia),
            self.create_centered_item(url),
            self.create_centered_item(contrasena)  # Mostrar la contraseña en texto claro
        ]
        self.model.appendRow(row)

        # Guardar datos en el archivo JSON
        self.guardar_datos()

        # Limpiar los campos de entrada
        self.line_referencia.clear()
        self.line_url.clear()
        self.line_contrasena.clear()
        
    def eliminar_datos(self):
        referencia = self.line_referencia.text()
        url = self.line_url.text()
        contrasena = self.line_contrasena.text()

        # Buscar y eliminar la fila correspondiente en la tabla
        for row in range(self.model.rowCount()):
            item_referencia = self.model.item(row, 0)
            item_url = self.model.item(row, 1)
            item_contrasena = self.model.item(row, 2)

            if (item_referencia and item_referencia.text() == referencia and
                item_url and item_url.text() == url and
                item_contrasena and item_contrasena.text() == contrasena):
                self.model.removeRow(row)
                QMessageBox.information(self, "Éxito", "Datos eliminados correctamente.")
                return

        QMessageBox.warning(self, "Error", "No se encontraron datos para eliminar.")

    def create_centered_item(self, text):
        item = QStandardItem(text)
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)  # Hacer que el item no sea editable
        return item

    def guardar_datos(self):
        datos = []
        for row in range(self.model.rowCount()):
            referencia = self.model.item(row, 0).text()
            url = self.model.item(row, 1).text()
            contrasena = self.model.item(row, 2).text()  # Guardar la contraseña real
            datos.append({"Referencia": referencia, "URL": url, "Contraseña": contrasena})

        # Guardar los datos en datos.json
        ruta_archivo = os.path.join("datos", "datos.json")
        with open(ruta_archivo, 'w') as f:
            json.dump(datos, f, indent=4)

    def cargar_datos(self):
        ruta_archivo = os.path.join("datos", "datos.json")
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r') as f:
                datos = json.load(f)
                for entrada in datos:
                    row = [
                        self.create_centered_item(entrada["Referencia"]),
                        self.create_centered_item(entrada["URL"]),
                        self.create_centered_item(entrada["Contraseña"])  # Mostrar la contraseña en texto claro
                    ]
                    self.model.appendRow(row)

    def ver_contrasena(self):
        clave_ingresada = self.line_clave.text().strip()
        clave_correcta = self.cargar_clave()  # Método para cargar la clave guardada

        if clave_ingresada == clave_correcta:
            self.tabla.setVisible(True)  # Hacer visible la tabla
            for row in range(self.model.rowCount()):
                contrasena = self.model.item(row, 2).text()  # Obtener la contraseña real
                self.model.setItem(row, 2, self.create_centered_item(contrasena))  # Mostrar la contraseña en texto claro
            QtWidgets.QMessageBox.information(self, "Éxito", "Las contraseñas se han mostrado.")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "La clave ingresada es incorrecta.")

    def cargar_clave(self):
        ruta_archivo = os.path.join("datos", "clave.json")
        if os.path.exists(ruta_archivo):
            with open(ruta_archivo, 'r') as f:
                return json.load(f).get("contraseña", "")
        return ""

    def guardar_clave(self, clave):
        ruta_archivo = os.path.join("datos", "clave.json")
        with open(ruta_archivo, 'w') as f:
            json.dump({"clave": clave}, f)

    def establecer_clave(self):
        clave = self.line_clave.text().strip()
        if clave:
            self.guardar_clave(clave)
            QtWidgets.QMessageBox.information(self, "Éxito", "Clave guardada correctamente.")
        else:
            QtWidgets.QMessageBox.warning(self, "Error", "La clave no puede estar vacía.")