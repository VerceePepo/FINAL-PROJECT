# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../disenios/contraseña.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_ventana3(object):
    def setupUi(self, ventana3):
        ventana3.setObjectName("ventana3")
        ventana3.resize(1000, 600)
        ventana3.setMinimumSize(QtCore.QSize(1000, 600))
        ventana3.setMaximumSize(QtCore.QSize(1000, 600))
        self.botonok = QtWidgets.QPushButton(ventana3)
        self.botonok.setGeometry(QtCore.QRect(880, 100, 91, 51))
        self.botonok.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")
        self.botonok.setText("")
        self.botonok.setObjectName("botonok")
        self.usuario_line = QtWidgets.QLineEdit(ventana3)
        self.usuario_line.setGeometry(QtCore.QRect(180, 60, 651, 41))
        self.usuario_line.setStyleSheet("\n"
"QLineEdit {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")
        self.usuario_line.setObjectName("usuario_line")
        self.contrasena_line = QtWidgets.QLineEdit(ventana3)
        self.contrasena_line.setGeometry(QtCore.QRect(180, 110, 651, 41))
        self.contrasena_line.setStyleSheet("\n"
"QLineEdit {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")
        self.contrasena_line.setObjectName("contrasena_line")
        self.referencia_line = QtWidgets.QLineEdit(ventana3)
        self.referencia_line.setGeometry(QtCore.QRect(180, 170, 651, 41))
        self.referencia_line.setStyleSheet("\n"
"QLineEdit {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")
        self.referencia_line.setObjectName("referencia_line")
        self.tabla = QtWidgets.QTableView(ventana3)
        self.tabla.setGeometry(QtCore.QRect(30, 250, 941, 341))
        self.tabla.setObjectName("tabla")
        self.boton_eliminar = QtWidgets.QPushButton(ventana3)
        self.boton_eliminar.setGeometry(QtCore.QRect(880, 170, 91, 51))
        self.boton_eliminar.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}\n"
"")
        self.boton_eliminar.setText("")
        self.boton_eliminar.setObjectName("boton_eliminar")
        self.label = QtWidgets.QLabel(ventana3)
        self.label.setGeometry(QtCore.QRect(0, 10, 1001, 591))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imagenes\contraseña.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.botonok.raise_()
        self.usuario_line.raise_()
        self.contrasena_line.raise_()
        self.referencia_line.raise_()
        self.tabla.raise_()
        self.boton_eliminar.raise_()

        self.retranslateUi(ventana3)
        QtCore.QMetaObject.connectSlotsByName(ventana3)

    def retranslateUi(self, ventana3):
        _translate = QtCore.QCoreApplication.translate
        ventana3.setWindowTitle(_translate("ventana3", "Form"))
