# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MaGrav.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self):
        #MainWindow = QtWidgets.QMainWindow()
        self.setObjectName("MainWindow")
        self.resize(702, 495)
        """
        Set main window qrids
        """
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setWindowTitle('MaGrav')
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_2.addWidget(self.graphicsView_2)
        self.setCentralWidget(self.centralwidget)

        """
        Set menu bar options
        """

        self.ReadPolygonAction = QtWidgets.QAction('&Read Polygon', self)
        self.ReadPolygonAction.setShortcut('Ctrl+Q')
        self.ReadPolygonAction.setStatusTip('Read Polygon from .txt')
        #ReadPolygonAction.triggered.connect(self.Read_File)
        ""
        self.menubar = self.menuBar()
        fileMenu = self.menubar.addMenu('&File')
        fileMenu.addAction(self.ReadPolygonAction)
        ""

        self.OpenPolygonTableAction = QtWidgets.QAction('&Open Polygon Table', self)
        self.OpenPolygonTableAction.setStatusTip('Open Polygon Table')

        ""

        tableMenu =  QtWidgets.QMenu('Polygon Table', self)
        tableMenu.addAction(self.OpenPolygonTableAction)
        self.menubar.addMenu(tableMenu)
        ""

        self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 26))
        self.menubar.setObjectName("menubar")
        self.setMenuBar(self.menubar)

        """
        Set status bar options
        """

        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        """
        ?
        """

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        """
        functions
        """

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))

    #def Open_Polygon_Table(self):
    #    #form = QtWidgets.QWidget()
    #    pt = PolygonTable()
    #    pt.show()


        """
        opens polygon table
        :return:
        """





