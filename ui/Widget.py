from PySide6.QtWidgets import *
from models.database import Database

class RumRunner(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('RumRunner')
        self.db = Database()
        
        
        #content

        #line_edit
        self.search_bar = QLineEdit()
        
        #table
        self.table = QTableWidget()

        #layouts 

        #main_layout
        layout = QVBoxLayout()
        layout.addWidget(self.search_bar)
        layout.addWidget(self.table)

        self.setLayout(layout)

        