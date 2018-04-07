import sys
from PyQt5 import QtWidgets, QtGui

class window():
        app = QtWidgets.QApplication(sys.argv)
        w = QtWidgets.QWidget()
        b = QtWidgets.QPushButton(w)
        l = QtWidgets.QLabel(w)
       # table = QtWidgets.QTableWidget(w)
       # tableItem = QtWidgets.QTableWidgetItem()
       # table.setWindowTitle("Recorded Runs")
       # table.resize(400,250)
       # table.setRowCount(4)
       # table.setColumnCount(4)
        b.setText('Add A Driver')
        l.setText('Test1')
        w.setWindowTitle('Test2')
        b.move(100,50)
        w.setGeometry(500,250,500,300)
       # table.show()
        w.show()
        sys.exit(app.exec_())


        def add_Driver(self):

                btn = QtGui.QPushButton("Add Driver",self)
                btn.clicked.connect(self.Add_Driver_Details)
                btn.resize(100,100)
                btn.move(400,200)
                self.show



window()
