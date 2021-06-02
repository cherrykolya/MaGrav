import sys
import json
from Polygon import Polygon
from PyQt5 import QtWidgets, uic, QtGui, QtCore
from mydesign import Ui_MainWindow
from PolygonTable import Ui_Form

plgs = []

class TableWindow(QtWidgets.QWidget, Ui_Form):
    """
    Class of Polygon table window
    all interaction of the user with the polygon table is described here
    """
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi() # setup window interface from file PolygonTable
        self.setWindowTitle("Polygon Table")
        self.setWindowIcon(QtGui.QIcon('tableicon.png'))
        for i in range(len(plgs)):                  # displaying poligons
            self.listWidget.addItem(plgs[i].Name)   # when creating a window in list widget
        self.listWidget.itemClicked.connect(self.List_Item_Clicked) # when user clicks on widget initialize function

    def List_Item_Clicked(self, item):
        """
        fills table widget then user clicks on
        polygon in list widget
        :param item:
        :return:
        """
        if len(plgs) != 0:
            poly = plgs[int(item.text()[-1])]
            self.Set_Table_Values(poly)

    def Set_Table_Values(self, poly):
        self.tableWidget.setRowCount(len(poly.Points))
        for i in range(len(poly.Points)):
            self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(str(poly.Points[i][0])))
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(poly.Points[i][1])))
            self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str(poly.Density)))
            self.tableWidget.item(i, 0).setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidget.item(i, 1).setTextAlignment(QtCore.Qt.AlignCenter)

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    class of main window
    all interaction of the user with the mainwindow is described here
    """
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi() # setup window interface from file mydesign
        self.setWindowTitle("MaGrav")
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.OpenPolygonTableAction.triggered.connect(self.Open_Polygon_Table) # when user clicks on widget initialize function
        self.ReadPolygonAction.triggered.connect(self.Read_File) # when user clicks on widget initialize function

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
        dlg.setWindowIcon(QtGui.QIcon('icon.png'))
        dlg.show()

        if dlg.exec_():
            filename = dlg.selectedFiles()
        try:                                   #Handling errors then reading from file
            with open (filename[0]) as file:
                data = json.load(file)
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('icon.png'))
            #msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error then reading file\nOr no files were selected ")
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowIcon(QtGui.QIcon('icon.png'))
            msg.setText("File read succesfully\nThere are %s polygons!" %str(len(data)))
            msg.setWindowTitle("Suckass!")
            msg.exec_()

            for i in range(len(data)): #add polygons to plgs
                poly = Polygon()
                poly.read_from_json(data[i], i)
                plgs.append(poly)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())

