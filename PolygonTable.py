# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PolygonTable.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(650, 465)
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.listWidget = QtWidgets.QListWidget(self)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout.addWidget(self.listWidget)
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(['X','Y','Density'])
        #self.tableWidget.horizontalHeaderItem(0).setTextAlignment(QtCore.Qt.AlignHCenter)
        #self.tableWidget.setRowCount()
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.horizontalLayout.addWidget(self.tableWidget)
        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 30)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
