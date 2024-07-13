from PySide6.QtWidgets import QApplication   
import sys 
from ui.Widget import RumRunner
from utils.system_scanner import system_scan

app = QApplication(sys.argv)

window = RumRunner()
window.show()


app.exec()







