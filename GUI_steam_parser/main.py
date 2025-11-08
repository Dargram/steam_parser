from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from gui_ui import MainWindow
import sys

app = QApplication(sys.argv)
window = MainWindow()
window.show()

with open("GUI_steam_parser/style.qss", "r") as file:
    app.setStyleSheet(file.read())
    
app.exec()