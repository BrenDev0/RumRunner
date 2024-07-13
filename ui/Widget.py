from PySide6.QtGui import *
from PySide6.QtCore import *
from PySide6.QtWidgets import *
import os
from utils.system_scanner import system_scan
from utils.get_data import get_Data

class RumRunner(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('RumRunner')
        
        
        #content

        #line_edit
        self.search_bar = QLineEdit()
        self.search_bar.textChanged.connect(self.populate_list)

        
        #table
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['id', '', 'filepath', 'clicks'])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.hideColumn(0)
        self.table.hideColumn(2)
        self.table.hideColumn(3)

        #buttons
        scan = QPushButton('Scan files')
        scan.clicked.connect(system_scan)


        #layouts 

        #main_layout
        layout = QVBoxLayout()
        layout.addWidget(self.search_bar)
        layout.addWidget(self.table)
        layout.addWidget(scan)

        self.setLayout(layout)

        

    def populate_list(self):
        search = self.search_bar.text()  
        files = get_Data(str(search))
        self.table.setRowCount(len(files))

        if files:
            row = 0
        for file in files:
            self.table.setItem(row, 0, QTableWidgetItem(str(file[0])))
            self.table.setItem(row, 1, QTableWidgetItem(file[1]))
            self.table.setItem(row, 2, QTableWidgetItem(file[2]))
            self.table.setItem(row, 3, QTableWidgetItem(file[3]))
            
            row = row + 1
        else:
            pass  

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return:
            path = self.table.item(self.table.currentRow(), 2).text()
            os.startfile(path)
            
       

   


        



        