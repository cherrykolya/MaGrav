import sys
import json
from Polygon import Polygon
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from mydesign import Ui_MainWindow
from PolygonTable import Ui_Form

plgs = []

class TableWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi()
        self.setWindowTitle("Polygon Table")
        self.setWindowIcon(QtGui.QIcon('tableicon.png'))
        for i in range(len(plgs)):
            self.listWidget.addItem(plgs[i].Name)
        self.listWidget.itemClicked.connect(self.List_Item_Clicked)
        self.tableWidget.setRowCount(1)
        #self.plgn_table.
        print(plgs[0].Points[0][1])
        #self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str(plgs[0].Points[0][1])))
       # self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(plgs.Points[0][1]))

    def List_Item_Clicked(self, item):
        #sender = self.sender()
        poly = plgs[int(item.text()[-1])]
        self.Set_Table_Values(poly)
        #print(item.text())
        #print(self.text())

    def Set_Table_Values(self, poly):
        self.tableWidget.setRowCount(len(poly.Points))
        for i in range(len(poly.Points)):
            self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(str(poly.Points[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(poly.Points[i][1])))
            self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(poly.Density)))
            self.tableWidget.item(i, 0).setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.item(i, 1).setTextAlignment(QtCore.Qt.AlignCenter)






class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        #super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi()# = Ui_MainWindow()
        self.setWindowTitle("MaGrav")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.OpenPolygonTableAction.triggered.connect(self.Open_Polygon_Table)
        self.ReadPolygonAction.triggered.connect(self.Read_File)

    def Open_Polygon_Table(self):
        """
        Opens polygon table
        :return:
        """
        self.plgn_table = TableWindow()
        #for i in range(len(plgs)):
        #    self.plgn_table.listWidget.addItem(plgs[i].Name)
        self.plgn_table.show()

    def Read_File(self):
        """
        function to read polygon from .txt
        example file is POLYGON_EXAMPLE_FILE.txt(JSON format)
        :return:
        """
        dlg = QtWidgets.QFileDialog()
        #dlg.setFilter()
        dlg.show()
        #print('hui')
        if dlg.exec_():
            filename = dlg.selectedFiles()
        #print(filename[])
        with open (filename[0]) as file:
            data = json.load(file)
        for i in range(len(data)):
            print(data[i])
            poly = Polygon()
            poly.read_from_json(data[i], i)
            plgs.append(poly)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())

