from PyQt6.QtWidgets import (QMainWindow, QLabel, QLineEdit,
                             QVBoxLayout, QWidget, QPushButton, QTextEdit)
from PyQt6.QtCore import Qt
import sys
from steam_api import get_game_info

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Parsteam")
        self.setFixedSize(600, 600)
        

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)


        self.program_label = QLabel("Software by Dargram")
        self.program_label.setObjectName("soft")

        self.game_input = QLineEdit()
        self.game_input.setFixedSize(300, 30)
        self.game_input.setPlaceholderText("Enter game name...")
        self.game_input.setObjectName("game_input")
        
        self.currency_input = QLineEdit()
        self.currency_input.setFixedSize(300, 30)
        self.currency_input.setPlaceholderText("Enter country's currency...(ua, de, it)")
        self.currency_input.setObjectName("currency_input")
        
        self.find_btn = QPushButton("Find Game Info")
        self.find_btn.setObjectName("find_btn")
        self.find_btn.clicked.connect(self.find_game_info)


        self.result_display = QTextEdit()
        self.result_display.setObjectName("result_display")
        self.result_display.setReadOnly(True)
        self.result_display.setFixedHeight(300)


        container = QWidget()
        container.setLayout(main_layout)
        container.setObjectName("container")
        
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop)


        main_layout.addWidget(self.program_label, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.game_input, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.currency_input, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.find_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.result_display, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.setCentralWidget(container)

    def find_game_info(self):
        game_name = self.game_input.text().strip()
        currency_code = self.currency_input.text().strip().lower()
        
        if not game_name or not currency_code:
            self.result_display.setPlainText("Please enter both game name and currency code.")
            return
        
        try:
            game_data = get_game_info(game_name, currency_code)
            if game_data:
                self.display_game_info(game_data)
            else:
                self.result_display.setPlainText("Game not found or error occurred.")
        except Exception as e:
            self.result_display.setPlainText(f"Error: {str(e)}")

    def display_game_info(self, game_data):
        info_text = f"Name: {game_data['name']}\n"
        info_text += f"Game ID: {game_data['steam_appid']}\n"
        
        if 'publishers' in game_data:
            info_text += f"Publishers: {game_data['publishers'][0]}\n"
        else:
            info_text += "Publishers: ?\n"
        
        if game_data['is_free']:
            info_text += "Price: Free to play!\n"
        else:
            price_info = game_data['price_overview']
            if price_info['discount_percent'] == 0:
                info_text += f"Price: {price_info['final_formatted']}\n"
            else:
                info_text += f"Price: {price_info['discount_percent']}% off - {price_info['final_formatted']}\n"
        
        if 'genres' in game_data:
            genres = [genre['description'] for genre in game_data['genres']]
            info_text += f"Genres: {', '.join(genres)}\n"
        
        self.result_display.setPlainText(info_text)