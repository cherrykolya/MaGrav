# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MaGrav.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(QtWidgets.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(702, 495)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.graphicsView_2 = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.verticalLayout_2.addWidget(self.graphicsView_2)
        MainWindow.setCentralWidget(self.centralwidget)

        exitAction = QtWidgets.QAction('&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(self.Read_File) #QtWidgets.qApp.quit)
        self.statusBar()
        self.menubar = self.menuBar()
        fileMenu = self.menubar.addMenu('&File')
        fileMenu.addAction(exitAction)

        """self.menubar = QtWidgets.QMenuBar(MainWindow)
        file = self.menubar.addMenu("File")
        file.addAction("R")

        self.Read_Polygon = QtWidgets.QAction("Read Polygon",MainWindow)#.triggered()#MainWindow)
        file.addAction(self.Read_Polygon)
        file.triggered.connect(self.Read_File())
        #self.Read_Polygon.triggered.    connect(QtWidgets.qApp.quit())"""

        #top_menu = self.menubar.addMenu("File")
        #Read_Polygon_Btn = QtWidgets.QAction("Read Polygon")
        #top_menu.addAction(Read_Polygon_Btn)
        #file.triggered[QtWidgets.QAction].connect(self.Read_File,)

        self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setEnabled(True)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    def Read_File(self):
        #print('hui')
        #if sender ==self.Read_Polygon:
        #    print('hui')
        dlg = QtWidgets.QFileDialog()
        #dlg.setFilter()
        dlg.show()
        #print('hui')
        if dlg.exec_():
            filenames = dlg.selectedFiles()




