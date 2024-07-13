from PySide6.QtWidgets import QApplication   
import sys 
from ui.Widget import RumRunner

app = QApplication(sys.argv)

window = RumRunner()
window.show()

app.exec()







