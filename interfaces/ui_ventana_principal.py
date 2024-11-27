# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../disenios/ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PySide2 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setMinimumSize(QtCore.QSize(1920, 1080))
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QWidget#centralwidget {\n"
"    background-image: url(/home/pepo/PROYECTO FINAL/imagenes/fondo_finalHD.jpg);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"    background-size: cover;\n"
"}\n"
"QLabel {\n"
"    background: none;  /* Asegúrate de que los QLabel no tengan fondo */\n"
"}\n"
"QPushButton {\n"
"    background: none;  /* Asegúrate de que los QPushButton no tengan fondo */\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.boton = QtWidgets.QPushButton(self.centralwidget)
        self.boton.setGeometry(QtCore.QRect(1860, 10, 51, 51))
        self.boton.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.boton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imagenes\oton_pregunta.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.boton.setIcon(icon)
        self.boton.setIconSize(QtCore.QSize(50, 50))
        self.boton.setAutoRepeatInterval(98)
        self.boton.setAutoDefault(False)
        self.boton.setObjectName("boton")
        self.aviso = QtWidgets.QLabel(self.centralwidget)
        self.aviso.setGeometry(QtCore.QRect(540, 750, 881, 41))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.aviso.setFont(font)
        self.aviso.setObjectName("aviso")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(770, -110, 591, 491))
        self.titulo.setMinimumSize(QtCore.QSize(400, 200))
        self.titulo.setMaximumSize(QtCore.QSize(600, 600))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Sans Mono")
        font.setPointSize(48)
        font.setBold(True)
        font.setWeight(75)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.toolBar_3 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_3.setObjectName("toolBar_3")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_3)
        self.toolBar_4 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_4.setObjectName("toolBar_4")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_4)
        self.toolBar_5 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_5.setObjectName("toolBar_5")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_5)

        self.retranslateUi(MainWindow)
        self.boton.pressed.connect(MainWindow.apretar) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.aviso.setText(_translate("MainWindow", "Acerque el llavero al lector para ingresar a su cuenta"))
        self.titulo.setText(_translate("MainWindow", "GEST-ORIAN"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))
        self.toolBar_3.setWindowTitle(_translate("MainWindow", "toolBar_3"))
        self.toolBar_4.setWindowTitle(_translate("MainWindow", "toolBar_4"))
        self.toolBar_5.setWindowTitle(_translate("MainWindow", "toolBar_5"))
