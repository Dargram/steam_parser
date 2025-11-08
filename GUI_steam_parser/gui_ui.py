from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout, QWidget, QPushButton)
from PyQt6.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # === Параметри вікна ===
        self.setWindowTitle("Parsteam")
        self.setFixedSize(500,500)
        
        
        # === Створення ліній ===
        main_layout = QHBoxLayout() # головна лінія
        menu_layout = QVBoxLayout()
        content_layout = QVBoxLayout()

        # === Створення віджетів ===
        self.program_label = QLabel("Software by Dargram")
        self.program_label.setObjectName("soft")
        
        self.game_input = QLineEdit()
        self.game_input.setFixedSize(300,30)
        self.game_input.setPlaceholderText("Enter game name...")
        self.game_input.setObjectName("game_input")
        
        self.currency_input = QLineEdit()
        self.currency_input.setFixedSize(300,30)
        self.currency_input.setPlaceholderText("Enter country's currency...(ua, de, it)")
        self.currency_input.setObjectName("currency_input")
        
        
        self.game_info = QPushButton("Find info")
        self.game_info.setObjectName("game_info_btn")

        # === Створення контейнерів ===
        container = QWidget()
        container.setLayout(main_layout)
        container.setObjectName("container")
        menu = QWidget()
        menu.setLayout(menu_layout)
        menu.setObjectName("menu")
        content = QWidget()
        content.setLayout(content_layout)
        
        
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        
        main_layout.addWidget(menu)
        main_layout.addWidget(content)

        # === Під'єднання віджетів до ліній ===
        content_layout.addWidget(self.program_label, alignment=Qt.AlignmentFlag.AlignCenter)
        content_layout.addWidget(self.game_input, alignment=Qt.AlignmentFlag.AlignCenter)
        content_layout.addWidget(self.currency_input, alignment=Qt.AlignmentFlag.AlignCenter)
        menu_layout.addWidget(self.game_info, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setCentralWidget(container)