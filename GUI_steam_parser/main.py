from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from gui_ui import MainWindow
import sys

app = QApplication(sys.argv)

with open("style.qss", "r") as file:
    app.setStyleSheet(file.read())

window = MainWindow()
window.show()
app.exec()