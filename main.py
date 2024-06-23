from PySide6.QtWidgets import QApplication   
import sys 
from components.file_filter import exe_files

app = QApplication(sys.argv)

exe_files('firefox')








