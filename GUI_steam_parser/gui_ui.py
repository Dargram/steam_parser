from PyQt6.QtWidgets import (
    QMainWindow, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QWidget
)
from PyQt6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Parsteam")
        self.setFixedSize(600, 400)


        self.program_label = QLabel("Software by Dargram")

        self.game_input = QLineEdit()
        self.game_input.setFixedSize(300, 30)
        self.game_input.setPlaceholderText("Enter game name...")

        self.country_input = QLineEdit()
        self.country_input.setFixedSize(300, 30)
        self.country_input.setPlaceholderText("Enter country's currency")

        self.btn_find = QPushButton("Find game info!")


        content_layout = QVBoxLayout()
        content_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        content_layout.addWidget(self.program_label, alignment=Qt.AlignmentFlag.AlignCenter)
        content_layout.addWidget(self.game_input, alignment=Qt.AlignmentFlag.AlignCenter)
        content_layout.addWidget(self.country_input, alignment=Qt.AlignmentFlag.AlignCenter)
        content_layout.addWidget(self.btn_find, alignment=Qt.AlignmentFlag.AlignCenter)

        content_widget = QWidget()
        content_widget.setLayout(content_layout)


        self.menu_btn_find = QPushButton("Game info")
        self.menu_btn_find.setFixedSize(100, 40)

        menu_layout = QVBoxLayout()
        menu_layout.addWidget(self.menu_btn_find)
        menu_layout.addStretch()

        menu_widget = QWidget()
        menu_widget.setLayout(menu_layout)
        menu_widget.setObjectName("menu")


        main_layout = QHBoxLayout()
        main_layout.addWidget(menu_widget)
        main_layout.addWidget(content_widget, stretch=1)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)