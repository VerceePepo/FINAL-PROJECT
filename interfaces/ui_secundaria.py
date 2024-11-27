# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../disenios/secundaria.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_SecondaryWindow(object):
    def setupUi(self, SecondaryWindow):
        SecondaryWindow.setObjectName("SecondaryWindow")
        SecondaryWindow.resize(400, 250)
        SecondaryWindow.setMinimumSize(QtCore.QSize(400, 250))
        SecondaryWindow.setMaximumSize(QtCore.QSize(400, 250))
        self.centralwidget = QtWidgets.QWidget(SecondaryWindow)
        self.centralwidget.setGeometry(QtCore.QRect(0, 10, 400, 250))
        self.centralwidget.setMinimumSize(QtCore.QSize(400, 250))
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 250))
        self.centralwidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralwidget.setMouseTracking(False)
        self.centralwidget.setStyleSheet("QWidget#centralwidget {\n"
"    background-image: url(/home/pepo/PROYECTO FINAL/imagenes/secundaria.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-size: cover;\n"
"}\n"
"QLabel {\n"
"    background: none;  /* Asegúrate de que los QLabel no tengan fondo */\n"
"}\n"
"QPushButton {\n"
"    background: none;  /* Asegúrate de que los QPushButton no tengan fondo */\n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.botonVolver = QtWidgets.QPushButton(self.centralwidget)
        self.botonVolver.setGeometry(QtCore.QRect(10, 10, 80, 23))
        self.botonVolver.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.botonVolver.setText("")
        self.botonVolver.setObjectName("botonVolver")
        self.botonContra = QtWidgets.QPushButton(self.centralwidget)
        self.botonContra.setGeometry(QtCore.QRect(110, 30, 161, 51))
        self.botonContra.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.botonContra.setText("")
        self.botonContra.setObjectName("botonContra")
        self.botonArchivo = QtWidgets.QPushButton(self.centralwidget)
        self.botonArchivo.setGeometry(QtCore.QRect(110, 90, 161, 51))
        self.botonArchivo.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.botonArchivo.setText("")
        self.botonArchivo.setObjectName("botonArchivo")
        self.botonDatos = QtWidgets.QPushButton(self.centralwidget)
        self.botonDatos.setGeometry(QtCore.QRect(110, 140, 161, 51))
        self.botonDatos.setMinimumSize(QtCore.QSize(80, 20))
        self.botonDatos.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.botonDatos.setText("")
        self.botonDatos.setObjectName("botonDatos")
        self.boto_cambiar_contra = QtWidgets.QPushButton(self.centralwidget)
        self.boto_cambiar_contra.setGeometry(QtCore.QRect(110, 200, 161, 51))
        self.boto_cambiar_contra.setStyleSheet("QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"}")
        self.boto_cambiar_contra.setText("")
        self.boto_cambiar_contra.setObjectName("boto_cambiar_contra")
        self.menubar = QtWidgets.QMenuBar(SecondaryWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 20))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(SecondaryWindow)
        self.statusbar.setGeometry(QtCore.QRect(0, 0, 3, 22))
        self.statusbar.setObjectName("statusbar")
        self.toolBar = QtWidgets.QToolBar(SecondaryWindow)
        self.toolBar.setGeometry(QtCore.QRect(0, 0, 8, 17))
        self.toolBar.setObjectName("toolBar")

        self.retranslateUi(SecondaryWindow)
        self.botonContra.clicked.connect(SecondaryWindow.boton_contrasena) # type: ignore
        self.botonArchivo.clicked.connect(SecondaryWindow.boton_archivos) # type: ignore
        self.botonDatos.clicked.connect(SecondaryWindow.boton_datos) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(SecondaryWindow)

    def retranslateUi(self, SecondaryWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondaryWindow.setWindowTitle(_translate("SecondaryWindow", "Opciones"))
        self.toolBar.setWindowTitle(_translate("SecondaryWindow", "toolBar"))